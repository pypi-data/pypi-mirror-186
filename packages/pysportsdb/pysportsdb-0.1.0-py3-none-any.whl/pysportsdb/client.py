import json
import logging
import os
from typing import Optional

import requests
from pysportsdb.constants import DEFAULT_API_KEY, DEFAULT_API_VERSION
from pysportsdb.api_spec import TheSportsDbAPISpec
from pysportsdb.exceptions import PateronOnlyEndpoint

logger = logging.getLogger(__name__)


class TheSportsDbClient(object):
    def __init__(self, **kwargs) -> "TheSportsDbClient":
        self.API_KEY = DEFAULT_API_KEY
        if "api_key" in kwargs:
            self.API_KEY = kwargs.get("api_key")
        self.API_VERSION = DEFAULT_API_VERSION
        if "version" in kwargs:
            self.API_VERSION = kwargs.get("version")

        self.api_spec = TheSportsDbAPISpec(
            api_key=self.API_KEY, version=self.API_VERSION
        )

    def _make_request(self, url: str) -> dict:
        """Makes a request and returns a python dictonary of the response"""
        json_data = {}
        response = requests.get(url)
        if response._content:
            try:
                json_data = json.loads(response._content)
            except UnicodeDecodeError:
                logger.error(
                    f"Received a non-JSON repsonse from request, check API key",
                    extra={"response": response},
                )
            except json.decoder.JSONDecodeError:
                logger.error(
                    f"Received a non-JSON repsonse from request, check API key",
                    extra={"response": response},
                )
        return json_data

    def lookup_event(self, event_id: str) -> dict:
        url = self.api_spec.get_lookup_event_url(id=event_id)
        return self._make_request(url)

    def search_teams(
        self, term: Optional[str] = None, short_code: Optional[str] = None
    ) -> dict:
        url = ""
        if term:
            url = self.api_spec.get_search_teams_url(t=term)
        if short_code:
            url = self.api_spec.get_search_teams_url(sname=short_code)
        return self._make_request(url)

    def search_player_by_name(
        self,
        player_name: Optional[str] = None,
        team_name: Optional[str] = None,
    ) -> dict:
        url = self.api_spec.get_search_teams_url(p=player_name, t=team_name)
        return self._make_request(url)
