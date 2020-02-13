import server1.db
import server1.models
import server1.api.statistics


def before_request():
    db = server1.db.get_db()
    server1.api.statistics.update_total(0, db)
