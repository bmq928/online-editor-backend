from wilibs.api_url import ROOT_API
import os as os
from wilibs.common import *
from wilibs.common import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def createZoneTemplate(token, payload):
    r = createZoneTemplate_RAW(token, payload)
    return verifyAndReturn(r)

def deleteZoneSetTemplate(token, ZoneTemplateId):
    r = deleteZoneTemplate_RAW(token, ZoneTemplateId)
    return verifyAndReturn(r)

def editZoneTemplate(token, payload):
    r = editZoneTemplate_RAW(token, payload)
    return verifyAndReturn(r)

#RAW
def editZoneTemplate_RAW(token, payload):
    url = ROOT_API + '/zone-set-template/zone-template/edit'
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()

def createZoneTemplate_RAW(token, payload):
    url = ROOT_API + '/zone-set-template/zone-template/new'
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()

def deleteZoneTemplate_RAW(token, ZoneTemplateId):
    url = ROOT_API + '/zone-set-template/zone-template/delete'
    r = requests.delete(url, json={'idZoneTemplate':ZoneTemplateId}, headers=tokenHeader(token), verify=False)
    return r.json()


