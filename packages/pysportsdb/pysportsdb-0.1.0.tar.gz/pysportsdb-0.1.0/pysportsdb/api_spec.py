import logging
import os
from functools import partial
from urllib.parse import urlencode

from pysportsdb.constants import DEFAULT_API_KEY, DEFAULT_API_VERSION
from pysportsdb.exceptions import ParameterNotAllowed, PateronOnlyEndpoint

logger = logging.getLogger(__name__)


call_method_map = {}


class TheSportsDbAPISpec(object):
    ENDPOINTS = {
        "search_teams": {
            "params": ["t", "sname"],
            "endpoint": "/searchteams.php",
            "patreon_only": True,
        },
        "search_player_by_name": {
            "params": ["p", "t"],
            "endpoint": "/searchplayers.php",
            "patreon_only": False,
        },
        "search_event_by_name": {
            "params": ["e", "s"],
            "endpoint": "/searchevents.php",
            "patreon_only": False,
        },
        "search_event_by_filename": {
            "params": ["e"],
            "endpoint": "/searchfilename.php",
            "patreon_only": False,
        },
        "list_all_sports": {
            "params": [],
            "endpoint": "/all_sports.php",
            "patreon_only": False,
        },
        "list_all_leagues": {
            "params": [],
            "endpoint": "/all_league.php",
            "patreon_only": False,
        },
        "list_all_countries": {
            "params": [],
            "endpoint": "/all_countries.php",
            "patreon_only": False,
        },
        "list_all_leagues_in_country": {
            "params": ["s", "c"],
            "endpoint": "/search_all_leagues.php",
            "patreon_only": False,
        },
        "list_all_teams_in_league": {
            "params": ["s", "c"],
            "endpoint": "/lookup_all_teams.php",
            "patreon_only": True,
        },
        "list_all_players_on_team": {
            "params": ["id"],
            "endpoint": "/lookup_all_players.php",
            "patreon_only": True,
        },
        "list_users_loved_teams_and_players": {
            "params": ["u"],
            "endpoint": "/searchloves.php",
        },
        "lookup_league": {
            "params": ["id"],
            "endpoint": "/lookupleague.php",
            "patreon_only": True,
        },
        "lookup_team": {
            "params": ["id"],
            "endpoint": "/lookupteam.php",
            "patreon_only": True,
        },
        "lookup_player": {
            "params": ["id"],
            "endpoint": "/lookupplayer.php",
            "patreon_only": False,
        },
        "lookup_event": {
            "params": ["id"],
            "endpoint": "/lookupevent.php",
            "patreon_only": True,
        },
        "lookup_event_statistics": {
            "params": ["id"],
            "endpoint": "/lookupeventstats.php",
            "patreon_only": True,
        },
        "lookup_event_statistics": {
            "params": ["id"],
            "endpoint": "/lookupeventstats.php",
            "patreon_only": True,
        },
        "lookup_event_lineup": {
            "params": ["id"],
            "endpoint": "/lookuplineup.php",
            "patreon_only": True,
        },
        "lookup_event_timeline": {
            "params": ["id"],
            "endpoint": "/lookuptimeline.php",
            "patreon_only": True,
        },
        "lookup_player_honours": {
            "params": ["id"],
            "endpoint": "/lookuphonours.php",
            "patreon_only": False,
        },
        "lookup_player_milestones": {
            "params": ["id"],
            "endpoint": "/lookupmilestones.php",
            "patreon_only": False,
        },
        "lookup_player_former_teams": {
            "params": ["id"],
            "endpoint": "/lookupformerteams.php",
            "patreon_only": False,
        },
        "lookup_player_contracts": {
            "params": ["id"],
            "endpoint": "/lookupcontracts.php",
            "patreon_only": False,
        },
        "lookup_event_results": {
            "params": ["id"],
            "endpoint": "/eventresults.php",
            "patreon_only": False,
        },
        "lookup_event_tv": {
            "params": ["id"],
            "endpoint": "/lookuptv.php",
            "patreon_only": True,
        },
        "lookup_table_by_league_and_season": {
            "params": ["l", "s"],
            "endpoint": "/lookuptable.php",
            "patreon_only": False,
        },
        "lookup_equipment_by_team": {
            "params": ["id"],
            "endpoint": "/lookupequipment.php",
            "patreon_only": False,
        },
        "livescore": {
            "params": ["s", "l"],
            "endpoint": "/livescore.php",
            "patreon_only": True,
            "version": "v2",
        },
    }
    API_BASE_URL = os.getenv(
        "THESPORTSDB_API_BASE_URL", "https://www.thesportsdb.com/api"
    )
    API_RESPONSE_TYPE = os.getenv("THESPORTSDB_API_RESPONSE_TYPE", "json")

    def __init__(self, **kwargs):
        self.API_KEY = DEFAULT_API_KEY
        self.API_VERSION = DEFAULT_API_VERSION

        self.LIMITED_KEY = False
        if "api_key" in kwargs:
            self.API_KEY = kwargs.get("api_key")
        if "version" in kwargs:
            self.API_VERSION = kwargs.get("version")

        if self.API_KEY == DEFAULT_API_KEY:
            logger.warning("Default API key has limited endpoint access")
            self.LIMITED_KEY = True

    def init_call_method_map(self):
        global call_method_map
        for call in self.ENDPOINTS.keys():
            call_method_map["get_%s_url" % call] = {
                "base_name": "_get_CALL_url",
                "call": call,
            }

    def _get_CALL_url(self, call: str, **kwargs) -> str:
        call_def = self.ENDPOINTS.get(call)

        if call_def.get("patreon_only") and self.LIMITED_KEY:
            raise PateronOnlyEndpoint

        kwargs_allowed = True
        if call_def.get("params"):
            for kwarg in kwargs.keys():
                kwargs_allowed = kwarg in call_def.get("params")

        kwargs_no_args_allowed = kwargs.keys() and not call_def.get("params")

        if not kwargs_allowed or kwargs_no_args_allowed:
            args = list(kwargs.keys())
            raise ParameterNotAllowed(
                f"Call {call} does not support arguments: {args}"
            )

        params = urlencode(kwargs)
        endpoint = call_def.get("endpoint")
        if params:
            endpoint = call_def.get("endpoint") + "?" + params

        version = self.API_VERSION
        if call_def.get("version"):
            version = call_def.get("version")

        url_parts = [
            self.API_BASE_URL,
            version,
            self.API_RESPONSE_TYPE,
            self.API_KEY,
            endpoint,
        ]
        return "/".join(s.strip("/") for s in url_parts)

    def __getattr__(self, name):
        global call_method_map
        if not call_method_map:
            self.init_call_method_map()
        di = call_method_map.get(name, None)
        if di is not None:
            result = partial(getattr(self, di["base_name"]), di["call"])
            setattr(self, name, result)
            return result
        else:
            raise AttributeError

    @classmethod
    def available_endpoints(cls):
        return list(cls.ENDPOINTS.keys())
