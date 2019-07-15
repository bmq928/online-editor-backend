from wilibs.api_url import ROOT_API
import os as os
from wilibs.common import *
from wilibs.common import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def createMarkerSetTemplate(token, projectId, name):
    r = createMarkerSetTemplate_RAW(token, projectId, name)
    return verifyAndReturn(r)


def listMarkerSetTemplate(token, projectId):
    r = listMarkerSetTemplate_RAW(token, projectId)
    return verifyAndReturn(r)


def deleteMarkerSetTemplate(token, markerSetTemplateId):
    r = deleteMarkerSetTemplate_RAW(token, markerSetTemplateId)
    return verifyAndReturn(r)


def getMarkerSetTeamplateInfo(token, markerSetTemplateId):
    r = getMarkerSetTemplateInfo_RAW(token, markerSetTemplateId)
    return verifyAndReturn(r)


# RAW
def createMarkerSetTemplate_RAW(token, projectId, name):
    url = genUrlWithWiId(ROOT_API + '/marker-set-template/new', {'idProject': projectId, 'name': name}, token)
    r = requests.post(url, json={'idProject': projectId, 'name': name}, headers=tokenHeader(token), verify=False)
    return r.json()


def listMarkerSetTemplate_RAW(token, projectId):
    url = genUrlWithWiId(ROOT_API + '/marker-set-template/list', {'idProject': projectId}, token)
    r = requests.post(url, json={'idProject': projectId}, headers=tokenHeader(token), verify=False)
    return r.json()


def deleteMarkerSetTemplate_RAW(token, markerSetTemplateId):
    url = genUrlWithWiId(ROOT_API + '/marker-set-template/delete', {'idMarkerSetTemplate': markerSetTemplateId}, token)
    r = requests.delete(url, json={'idMarkerSetTemplate': markerSetTemplateId}, headers=tokenHeader(token),
                        verify=False)
    return r.json()


def getMarkerSetTemplateInfo_RAW(token, markerSetTemplateId):
    url = genUrlWithWiId(ROOT_API + '/marker-set-template/info', {'idMarkerSetTemplate': markerSetTemplateId}, token)
    r = requests.post(url, json={'idMarkerSetTemplate': markerSetTemplateId}, headers=tokenHeader(token), verify=False)
    return r.json()
