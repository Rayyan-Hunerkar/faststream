"""
FastAPI JWT configuration
"""

# pylint: disable=unused-argument

from fastapi_jwt_auth import AuthJWT

# from server.app import app
from server.config.settings import jwtsettings


@AuthJWT.load_config
def get_config():
    """Load AuthJWT settings"""
    return jwtsettings
