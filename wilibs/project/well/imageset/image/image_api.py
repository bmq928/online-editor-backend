from .....api_url import ROOT_API
from .....api_url import EXPORT_PATH
import os as os
from .....common import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def getImageInfo(token, imageId):
    r = getImageInfo_RAW(token, imageId)
    return verifyAndReturn(r)


def createImage(token, wellId, name):
    r = createImage_RAW(token, wellId, name)
    return verifyAndReturn(r)


def editImage(token, imageId, **data):
    data['idImage'] = imageId
    r = editImageInfo_RAW(token, data)
    return verifyAndReturn(r)


def deleteImage(token, imageId):
    r = deleteImage_RAW(token, imageId)
    return verifyAndReturn(r)


# RAW:

def createImage_RAW(token, wellId, name):
    url = genUrlWithWiId(ROOT_API + '/project/well/image-set/image/new', {'idWell': wellId, 'name': name}, token)
    r = requests.post(url, json={'idWell': wellId, 'name': name}, headers=tokenHeader(token), verify=False)
    return r.json()


def getImageInfo_RAW(token, imageId):
    url = genUrlWithWiId(ROOT_API + '/project/well/image-set/image/info', {'idImage': imageId}, token)
    r = requests.post(url, json={'idImage': imageId}, headers=tokenHeader(token), verify=False)
    return r.json()


def editImageInfo_RAW(token, payload):
    url = genUrlWithWiId(ROOT_API + '/project/well/image-set/image/edit', payload, token)
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()


def deleteImage_RAW(token, imageId):
    url = genUrlWithWiId(ROOT_API + '/project/well/image-set/image/delete', {'idImage': imageId}, token)
    r = requests.post(url, json={'idImage': imageId}, headers=tokenHeader(token), verify=False)
    return r.json()
