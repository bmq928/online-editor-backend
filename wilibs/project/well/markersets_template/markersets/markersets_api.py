from ....api_url import ROOT_API
from ....api_url import EXPORT_PATH
import os as os
from ....common import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def createMarkerSets(token, wellId, name):
    r = createImageSet_RAW(token, wellId, name)
    return verifyAndReturn(r)

def getListMarkerSets(token, imageSetId, **data):
    data['idImageSet'] = imageSetId
    r = editImageSetInfo_RAW(token, data)
    return verifyAndReturn(r)

def deleteMarkerSets(token, imageSetId):
    r = deleteImageSet_RAW(token, imageSetId)
    return verifyAndReturn(r)

#RAW:
def createMarkerSets_RAW(token, ):
    url = ROOT_API + '/project/well/marker-set/new'
    r = requests.post(url, json={'idWell': wellId, 'name':name}, headers=tokenHeader(token), verify=False)
    return r.json()

def deleteMarkerSets_RAW(token, imageSetId):
    url = ROOT_API + '/project/well/marker-set/delete'
    r = requests.post(url, json={'idImageSet': imageSetId}, headers=tokenHeader(token), verify=False)
    return r.json()

def getListMarkerSets_RAW(token, wellId):
    url = ROOT_API + '/project/well/marker-set/list'
    r = requests.post(url, json={'idWell': wellId}, headers=tokenHeader(token), verify=False)
    return r.json()