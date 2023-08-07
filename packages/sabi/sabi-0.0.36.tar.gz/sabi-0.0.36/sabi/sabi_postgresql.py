import logging
from rebel import Database, PgsqlDriver
from hashids import Hashids
import base64
import json


class Sabi_Postgresql:
    session = None
    logger = None
    db = None
    schema = None
    private_key = None
    server = None
    lambda_client = None
    generic_hashid = None

    def __init__(self, hashid_salt, host, user, password, database, schema=None, port=5432, timezone=""):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.schema = schema
        self.generic_hashid = Hashids(salt=hashid_salt, min_length=16)

        driver = PgsqlDriver(host=host, port=int(port), database=database, user=user, password=password)
        self.db = Database(driver)
        if schema != None:
            self.db.execute(f"SET search_path TO :schema", schema=self.schema)
            self.generic_hashid = Hashids(salt=hashid_salt, min_length=16)

        if timezone != "":
            self.db.execute(f"SET TIMEZONE=:timezone; ", timezone=timezone)

    def encode(self, string):
        if string is None:
            return_value = None
        else:
            return_value = self.generic_hashid.encode(string)

        return return_value

    def decode(self, string):
        if string is None:
            return_value = None
        else:
            return_value = self.generic_hashid.decode(string)
            if len(return_value) > 0:
                return_value = return_value[0]
        return return_value

    def encode_to_base64(self, string):
        return base64.b64encode(bytes(string, "utf-8")).decode("utf-8")

    def decode_from_base64(self, string):
        base64_bytes = string.encode("ascii")
        message_bytes = base64.b64decode(base64_bytes)
        decoded = message_bytes.decode("ascii")
        return decoded

    def query(self, sql, params={}):
        rows = self.db.query(sql, **params)
        return rows

    def refresh_materialized_view(self, logger, schema_name, view_name):
        sql = self.db.sql(
            f"""
            SELECT pid FROM pg_stat_activity WHERE state='active' AND query LIKE 'REFRESH MATERIALIZED VIEW CONCURRENTLY "{schema_name}"."{view_name}"'
            """
        )
        current_processes = sql.query()

        # Cancel an existing run if there is one
        if len(current_processes) > 0:
            logger.info(f"Cancelling existing refresh run for {schema_name} - {view_name}")
            self.db.query("SELECT pg_cancel_backend(:pid);", pid=current_processes[0]["pid"])
        logger.info(f"Starting refresh run for {schema_name} - {view_name}")
        sql = self.db.sql(f'REFRESH MATERIALIZED VIEW CONCURRENTLY "{schema_name}"."{view_name}"')
        sql.execute()

    def check_view_refresh_run(self, logger, schema_name, view_name):
        current_processes = self.db.query(
            f"""SELECT pid FROM pg_stat_activity WHERE state='active' AND query LIKE 'REFRESH MATERIALIZED VIEW CONCURRENTLY "{schema_name}"."{view_name}"';""",
            schema=schema_name,
            view_name=view_name,
        )
        return_value = False

        if len(current_processes) > 0:
            logger.info(f"Confirmed that {schema_name} - {view_name} is running")
            return_value = True
        else:
            logger.info(f"{schema_name} - {view_name} is not running")
        return return_value

    def get_sql_as_string(self, sql):
        full_sql = ""
        for part in sql.parts:
            args = []
            for arg in part["args"]:
                if type(arg) is tuple:
                    append_string = arg[0]
                else:
                    append_string = arg

                if isinstance(append_string, str):
                    args.append("'" + append_string + "'")
                else:
                    args.append(append_string)

            full_sql += part["sql"].replace("?", "{}").format(*args)
        full_sql = full_sql.replace("None", "NULL")
        return full_sql

    def get_filtered_tickets(
        self,
        individual_id,
        start_date=None,
        end_date=None,
        epic=None,
        ticket_type=None,
        label=None,
        team_id=None,
        project_id=None,
        tax_credits_project_id=None,
        fields_to_include=None,
        ticket_ids=None,
    ):
        if team_id is not None:
            teams = team_id.split(",")
            team_id = ""
            for team in teams:
                team_id += str(self.decode(team.strip())) if team_id == "" else f", {self.decode(team.strip())}"
                # team_id = self.decode(team_id)
        if individual_id is not None:
            individuals = individual_id.split(",")
            individual_id = ""
            for individual in individuals:
                current_individual_id = self.decode_from_base64(individual)
                individual_id += str(current_individual_id) if individual_id == "" else f", {current_individual_id}"

        if fields_to_include is not None:
            if epic is not None:
                fields_to_include.append("epic_tickets")
            if label is not None:
                fields_to_include.append("ticket_labels")
            if team_id is not None:
                fields_to_include.append("teams")
            if individual_id is not None:
                fields_to_include.append("ticket_totals")

        sql = self.db.sql(
            """
            WITH ticket_totals AS (
            SELECT 
                ticket.company_integration_id,
                ticket.ticket_id,
                SUM(CASE 
                        WHEN 
                                timesheet.is_timesheet_refundable = false 
                                OR approval_status = 0
                                THEN timesheet.effective_working_minutes
                        ELSE 0
                END) AS considered_non_refundable_work_minutes,
                SUM(CASE 
                        WHEN project_timesheet.timesheet_id IS NOT NULL AND timesheet.is_timesheet_refundable = true THEN  COALESCE(project_timesheet.effective_working_minutes,0)
                        ELSE 0
                END) AS project_allocated_minutes,
                array_agg(DISTINCT(timesheet.individual_id)) filter (where timesheet.individual_id is not null) AS individual_ids,
                array_agg(DISTINCT(timesheet.individual_name) ORDER BY timesheet.individual_name) filter (where timesheet.individual_name is not null) AS names,
                SUM(timesheet.effective_working_minutes) AS total_minutes,
                ticket.ticket_id AS parent
            FROM ticket
            INNER JOIN timesheet ON (timesheet.work_day>=:start_date AND timesheet.work_day<=:end_date) AND (ticket.ticket_id = ANY (timesheet.path) OR ticket.ticket_id = timesheet.ticket_id)
            LEFT JOIN (
                SELECT 
                        SUM(project_timesheet.effective_working_minutes) AS effective_working_minutes,
                        project_timesheet.timesheet_id  
                FROM project_timesheet 
                INNER JOIN timesheet ON timesheet.id = project_timesheet.timesheet_id
                INNER JOIN project ON project.id = project_timesheet.project_id
                WHERE timesheet.work_day >= project.start_date AND timesheet.work_day <= project.end_date """,
            start_date=start_date,
            end_date=end_date,
        )
        if tax_credits_project_id is not None:
            sql.add(""" AND project.id = :tax_credits_project_id""", tax_credits_project_id=tax_credits_project_id)

        sql.add(
            """
                GROUP BY timesheet_id
            ) AS project_timesheet ON project_timesheet.timesheet_id = timesheet.id
            INNER JOIN individual_information ON 
                    individual_information.individual_id = timesheet.individual_id 
                    AND individual_information.company_integration_id = timesheet.company_integration_id
            INNER JOIN active_timesheets ON active_timesheets.id = timesheet.id
            WHERE ((timesheet.work_day>=:start_date AND timesheet.work_day<=:end_date) OR timesheet.work_day IS NULL) AND (active_timesheets.id IS NOT NULL OR timesheet.id > (SELECT MAX(id) FROM active_timesheets))
        """,
            start_date=start_date,
            end_date=end_date,
        )
        if team_id is not None:
            sql = self.add_multiple_ors(sql, team_id, "individual_information.team_ids", True, True)
        if individual_id is not None:
            sql = self.add_multiple_ors(sql, individual_id, "timesheet.individual_id", False, True)

        sql.add("GROUP BY ticket.company_integration_id, ticket.ticket_id)")

        sql.add(
            """,filtered_tickets AS (SELECT
                ticket.company_integration_id,
                ticket.ticket_id,
                ticket.created_at AS ticket_created_at,
                ticket.description,
                ticket.name,
                ticket.archived,
                ticket.project_id,
                ticket.type AS ticket_type,
                ticket.estimate,
                ticket.link"""
        )
        if fields_to_include is None or "epic_tickets" in fields_to_include:
            sql.add(",epic_tickets.epic_ticket_id")
        if fields_to_include is None or "teams" in fields_to_include:
            sql.add(
                """
                ,teams.team_ids,
                teams.team_names"""
            )
        if fields_to_include is None or "states" in fields_to_include:
            sql.add(
                """
                ,states.states_dates[array_position(states.is_wip_state,true)] AS wip_start_date,
                states.states_dates_reversed[array_position(states.is_completed_state_reversed, true)] AS completion_date,
                states.states,
                states.state_names,
                states.states_dates,
                states.is_completed_state,
                states.is_wip_state,
                states.was_in_wip,
                states.was_in_completed,
                states.was_in_waiting"""
            )
        if fields_to_include is None or "parent_information" in fields_to_include:
            sql.add(
                """
                ,parent_information.parent_id,
                parent_information.parent_type,
                parent_information.parent_name"""
            )
        if fields_to_include is None or "ticket_totals" in fields_to_include:
            sql.add(
                """
                ,ticket_totals.total_minutes,
                CAST(ROUND(CAST(ticket_totals.total_minutes/60 AS numeric),2) AS FLOAT) AS total_hours,
                ticket_totals.names AS all_individual_names,
                ticket_totals.individual_ids AS all_individual_ids,
                ticket_totals.project_allocated_minutes,
                CAST(ROUND(CAST(ticket_totals.project_allocated_minutes/60 AS numeric),2) AS FLOAT) AS project_allocated,
                ticket_totals.considered_non_refundable_work_minutes,
                CAST(ROUND(CAST(ticket_totals.considered_non_refundable_work_minutes/60 AS numeric),2) AS FLOAT) AS considered_non_refundable_work
                """
            )
        if fields_to_include is None or "ticket_labels" in fields_to_include:
            sql.add(",ticket_labels.labels")
        sql.add(" FROM ticket")
        if fields_to_include is None or "ticket_totals" in fields_to_include:
            sql.add(
                " LEFT JOIN ticket_totals ON ticket.ticket_id = ticket_totals.ticket_id AND ticket_totals.company_integration_id = ticket.company_integration_id"
            )
            # We add this in here because we need to add chiled tickets when we are filtering by ticket type with EPICS
            # The companion of this is the ticket_ids check later in the query.
            if ticket_type is not None:
                sql.add(" INNER JOIN tickets_with_heirarchy ON tickets_with_heirarchy.ticket_id = ticket.ticket_id")
        if fields_to_include is None or "parent_information" in fields_to_include:
            sql.add(
                """ LEFT JOIN 
                        (SELECT 
                            ticket.company_integration_id, 
                            ticket.ticket_id, 
                            ticket.parent_id, 
                            parent.name AS parent_name, 
                            parent.type AS parent_type 
                        FROM ticket 
                        INNER JOIN ticket AS parent ON parent.company_integration_id = ticket.company_integration_id AND parent.ticket_id = ticket.parent_id
                        ) AS parent_information ON parent_information.company_integration_id = ticket.company_integration_id AND parent_information.ticket_id = ticket.ticket_id"""
            )
        if fields_to_include is None or "ticket_labels" in fields_to_include:
            sql.add(
                """ LEFT JOIN 
                        (SELECT 
                            company_integration_id, 
                            ticket_id, 
                            ARRAY_AGG(DISTINCT(name)) AS labels 
                        FROM ticket_label 
                        WHERE add_or_remove = 'added' AND (ticket_label.start_date,ticket_label.end_date) OVERLAPS (:start_date,:end_date) 
                        GROUP BY company_integration_id, ticket_id
                        ) AS ticket_labels ON ticket_labels.ticket_id = ticket.ticket_id AND ticket_labels.company_integration_id = ticket.company_integration_id""",
                start_date=start_date,
                end_date=end_date,
            )
        if fields_to_include is None or "epic_tickets" in fields_to_include:
            sql.add(
                " LEFT JOIN epic_tickets ON epic_tickets.company_integration_id = ticket.company_integration_id AND epic_tickets.ticket_id = ticket.ticket_id"
            )
        if fields_to_include is None or "teams" in fields_to_include:
            sql.add(
                """ LEFT JOIN (
                    SELECT 
                        array_agg(DISTINCT(individual_team.team_id)) AS team_ids, 
                        array_agg(DISTINCT(team.name)) AS team_names, 
                        ticket_id
                    FROM individual_team
                    INNER JOIN team ON team.id = individual_team.team_id
                    INNER JOIN ticket_totals ON individual_team.individual_id = ANY (ticket_totals.individual_ids)
                    GROUP BY ticket_id) AS teams ON teams.ticket_id = ticket.ticket_id"""
            )
        if fields_to_include is None or "states" in fields_to_include:
            sql.add(
                """ LEFT JOIN 
                        (SELECT
                            ticket_status.company_integration_id,
                            ticket_status.ticket_id,
                            ARRAY_AGG(state_metadata.state_id ORDER BY ticket_status.start_date ASC) AS states,
                            ARRAY_AGG(state.name ORDER BY ticket_status.start_date ASC) AS state_names,
                            ARRAY_AGG(ticket_status.start_date ORDER BY ticket_status.start_date ASC) AS states_dates,
                            ARRAY_AGG(ticket_status.start_date ORDER BY ticket_status.start_date DESC) AS states_dates_reversed,
                            ARRAY_AGG(state_metadata.is_completed ORDER BY ticket_status.start_date ASC) AS is_completed_state,
                            ARRAY_AGG(state_metadata.is_wip ORDER BY ticket_status.start_date ASC) AS is_wip_state,
                            true = ANY (ARRAY_AGG(DISTINCT(state_metadata.is_wip))) AS was_in_wip,
                            true = ANY (ARRAY_AGG(DISTINCT(state_metadata.is_completed))) AS was_in_completed,
                            ARRAY_AGG(state_metadata.is_completed ORDER BY ticket_status.start_date DESC) AS is_completed_state_reversed, 
                            true = ANY (ARRAY_AGG(DISTINCT(state_metadata.is_waiting))) AS was_in_waiting
                        FROM ticket_status
                        INNER JOIN state ON state.company_integration_id = ticket_status.company_integration_id AND state.state_id = ticket_status.state_id
                        LEFT JOIN state_metadata ON ticket_status.state_id = state_metadata.state_id
                        WHERE (ticket_status.start_date,ticket_status.end_date) OVERLAPS (:start_date,:end_date)
                        GROUP BY ticket_status.company_integration_id, ticket_status.ticket_id) AS states
                        ON states.company_integration_id = ticket.company_integration_id AND states.ticket_id = ticket.ticket_id""",
                start_date=start_date,
                end_date=end_date,
            )

        # Dynamic where clauses
        if epic is not None:
            sql = self.add_multiple_ors(sql, epic, "epic_ticket_id")
        if ticket_type is not None:
            sql = self.add_multiple_ors(sql, ticket_type, "ticket.type")
            # We added this for a special case. If the user filters by EPIC, we need to include the EPIC
            # as well as the EPIC's children. We do this by INNER JOINING with the tickets_with_heirarchy
            # in the filtered_tickets WITH statement, and by adding the code below, which adds the children of the tickets ids
            # the user choice into the result.
            if ticket_ids is not None:
                sql.back()  # remove the closing ")"
                sql.add("OR")
                for ticket_id in ticket_ids.split(","):
                    sql.add(
                        """
                        :ticket_id = ANY(tickets_with_heirarchy.path) """,
                        ticket_id=ticket_id.strip(),
                    )
                    sql.add("OR")
            sql.back()
            sql.add(")")
        if label is not None:
            sql = self.add_multiple_ors(sql, label, "ticket_labels.labels", True)
        if team_id is not None:
            sql = self.add_multiple_ors(sql, team_id, "teams.team_ids", True)
        if individual_id is not None:
            sql = self.add_multiple_ors(sql, individual_id, "ticket_totals.individual_ids", True)
        if project_id is not None:
            sql = self.add_multiple_ors(sql, project_id, "ticket.project_id")

        sql.add(")")
        return sql

    def flatten_jira_content(self, content):
        try:
            obj = json.loads(content)
            content = self.flatten_content_recoursive(obj["content"], "text")
        except Exception:
            # If it fails, it was not a json JIRA object ..
            pass

        return content

    def flatten_content_recoursive(self, d, key):
        results = ""
        if type(d) == list:
            for obj in d:
                results += self.flatten_content_recoursive(obj, key)
        elif type(d) == dict:
            for k in d:
                if k == key:
                    results += d[key] + "\n"
                else:
                    results += self.flatten_content_recoursive(d[k], key)

        return results

    def add_multiple_ors(self, sql, values, column_name, any=False, add_null=False):
        values = values.split(",")
        sql.add(" AND (")
        for value in values:
            if any:
                sql.add(f" :col_value = any ({column_name})", col_value=value.strip())
            else:
                sql.add(f" {column_name} = :col_value", col_value=value.strip())
            sql.add(" OR ")
        sql.back()
        if add_null:
            sql.add(f" OR {column_name} IS NULL")
        sql.add(")")
        return sql
