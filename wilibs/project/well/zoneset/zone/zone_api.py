from wilibs.api_url import ROOT_API
import os as os
from wilibs.common import *
from wilibs.common import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def createZone(token, payload):
    r = createZone_RAW(token, payload)
    return verifyAndReturn(r)

def deleteZoneSetTemplate(token, ZoneId):
    r = deleteZone_RAW(token, ZoneId)
    return verifyAndReturn(r)

def editZoneTemplate(token, payload):
    r = editZone_RAW(token, payload)
    return verifyAndReturn(r)

def getListZone(token, ZoneSetId):
    r = getListZone_RAW(token, ZoneSetId)
    return verifyAndReturn(r)

#RAW
def createZone_RAW(token, payload):
    url = ROOT_API + '/project/well/zone-set/zone/new'
    r = requests.post(url,json = {payload}, headers=tokenHeader(token), verify=False)
    return r.json()

def deleteZone_RAW(token, ZoneId):
    url = ROOT_API + '/project/well/zone-set/zone/delete'
    r = requests.delete(url, json={'idZone':ZoneId}, headers=tokenHeader(token), verify=False)
    return r.json()

def editZone_RAW(token, payload):
    url = ROOT_API + '/project/well/zone-set/zone/edit'
    r = requests.delete(url, json={'idZone':payload}, headers=tokenHeader(token), verify=False)
    return r.json()

def getListZone_RAW(token, ZoneSetId):
    url = ROOT_API + '/project/well/zone-set/zone/list'
    r = requests.post(url, json={'idZoneSet':ZoneSetId}, headers=tokenHeader(token), verify=False)
    return r.json()