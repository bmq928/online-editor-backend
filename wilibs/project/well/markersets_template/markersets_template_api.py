from ....api_url import ROOT_API
from ....api_url import EXPORT_PATH
from ....common import *
import requests

def createMarkerset(token, projectId, **data):
    payload = {
        'idproject' : projectId
    }
    if 'name' in data:
        payload['name'] = data['name']
    r = createMarkerSetTemplate_RAW(token, payload)
    return verifyAndReturn(r)

def listMarkerSetTemplate(token, projectId):
    payload = {
        'idProject' : projectId
    }
    r = listMarkerSetTemplate_RAW(token, payload)
    if 'content' in r:
        return r['content']
    return verifyAndReturn(r)

def deleteMarkerSetTemplate(token, markerSetTemplateId):
    r = deleteMarkerSetTemplate_RAW(token, markerSetTemplateId)
    return verifyAndReturn(r)

#RAW
def createMarkerSetTemplate_RAW(token, payload):
    url = ROOT_API + '/project/marker-set/new'
    r = requests.post(url, json = payload, headers = tokenHeader(token))
    return r.json()

def listMarkerSetTemplate_RAW(token, projectId):
    url = ROOT_API + '/project/marker-set-template/list'
    r = requests.post(url, json = {'idProject' : projectId} , headers = tokenHeader(token))
    return r.json()

def deleteMarkerSetTemplate_RAW(token, markerSetTemplateId):
    url = ROOT_API + '/project/marker-set-template/delete'
    r = requests.post(url, json = {'idMarkerTemplate' :markerSetTemplateId} , headers = tokenHeader(token))
    return r.json()