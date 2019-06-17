from wilibs.api_url import ROOT_API
from wilibs.api_url import EXPORT_PATH
import os as os
from wilibs.common import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def createMarkerSets(token, wellId, markerSetTemplateId, name):
    r = createMarkerSets_RAW(token, wellId, markerSetTemplateId, name)
    return verifyAndReturn(r)

def getListMarkerSets(token, wellId):
    r = getListMarkerSets_RAW(token, wellId)
    return verifyAndReturn(r)

def deleteMarkerSets(token, markerSetId):
    r = deleteMarkerSets_RAW(token, markerSetId)
    return verifyAndReturn(r)

def getMarkerSetInfo(token, markersetId):
    r = getMarkerSetInfo_RAW(token, markersetId)
    return verifyAndReturn(r)
#RAW:
def createMarkerSets_RAW(token,wellId,  markerSetTemplateId, name):
    url = ROOT_API + '/project/well/marker-set/new'
    r = requests.post(url, json={'idWell': wellId, 'idMarkerSetTemplate':markerSetTemplateId ,'name': name}, headers=tokenHeader(token), verify=False)
    return r.json()


def deleteMarkerSets_RAW(token, markerSetId):
    url = ROOT_API + '/project/well/marker-set/delete'
    r = requests.post(url, json={'idMarkerSet': markerSetId}, headers=tokenHeader(token), verify=False)
    return r.json()

def getListMarkerSets_RAW(token, wellId):
    url = ROOT_API + '/project/well/marker-set/list'
    r = requests.post(url, json={'idWell': wellId}, headers=tokenHeader(token), verify=False)
    return r.json()

def getMarkerSetInfo_RAW(token, MarkerSetId):
    url = ROOT_API + '/project/well/marker-set/info'
    r = requests.post(url, json={'idMarkerSet': MarkerSetId}, headers=tokenHeader(token), verify=False)
    return r.json()
