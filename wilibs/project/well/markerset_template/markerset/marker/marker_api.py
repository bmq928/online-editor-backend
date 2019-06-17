from wilibs.api_url import ROOT_API
from wilibs.api_url import EXPORT_PATH
import os as os
from wilibs.common import *
import requests
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def createMarker(token,markerSetId, markerTemplateId, name):
    r = createMarker_RAW(token, markerSetId, markerTemplateId, name)
    return verifyAndReturn(r)

def deleteMarker(token, markerId):
    r = deleteMarker_RAW(token, markerId)
    return verifyAndReturn(r)

def getListMarker(token, markerSetId):
    r = getListMarker_RAW(token, markerSetId)
    return verifyAndReturn(r)

#RAW:
def createMarker_RAW(token, markerSetId, markerTemplateId, name):
    url = ROOT_API + '/project/well/marker-set/marker/new'
    r = requests.post(url, json={'idMarkerSet':markerSetId, 'idMarkerTemplate':markerTemplateId, 'name':name}, headers=tokenHeader(token), verify=False)
    return r.json()

def deleteMarker_RAW(token, markerId):
    url = ROOT_API + '/project/well/marker-set/marker/delete'
    r = requests.post(url, json={'idMarker': markerId}, headers=tokenHeader(token), verify=False)
    return r.json()

def getListMarker_RAW(token, markerSetId):
    url = ROOT_API + '/project/well/marker-set/marker/list'
    r = requests.post(url, json={'idMarkerSet': markerSetId}, headers=tokenHeader(token), verify=False)
    return r.json()
