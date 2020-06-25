"""/oauth
"""
import time

import authlib.oauth2
import flask_login
from authlib.integrations import flask_oauth2
from flask import (
    render_template, request, redirect, url_for, jsonify,
    Blueprint,
)
from werkzeug import security

from server1.api import auth, oauth2
from server1.models import db, OAuth2Client
from server1.oauth2 import authorization, require_oauth

bp = Blueprint("oauth", __name__, url_prefix="/oauth")


def current_user():
    return auth.get_user(uuid=flask_login.current_user.get_id())


"""Sample implementation from
https://github.com/authlib/example-oauth2-server/blob/master/website/routes.py
"""


def split_by_crlf(s):
    return [v for v in s.splitlines() if v]


@bp.route("/", methods=("GET",))
@flask_login.login_required
def root():
    user = current_user()
    clients = oauth2.get_clients(user.uuid)

    return render_template("oauth/home.html", user=user, clients=clients)


@bp.route("/create_client", methods=("GET", "POST"))
@flask_login.login_required
def create_client():
    user = current_user()
    if request.method == "GET":
        return render_template("/oauth/create_client.html")

    client_id = security.gen_salt(24)
    client_id_issued_at = int(time.time())
    client = OAuth2Client(
        client_id=client_id,
        client_id_issued_at=client_id_issued_at,
        user_id=user.uuid,
    )

    form = request.form
    client_metadata = {
        "client_name": form["client_name"],
        "client_uri": form["client_uri"],
        "grant_types": split_by_crlf(form["grant_type"]),
        "redirect_uris": split_by_crlf(form["redirect_uri"]),
        "response_types": split_by_crlf(form["response_type"]),
        "scope": form["scope"],
        "token_endpoint_auth_method": form["token_endpoint_auth_method"]
    }
    client.set_client_metadata(client_metadata)

    if form["token_endpoint_auth_method"] == "none":
        client.client_secret = str()
    else:
        client.client_secret = security.gen_salt(48)

    db.session.add(client)
    db.session.commit()
    return redirect(url_for("oauth.root"))


@bp.route("/authorize", methods=["GET", "POST"])
@flask_login.login_required
def authorize():
    user = current_user()

    if request.method == "GET":
        try:
            grant = authorization.validate_consent_request(end_user=user)
        except authlib.oauth2.OAuth2Error as error:
            return error.error
        return render_template("oauth/authorize.html", user=user, grant=grant)

    if request.form["confirm"]:
        grant_user = user
    else:
        grant_user = None
    return authorization.create_authorization_response(grant_user=grant_user)


@bp.route("/token", methods=["POST"])
def issue_token():
    return authorization.create_token_response()


@bp.route("/revoke", methods=["POST"])
def revoke_token():
    return authorization.create_endpoint_response("revocation")


@bp.route("/api/me")
@require_oauth("profile")
def api_me():
    user = flask_oauth2.current_token.user
    return jsonify(id=user.id, username=user.username)
