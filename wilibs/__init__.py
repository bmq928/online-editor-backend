import requests
import os


def login(username, password):
  
  root_url = os.environ['USER_RELATED_ROOT_URL'] if 'USER_RELATED_ROOT_URL' in os.environ else 'http://localhost:3000'
  url = root_url + '/user/login'
  payload = {
    "username": str(username),
    "password": str(password)
  }
  r = requests.post(url, json=payload, verify=False)
  return r.json()

def list_project():
    
  root_url = os.environ['PROJECT_RELATED_ROOT_URL'] if 'PROJECT_RELATED_ROOT_URL' in os.environ else 'http://localhost:3000'
  url = root_url +  '/project/list'
  payload = {}
  r = requests.post(url, json=payload, verify=False)
  return r.json()


def list_well_of_project(idProject, start, limit, forward, match):
  
  root_url = os.environ['PROJECT_RELATED_ROOT_URL'] if 'PROJECT_RELATED_ROOT_URL' in os.environ else 'http://localhost:3000'
  url = root_url +  '/project/well/list'
  payload = {
    "idProject": str(idProject),
    "start": str(start),
    "limit": str(limit),
    "forward": str(forward),
    "match": str(match)
  }
  r = requests.post(url, json=payload, verify=False)
  return r.json()

def list_reference_curve():
  
  root_url = os.environ['PROJECT_RELATED_ROOT_URL'] if 'PROJECT_RELATED_ROOT_URL' in os.environ else 'http://localhost:3000'
  url = root_url +  '/project/well/reference-curve/list'
  payload = {}
  r = requests.post(url, json=payload, verify=False)
  return r.json()



def get_curve_info(idReferenceCurve):
  
  root_url = os.environ['PROJECT_RELATED_ROOT_URL'] if 'PROJECT_RELATED_ROOT_URL' in os.environ else 'http://localhost:3000'
  url = root_url +  '/project/well/reference-curve/info'
  payload = {
    "idReferenceCurve": str(idReferenceCurve)
  }
  r = requests.post(url, json=payload, verify=False)
  return r.json()