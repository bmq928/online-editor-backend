from wilibs.api_url import ROOT_API
import os as os
from wilibs.common import *
from wilibs.common import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def createZoneSet(token, payload):
    r = createZoneSet_RAW(token, payload)
    return verifyAndReturn(r)

def editZoneSet(token, payload):
    r = editZoneSet_RAW(token, payload)
    return verifyAndReturn(r)

def deleteZoneSet(token, idZoneSet):
    r = deleteZoneSet_RAW(token, idZoneSet)
    return verifyAndReturn(r)


def getZoneSetInfo(token, idZoneSet):
    r = getZoneSetInfo_RAW(token, idZoneSet)
    return verifyAndReturn(r)


def getListZoneSets(token, idWell):
    r = getListZoneSets_RAW(token, idWell)
    return verifyAndReturn(r)

#RAW
def editZoneSet_RAW(token, payload):
    url = ROOT_API + '/project/well/zone-set/edit'
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()

def createZoneSet_RAW(token, payload):
    url = ROOT_API + '/project/well/zone-set/new'
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()

def getListZoneSets_RAW(token, wellId):
    url = ROOT_API + '/project/well/zone-set/list'
    r = requests.post(url, json={'idWell': wellId}, headers=tokenHeader(token), verify=False)
    return r.json()


def deleteZoneSet_RAW(token, idZoneSet):
    url = ROOT_API + '/dustbin/delete'
    r = requests.post(url, json={'idObject': idZoneSet, 'type': 'zoneset'}, headers=tokenHeader(token), verify=False)
    return r.json()


def getZoneSetInfo_RAW(token, idZoneSet):
    url = ROOT_API + '/project/well/zone-set/info'
    r = requests.post(url, json={'idZoneSet': idZoneSet}, headers=tokenHeader(token), verify=False)
    return r.json()