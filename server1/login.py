import flask_login

from server1.models import User

lm = flask_login.LoginManager()


@lm.user_loader
def load_user(user_id):
    return User.query.filter_by(uuid=user_id).first()
