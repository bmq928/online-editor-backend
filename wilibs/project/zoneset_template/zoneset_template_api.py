from wilibs.api_url import ROOT_API
import os as os
from wilibs.common import *
from wilibs.common import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def getlistZoneSetTemplate(token, projectId):
    r = listZoneSetTemplate_RAW(token, projectId)
    return verifyAndReturn(r)


def getZoneSetTeamplateInfo(token, ZoneSetTemplateId):
    r = getZoneSetTemplateInfo_RAW(token, ZoneSetTemplateId)
    return verifyAndReturn(r)


def editZoneSetTemplate(token, payload):
    r = editZoneSetTemplate_RAW(token, payload)
    return verifyAndReturn(r)


def deleteZoneSetTemplate(token, idZoneSetTemplate):
    r = deleteZoneSetTemplate_RAW(token, idZoneSetTemplate)
    return verifyAndReturn(r)


def createZoneSetTemplate(token, payload):
    r = createZoneSetTemplate_RAW(token, payload)
    return verifyAndReturn(r)


# RAW

def listZoneSetTemplate_RAW(token, projectId):
    url = genUrlWithWiId(ROOT_API + '/zone-set-template/list', {'idProject': projectId}, token)
    r = requests.post(url, json={'idProject': projectId}, headers=tokenHeader(token), verify=False)
    return r.json()


def deleteZoneSetTemplate_RAW(token, ZoneSetTemplateId):
    url = genUrlWithWiId(ROOT_API + '/zone-set-template/delete', {'idZoneSetTemplate': ZoneSetTemplateId}, token)
    r = requests.delete(url, json={'idZoneSetTemplate': ZoneSetTemplateId}, headers=tokenHeader(token), verify=False)
    return r.json()


def getZoneSetTemplateInfo_RAW(token, ZoneSetTemplateId):
    url = genUrlWithWiId(ROOT_API + '/zone-set-template/info', {'idZoneSetTemplate': ZoneSetTemplateId}, token)
    r = requests.post(url, json={'idZoneSetTemplate': ZoneSetTemplateId}, headers=tokenHeader(token), verify=False)
    return r.json()


def createZoneSetTemplate_RAW(token, payload):
    url = genUrlWithWiId(ROOT_API + '/zone-set-template/new', payload, token)
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()


def editZoneSetTemplate_RAW(token, payload):
    url = genUrlWithWiId(ROOT_API + '/zone-set-template/edit', payload, token)
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()
