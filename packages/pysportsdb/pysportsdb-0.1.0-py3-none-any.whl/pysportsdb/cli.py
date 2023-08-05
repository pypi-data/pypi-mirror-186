import json
import logging
import sys
import os

from . import TheSportsDbClient

# this line must be after django.setup() for logging configure
logger = logging.getLogger("pysportsdb")


def lookup_event(event_id: str) -> str:
    API_KEY = os.getenv("THESPORTSDB_API_KEY", "2")
    API_VERSION = os.getenv("THESPORTSDB_API_VERSION", "v1")

    try:
        client = TheSportsDbClient(api_key=API_KEY, api_version=API_VERSION)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import TheSportsDbClient. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    print(client._build_url("lookup_event"))
    json.dumps(client.lookup_event(event_id))


def main():
    if len(sys.argv) > 1:
        result = {}
        if sys.argv[1] == "lookup_event":
            if not len(sys.argv) > 2:
                logger.error(f"lookup_event requires string argument event_id")
                return
            event_id = sys.argv[2]
            result = lookup_event(event_id)
        print(result)


if __name__ == "__main__":
    main()
