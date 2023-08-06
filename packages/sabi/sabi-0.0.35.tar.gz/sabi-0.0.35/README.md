# Sabi

## To set up the repo:

`pip install wheel`
`pip install twine`

API for the scientific advamced business intelligence tool at sabi.ai.

## To Deploy:

- Make the changes
- Increment the version (setup.py)

`make deploy`

## Example usage:

`pip install sabi`

```
from sabi import Sync

api_key = <your api key>

sabi_sync_api = Sync(api_key)
sabi_sync_api.get_missing_individuals()
```

