from wilibs.api_url import ROOT_API
from wilibs.api_url import EXPORT_PATH
import os as os
# from ....common import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def createMarker(token, wellId, name):
    r = createImageSet_RAW(token, wellId, name)
    return verifyAndReturn(r)

def deleteMarker(token, imageSetId):
   
    return verifyAndReturn(r)

def getListMarker(token, wellId):
   
    return verifyAndReturn(r)

#RAW:
def createMarker_RAW(token, wellId, name):
    url = ROOT_API + '/project/well/marker-set/marker/new'
    r = requests.post(url, json={'idWell': wellId, 'name':name}, headers=tokenHeader(token), verify=False)
    return r.json()

def deleteMarker_RAW(token, imageSetId):
    url = ROOT_API + '/project/well/marker-set/marker/delete'
    r = requests.post(url, json={'idImageSet': imageSetId}, headers=tokenHeader(token), verify=False)
    return r.json()

def getListMarker_RAW(token, wellId):
    url = ROOT_API + '/project/well/marker-set/marker/list'
    r = requests.post(url, json={'idWell': wellId}, headers=tokenHeader(token), verify=False)
    return r.json()