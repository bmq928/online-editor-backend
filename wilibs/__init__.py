import os
import requests

def login(username, password):
  root_url = os.environ.get('USER_RELATED_ROOT_URL', 'http://localhost:3000')
  url = root_url + '/login'
  payload = {
    "username": str(username),
    "password": str(password),
    "whoami": 'main-service'
  }
  r = requests.post(url, json=payload, verify=False)
  return r.json()


def list_project(token):
  root_url = os.environ.get('PROJECT_RELATED_ROOT_URL', 'http://localhost:3000')
  url = root_url +  '/project/list'
  payload = {}
  headers = {
    'Authorization': str(token)
    }
  r = requests.post(url, json=payload, verify=False, headers=headers)
  return r.json()


def list_well_of_project(idProject, start, limit, forward, match):
  root_url = os.environ.get('PROJECT_RELATED_ROOT_URL', 'http://localhost:3000')
  url = root_url +  '/project/well/list'
  payload = {
    "idProject": idProject,
    "start": start,
    "limit": limit,
    "forward": forward,
    "match": match
  }
  r = requests.post(url, json=payload, verify=False)
  return r.json()


def list_reference_curve():
  root_url = os.environ.get('PROJECT_RELATED_ROOT_URL', 'http://localhost:3000')
  url = root_url +  '/project/well/reference-curve/list'
  payload = {}
  r = requests.post(url, json=payload, verify=False)
  return r.json()


def get_curve_info(idReferenceCurve):
  root_url = os.environ.get('PROJECT_RELATED_ROOT_URL', 'http://localhost:3000')
  url = root_url +  '/project/well/reference-curve/info'
  payload = {
    "idReferenceCurve": idReferenceCurve
  }
  r = requests.post(url, json=payload, verify=False)
  return r.json()
