"""This module provides views with url prefix /api/blog
"""
import flask

import server1.api
import server1.api.auth
import server1.api.blog
import server1.db
import server1.models

bp = flask.Blueprint("api_blog", __name__, url_prefix="/api/blog")


@bp.route("/all", methods=("GET",))
def all_():
    """Get all of the posts

    GET /api/blog/all

    Returns: a json object of a dict with id as key and post as value
        post: a json object
            id(int): the id of the post
            author_uuid(string): the uuid of the author
            created(DateTime): the time when the post is created
            title(str): the title of the post
            body(str): the body of the post
    """
    db = server1.db.get_db()
    res = dict()
    for post in server1.api.blog.get_posts(db):
        res.update({post.id: post})
    return res


@bp.route("/get", methods=("POST",))
def post_get():
    """Get one post

    POST /api/blog/get

    Returns: a json object, the post
        id(int): the id of the post
        author_uuid(string): the uuid of the author
        created(DateTime): the time when the post is created
        title(str): the title of the post
        body(str): the body of the post

    Raises: flask.abort(400) when the id is not provided
    Raises: flask.abort(404) when the post is not found
    """
    db = server1.db.get_db()
    c_id = flask.request.json.get("id", None)
    if c_id is None:
        flask.abort(400)
    post = server1.api.blog.get_post(c_id, db)
    if post is None:
        flask.abort(404)
    return post


def get_user(db_session) -> server1.models.User:
    """Get the user from json

    Args:
        db_session (): the database session

    For POST requests middleware

    POST json data (tier 1):
        uuid(str): the uuid of the user
        expires(float): the expire time of the session
        token(str): the token of the session

    POST json data (tier 2):
        username(str): the username of the user
        password(str): the password of the user

    Returns: The user object

    Raises: flask.abort(403) if the user is invalid
    """
    c_uuid = flask.request.json.get("uuid", None)
    expires = flask.request.json.get("expires", None)
    token = flask.request.json.get("token", None)
    if not all((c_uuid, expires, token)):
        username = flask.request.json.get("username", None)
        password = flask.request.json.get("password", None)
        if not all((username, password)):
            flask.abort(403)
        res = server1.api.auth.login(username, password, db_session,
                                     flask.current_app.config["SESSION_EXPIRES"])
        c_uuid = res["uuid"]
        expires = res["expires"]
        token = res["token"]
    user = server1.api.auth.load_logged_in_user(c_uuid, expires, token)
    if user is None:
        flask.abort(403)
    return user


def get_post(c_id, db_session, check_author: bool = True, author_uuid=None) -> server1.models.Post:
    """Get a post with/without author check

    Args:
        c_id (int): the id of the post
        db_session (): the database session
        check_author (bool): whether to check the author
        author_uuid (str): the uuid of the author (only when check_author)

    Returns: the post object

    Raises: flask.abort(403) when the author check fails
    Raises: flask.abort(404) when the post does not exist
    """
    post = server1.api.blog.get_post(c_id, db_session)
    if post is None:
        flask.abort(404)

    if check_author and post.author_uuid != author_uuid:
        # TODO: If you want specific author, change here
        flask.abort(403)
    return post


@bp.route("/create", methods=("POST",))
def create():
    """Create a new post

    POST /api/blog/create

    POST json data:
        {user info} see get_user for details
        title(str): the title of the post
        body(str): (optional) the body of the post

    Returns: the id of the post

    Raises: see get_user for details
    Raises: flask.abort(403) when title is not provided
    """
    db = server1.db.get_db()
    user = get_user(db)
    title = flask.request.json.get("title", None)
    if not title:
        flask.abort(403)
    body = flask.request.json.get("body", None)
    c_id = server1.api.blog.create_post(user.uuid, title, body, db)
    return c_id


@bp.route("/delete", methods=("POST",))
def post_delete():
    """Delete a post

    POST /api/blog/delete

    POST json data:
        {user info} see get_user for details
        id(int): the id of the post

    Returns: whether the blog is deleted

    Raises: see get_user for details
    Raises: see get_post(check_author=True, ...) for details
    """
    db = server1.db.get_db()
    c_id = flask.request.json.get("id", None)
    user = get_user(db)
    get_post(c_id, db, True, user.uuid)
    res = server1.api.blog.delete_post(c_id, db)
    return res
