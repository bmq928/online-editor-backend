"""
    This module contain API to login/logout, change user information.
"""

import requests
from ..api_url import AUTH_API
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def login(username, password):
    r = login_RAW(username, password)
    if r['code'] == 200:
        return True, r['content']
    return False, r['reason']

def login_RAW(username, password):
    payload = {
        "username": username,
        "password": password
    }
    url = AUTH_API + '/login'
    r = requests.post(url, json = payload, verify=False)
    return r.json()