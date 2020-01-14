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
from .model import bp as model_bp
from .blog import bp as blog_bp

bps = (api_auth_bp,
       api_model_bp,
       auth_bp,
       root_bp,
       model_bp,
       blog_bp)
