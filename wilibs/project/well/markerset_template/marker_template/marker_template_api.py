from ....api_url import ROOT_API
from ....api_url import EXPORT_PATH
import os as os
from ....common import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def createMarkerTemplate(token, MarkerSetTemplateId, payload):
    payload = {
        'idMarkerSetTemplate' : MarkerSetTemplateId
    }
    r = createImageSet_RAW(token, MarkerSetTemplateId, payload)
    return verifyAndReturn(r)


def deleteMarkerTemplate(token, imageSetId):
    r = deleteImageSet_RAW(token, imageSetId)
    return verifyAndReturn(r)

def getListMarkerTemplate(token, wellId):
    r = getListImageSet_RAW(token, wellId)
    return verifyAndReturn(r)

#RAW:
def createMarkerTemplate_RAW(token, payload):
    url = ROOT_API + '/marker-set-template/marker-template/new'
    r = requests.post(url, json= payload , headers=tokenHeader(token), verify=False)
    return r.json()

def deleteMarkerTemplate_RAW(token, MarkerTemplateId):
    url = ROOT_API + '/marker-set-template/marker-template/delete'
    r = requests.post(url, json={'idMarkerTemplate': MarkerTemplateId}, headers=tokenHeader(token), verify=False)
    return r.json()

def getListMarkerTemplate_RAW(token, wellId):
    url = ROOT_API + '/marker-set-template/marker-template/list'
    r = requests.post(url, json={'idWell': wellId}, headers=tokenHeader(token), verify=False)
    return r.json()