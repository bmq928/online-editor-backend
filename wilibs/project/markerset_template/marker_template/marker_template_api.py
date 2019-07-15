from wilibs.api_url import *
import os as os
import requests
from wilibs.common import *


# from requests.packages.urllib3.exceptions import InsecureRequestWarning
#
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def createMarkerTemplate(token, MarkerSetTemplateId, name):
    r = createMarkerTemplate_RAW(token, MarkerSetTemplateId, name)
    return verifyAndReturn(r)


def deleteMarkerTemplate(token, MarkerTemplateId):
    r = deleteMarkerTemplate_RAW(token, MarkerTemplateId)
    return verifyAndReturn(r)


def getMarkerTemplateInfo(token, MarkerTemplateId):
    r = getMarkerTemplateInfo_RAW(token, MarkerTemplateId)
    return verifyAndReturn(r)


# RAW:
def createMarkerTemplate_RAW(token, MarkerSetTemplateId, name):
    url = genUrlWithWiId(ROOT_API + '/marker-set-template/marker-template/new',
                         {'idMarkerSetTemplate': MarkerSetTemplateId, 'name': name}, token)
    r = requests.post(url, json={'idMarkerSetTemplate': MarkerSetTemplateId, 'name': name}, headers=tokenHeader(token),
                      verify=False)
    return r.json()


def deleteMarkerTemplate_RAW(token, MarkerTemplateId):
    url = genUrlWithWiId(ROOT_API + '/marker-set-template/marker-template/delete',
                         {'idMarkerTemplate': MarkerTemplateId}, token)
    r = requests.delete(url, json={'idMarkerTemplate': MarkerTemplateId}, headers=tokenHeader(token), verify=False)
    return r.json()


def getMarkerTemplateInfo_RAW(token, MarkerTemplateId):
    url = genUrlWithWiId(ROOT_API + '/marker-set-template/marker-template/info', {'idMarkerTemplate': MarkerTemplateId},
                         token)
    r = requests.post(url, json={'idMarkerTemplate': MarkerTemplateId}, headers=tokenHeader(token), verify=False)
    return r.json()
