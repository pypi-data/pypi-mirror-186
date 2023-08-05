class PateronOnlyEndpoint(Exception):
    """Endpoint not available unelss using a Patreon-supporter API key"""


class ParameterNotAllowed(Exception):
    """Parameter passed to API call is not allowed"""
