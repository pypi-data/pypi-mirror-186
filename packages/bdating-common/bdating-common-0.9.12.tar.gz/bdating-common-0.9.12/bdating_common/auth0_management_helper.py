import requests
import os
from typing import Dict, Any
import json


def get_access_token() -> str:
    client_id = os.environ['AUTH0_MANAGEMENT_APP_CLIENT_ID']
    client_secret = os.environ['AUTH0_MANAGEMENT_APP_CLIENT_SECRET']
    audience = os.environ['AUTH0_MANAGEMENT_APP_AUDIENCE']
    audience_domain = audience.split('/')[2]
    url = f"https://{audience_domain}/oauth/token"
    resp = requests.post(url,
                         data={
                             "client_id": client_id,
                             "client_secret": client_secret,
                             "audience": audience,
                             "grant_type": "client_credentials"}
                         ).json()

    return resp['access_token']


def update_app_metadata(user_id: str, app_metadata: Dict[str, Any]) -> Dict[str, Any]:
    token = get_access_token()
    audience = os.environ['AUTH0_MANAGEMENT_APP_AUDIENCE']
    audience_domain = audience.split('/')[2]
    url = f"https://{audience_domain}/api/v2/users/{user_id}"
    resp = requests.patch(
        url,
        data=json.dumps({
            "app_metadata": app_metadata
        }),
        headers={
            'Authorization': 'Bearer '+token,
            'content-type': 'application/json',
        })
    return resp.json()


