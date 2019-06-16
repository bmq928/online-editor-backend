from ....api_url import ROOT_API
from ....api_url import EXPORT_PATH
import os as os
from ....common import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def createImageSet(token, wellId, name):
    r = createImageSet_RAW(token, wellId, name)
    return verifyAndReturn(r)


def deleteImageSet(token, imageSetId):
    r = deleteImageSet_RAW(token, imageSetId)
    return verifyAndReturn(r)

def getListImageSet(token, wellId):
    r = getListImageSet_RAW(token, wellId)
    return verifyAndReturn(r)

#RAW:
def createMarkerTemplate_RAW(token, wellId, name):
    url = ROOT_API + '/marker-set-template/marker-template/new'
    r = requests.post(url, json={'idWell': wellId, 'name':name}, headers=tokenHeader(token), verify=False)
    return r.json()

def deleteMarkerTemplate_RAW(token, imageSetId):
    url = ROOT_API + '/marker-set-template/marker-template/delete'
    r = requests.post(url, json={'idImageSet': imageSetId}, headers=tokenHeader(token), verify=False)
    return r.json()

def getListMarkerTemplate_RAW(token, wellId):
    url = ROOT_API + '/marker-set-template/marker-template/list'
    r = requests.post(url, json={'idWell': wellId}, headers=tokenHeader(token), verify=False)
    return r.json()