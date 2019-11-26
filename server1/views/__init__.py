from .api.auth import bp as api_auth_bp
from .api.model import bp as api_model_bp
from .auth import bp as auth_bp
from .root import bp as root_bp
from .model import bp as model_bp

bps = (api_auth_bp,
       api_model_bp,
       auth_bp,
       root_bp,
       model_bp)
