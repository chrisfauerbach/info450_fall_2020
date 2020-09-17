import base64
import logging
import os 

import requests

def get_access_token():
    token = ""
    url = "https://accounts.spotify.com/api/token"
    body_parameters = {}
    body_parameters['grant_type'] = "client_credentials"
    headers = {}
    secret_client = f"{CLIENT_ID}:{CLIENT_SECRET}"
    encoded = base64.b64encode(bytes(secret_client, "utf-8")).decode('utf-8')

    headers['Authorization'] = f"Basic {encoded}"
    response = requests.post(url, headers=headers, data=body_parameters)
    logging.debug(str(response))
    logging.debug(response.text)
    token = response.json().get('access_token')
    return token


def search(q):

    access_token = get_access_token()

    logging.debug(f"Searching for: {q}")
    search_url = "https://api.spotify.com/v1/search"
    parms = {}
    parms["q"] = q
    parms["type"] = "album,artist"
    logging.debug("My search is: %s", str(parms))
    headers = {}
    headers['Authorization'] = f"Bearer {access_token}"
    result = requests.get(search_url, headers=headers, params=parms)
    logging.debug(str(result))
    logging.debug(result.text)

if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    CLIENT_ID = os.environ['CLIENT_ID']
    CLIENT_SECRET = os.environ['CLIENT_SECRET']
    logging.debug(f"Client ID: {CLIENT_ID}")
    logging.debug("Length of client secret: %s", len(CLIENT_SECRET))
    search("berhana")
    search("beyonce")