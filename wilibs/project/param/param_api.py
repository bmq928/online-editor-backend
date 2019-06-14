import requests
from ...api_url import ROOT_API
from ...common import *

def createParam(token, projectId, **data):
    payload = {
        'idProject' : projectId
    }
    if 'name' in data:
        payload['name'] = data['name']
    if 'content' in data:
        payload['content'] = data['content']
    if 'type' in data:
        payload['type'] = data['type']
    r = createParam_RAW(token, payload)
    return verifyAndReturn(r)

def getParamInfo(token, paramId):
    r = getParamInfo_RAW(token, paramId)
    return verifyAndReturn(r)

def listParam(token, projectId):
    payload = {
        'idProject' : projectId
    }
    r = listParam_RAW(token, payload)
    if 'content' in r:
        return r['content']
    return verifyAndReturn(r)

def editParam(token, paramId, **data):
    payload = {
        'idParameterSet': paramId    
    }
    if 'name' in data:
        payload['name'] = data['name']
    if 'content' in data:
        payload['content'] = data['content']
    if 'type' in data:
        payload['type'] = data['type']
    r = editParam_RAW(token, payload)
    return verifyAndReturn(r)
    
def deleteParam(token, paramId):
    r = deleteParam_RAW(token, paramId)
    return verifyAndReturn(r)

#RAW 
def createParam_RAW(token, payload):
    url = ROOT_API + '/project/parameter-set/new'
    r = requests.post(url, json = payload, headers = tokenHeader(token))
    return r.json()

def getParamInfo_RAW(token, paramId):
    url = ROOT_API + '/project/parameter-set/info'
    r = requests.post(url, json= {'idParameterSet' : paramId}, headers= tokenHeader(token))
    return r.json()

def listParam_RAW(token, payload):
    url = ROOT_API + '/project/parameter-set/list'
    r = requests.post(url, json= payload, headers= tokenHeader(token))
    return r.json()

def editParam_RAW(token,payload):
    url = ROOT_API + '/project/parameter-set/edit'
    r = requests.post(url, json = payload, headers = tokenHeader(token))
    return r.json()

def deleteParam_RAW(token, paramId):
    url = ROOT_API + '/project/parameter-set/delete'
    r = requests.post(url, json={'idParameterSet' : paramId}, headers = tokenHeader(token))
    r = r.json()
    return r