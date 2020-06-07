from server1.models import OAuth2Client


def get_clients(uuid: str) -> list:
    return OAuth2Client.query.filter_by(user_id=uuid).all()
