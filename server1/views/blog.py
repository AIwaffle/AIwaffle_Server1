import flask

import server1.api.blog
import server1.db
import server1.models
import server1.views.api.blog
from .auth import login_required, load_logged_in_user

bp = flask.Blueprint("blog", __name__, url_prefix="/blog")
bp.before_app_first_request(load_logged_in_user)


@bp.route("/")
def index():
    """The blog page

    GET /blog

    Returns: the blog page
    """
    db = server1.db.get_db()
    posts = server1.api.blog.get_posts(db)
    return flask.render_template("blog/index.html", posts=posts)


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    """Create a new post

    Requires login

    GET /blog/create

    Returns: the creation page

    POST /blog/create

    POST form data:
        title(str): the title of the post
        body(str): (optional) the body of the post

    Returns: flask.redirect(blog.index)
    """
    if flask.request.method == "POST":
        title = flask.request.form.get("title", None)
        body = flask.request.form.get("body", None)
        if title is None:
            flask.flash("Title is required")
        else:
            db = server1.db.get_db()
            c_uuid = flask.g.user.uuid
            server1.api.blog.create_post(c_uuid, title, body, db)
            return flask.redirect(flask.url_for('blog.index'))
    return flask.render_template("blog/create.html")


@bp.route("/<int:c_id>/update", methods=("GET", "POST"))
@login_required
def update(c_id):
    # TODO: Update
    raise NotImplemented
    # db = server1.db.get_db()
    # post = server1.views.api.blog.get_post(c_id, db, True, flask.g.user.uuid)
    # return flask.render_template("blog/update.html", post=post)


@bp.route('/<int:c_id>/delete', methods=('POST',))
@login_required
def delete(c_id):
    """Delete a post

    Args:
        c_id (int): the id of the post

    Returns:
        flask.redirect(blog.index)

    Raises: see server1.views.api.blog.get_post for details
    """
    db = server1.db.get_db()
    server1.views.api.blog.get_post(c_id, db, True, flask.g.user.uuid)
    res = server1.api.blog.delete_post(c_id, db)
    return flask.redirect(flask.url_for("blog.index"))
