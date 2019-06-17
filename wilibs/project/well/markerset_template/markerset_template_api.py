from wilibs.api_url import ROOT_API
import os as os
from wilibs.common import *
from wilibs.common import *
import requests

def createMarkerSetTemplate(token, projectId, name):
    r = createMarkerSetTemplate_RAW(token, projectId, name)
    return verifyAndReturn(r)

def listMarkerSetTemplate(token, projectId):
    r = listMarkerSetTemplate_RAW(token, projectId)
    if 'content' in r:
        return r['content']
    return verifyAndReturn(r)

def deleteMarkerSetTemplate(token, markerSetTemplateId):
    r = deleteMarkerSetTemplate_RAW(token, markerSetTemplateId)
    return verifyAndReturn(r)

#RAW
def createMarkerSetTemplate_RAW(token, projectId, name):
    url = ROOT_API + '/marker-set-template/new'
    r = requests.post(url, json ={'idProject': projectId, 'name': name}, headers=tokenHeader(token), verify=False)
    return r.json()

def listMarkerSetTemplate_RAW(token, projectId):
    url = ROOT_API + '/marker-set-template/list'
    r = requests.post(url, json={'idProject': projectId}, headers=tokenHeader(token), verify=False)
    return r.json()

def deleteMarkerSetTemplate_RAW(token, markerSetTemplateId):
    url = ROOT_API + '/marker-set-template/delete'
    r = requests.post(url, json={'idMarkerSetTemplate': markerSetTemplateId}, headers=tokenHeader(token), verify=False)
    return r.json()
