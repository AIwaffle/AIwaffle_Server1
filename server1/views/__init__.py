"""This package provides views with url prefix /
Also records the full blueprint list

Site map:
 /
 /api
 /api/auth
 /api/auth/register POST
 /api/auth/login POST
 /api/blog
 /api/blog/all GET
 /api/blog/get POST
 /api/blog/create POST
 /api/blog/delete POST
 /api/model
 /api/model/new POST
 /api/model/iter POST
 /model
 /blog
"""
from .api.auth import bp as api_auth_bp
from .api.model import bp as api_model_bp
from .auth import bp as auth_bp
from .root import bp as root_bp
from .oauth import bp as oauth_bp

bps = (api_auth_bp,
       api_model_bp,
       auth_bp,
       root_bp,
       oauth_bp,
       )
