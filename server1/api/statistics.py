import server1.models
import server1.db


def update_total(id_, db_session):
    record = server1.models.Statistics.query.filter(server1.models.Statistics.id == id_).first()
    if record is None:
        record = server1.models.Statistics(id_)
        db_session.add(record)
        db_session.commit()
        record = server1.models.Statistics.query.filter(server1.models.Statistics.id == id_).first()
    record.access_total += 1
    db_session.commit()
    print(record.access_total)


def get_total(id_, db_session) -> int:
    record = server1.models.Statistics.query.filter(server1.models.Statistics.id == id_).first()
    if record is None:
        return 0
    return record.access_total
