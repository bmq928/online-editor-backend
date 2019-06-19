from wilibs.api_url import ROOT_API
import os as os
from wilibs.common import *
from wilibs.common import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def createZoneSetTemplate(token, projectId, name):
    r = createZoneSetTemplate_RAW(token, projectId, name)
    return verifyAndReturn(r)

def getlistZoneSetTemplate(token, projectId):
    r = listZoneSetTemplate_RAW(token, projectId)
    return verifyAndReturn(r)

def deleteMarkerSetTemplate(token, ZoneSetTemplateId):
    r = deleteZoneSetTemplate_RAW(token, ZoneSetTemplateId)
    return verifyAndReturn(r)

def getZoneSetTeamplateInfo(token, ZoneSetTemplateId):
    r = getZoneSetTemplateInfo_RAW(token, ZoneSetTemplateId)
    return verifyAndReturn(r)
#RAW
def createZoneSetTemplate_RAW(token, projectId, name):
    url = ROOT_API + '/zone-set-template/new'
    r = requests.post(url, json={'idProject': projectId, 'name': name}, headers=tokenHeader(token), verify=False)
    return r.json()

def listZoneSetTemplate_RAW(token, projectId):
    url = ROOT_API + '/zone-set-template/list'
    r = requests.post(url, json={'idProject': projectId}, headers=tokenHeader(token), verify=False)
    return r.json()

def deleteZoneSetTemplate_RAW(token, ZoneSetTemplateId):
    url = ROOT_API + '/zone-set-template/delete'
    r = requests.delete(url, json={'idZoneSetTemplate': ZoneSetTemplateId}, headers=tokenHeader(token), verify=False)
    return r.json()

def getZoneSetTemplateInfo_RAW(token, ZoneSetTemplateId):
    url = ROOT_API + '/zone-set-template/info'
    r = requests.post(url, json={'idZoneSetTemplate': ZoneSetTemplateId}, headers=tokenHeader(token), verify=False)
    return r.json()