import flask

import server1.api.statistics
import server1.db
import server1.models

bp = flask.Blueprint("api_statistics", __name__, url_prefix="/api/statistics")


@bp.route("/total", methods=("GET",))
def total():
    db = server1.db.get_db()
    return str(server1.api.statistics.get_total(0, db))
