import json
import base64

import bs4

def test_create_client(client, auth):
    auth.login()

    resp = client.get("/oauth/create_client")
    assert resp.status_code == 200

    resp = client.post("/oauth/create_client", data={
        "client_name": "Hi",
        "client_uri": "https://authlib.org",
        "scope": "profile",
        "redirect_uri": "https://authlib.org",
        "grant_type": "authorization_code\npassword",
        "response_type": "code",
        "token_endpoint_auth_method": "client_secret_basic",
    })
    assert resp.status_code == 302

    resp = client.get("/oauth/")
    assert resp.status_code == 200
    soup = bs4.BeautifulSoup(resp.data, "html.parser")
    oauth_clients = soup.find_all("pre")
    assert len(oauth_clients) == 1
    oauth_client = oauth_clients[0]
    assert isinstance(oauth_client, bs4.element.Tag)
    client_data = json.loads(oauth_client.text.strip().split("\n")[0])
    assert "client_id" in client_data
    assert "client_secret" in client_data
