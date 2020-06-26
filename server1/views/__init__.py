"""This package provides views with url prefix /
Also records the full blueprint list

Site map:
 /
 /api
 /api/model
 /auth
 /oauth
"""
from .api.model import bp as api_model_bp
from .auth import bp as auth_bp
from .oauth import bp as oauth_bp
from .root import bp as root_bp
from .api.auth import bp as api_auth_bp

bps = (
    api_model_bp,
    auth_bp,
    root_bp,
    oauth_bp,
    api_auth_bp,
)
