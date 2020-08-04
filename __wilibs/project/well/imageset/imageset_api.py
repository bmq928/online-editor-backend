from ....api_url import ROOT_API
from ....api_url import EXPORT_PATH
import os as os
from ....common import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def getImageSetInfo(token, imageSetId):
    r = getImageSetInfo_RAW(token, imageSetId)
    return verifyAndReturn(r)


def createImageSet(token, wellId, name):
    r = createImageSet_RAW(token, wellId, name)
    return verifyAndReturn(r)


def editImageSet(token, imageSetId, **data):
    data['idImageSet'] = imageSetId
    r = editImageSetInfo_RAW(token, data)
    return verifyAndReturn(r)


def deleteImageSet(token, imageSetId):
    r = deleteImageSet_RAW(token, imageSetId)
    return verifyAndReturn(r)


def getListImageSet(token, wellId):
    r = getListImageSet_RAW(token, wellId)
    return verifyAndReturn(r)


# RAW:
def createImageSet_RAW(token, wellId, name):
    url = genUrlWithWiId(ROOT_API + '/project/well/image-set/new', {'idWell': wellId, 'name': name}, token)
    r = requests.post(url, json={'idWell': wellId, 'name': name}, headers=tokenHeader(token), verify=False)
    return r.json()


def getImageSetInfo_RAW(token, imageSetId):
    url = genUrlWithWiId(ROOT_API + '/project/well/image-set/info', {'idImageSet': imageSetId}, token)
    r = requests.post(url, json={'idImageSet': imageSetId}, headers=tokenHeader(token), verify=False)
    return r.json()


def editImageSetInfo_RAW(token, payload):
    url = genUrlWithWiId(ROOT_API + '/project/well/image-set/edit', payload, token)
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()


def deleteImageSet_RAW(token, imageSetId):
    url = genUrlWithWiId(ROOT_API + '/project/well/image-set/delete', {'idImageSet': imageSetId}, token)
    r = requests.post(url, json={'idImageSet': imageSetId}, headers=tokenHeader(token), verify=False)
    return r.json()


def getListImageSet_RAW(token, wellId):
    url = genUrlWithWiId(ROOT_API + '/project/well/image-set/list', {'idWell': wellId}, token)
    r = requests.post(url, json={'idWell': wellId}, headers=tokenHeader(token), verify=False)
    return r.json()
