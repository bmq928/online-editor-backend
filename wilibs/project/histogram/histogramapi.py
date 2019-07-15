import requests
from ...api_url import ROOT_API
from ...common import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def getHistogramList(token, projectId):
    r = getHistogramList_RAW(token, projectId)
    return verifyAndReturn(r)

def getHistogramInfo(token, histogramId):
    r = getHistogramInfo_RAW(token, histogramId)
    return verifyAndReturn(r)

def createHistogram(token, projectId, **kwargs):
    kwargs['idProject'] = projectId 
    r = createHistogram_RAW(token, kwargs)
    return verifyAndReturn(r)

def editHistogram(token, histogramId, **kwargs):
    kwargs['idHistogram'] = histogramId
    r = editHistogram_RAW(token, kwargs)
    return verifyAndReturn(r)

def deleteHistogram(token, histogramId):
    r =  deleteHistogram_RAW(token, histogramId)
    return verifyAndReturn(r)

#RAW:
def getHistogramList_RAW(token, projectId):
    url = genUrlWithWiId(ROOT_API + '/project/histogram/list', {"idProject": projectId}, token)
    r = requests.post(url, json={'idProject': projectId}, headers=tokenHeader(token), verify=False)
    return r.json()
    
def getHistogramInfo_RAW(token, histogramId):
    url = genUrlWithWiId(ROOT_API + '/project/histogram/info', {"idHistogram": histogramId}, token)
    r = requests.post(url, json={'idHistogram': histogramId}, headers=tokenHeader(token), verify=False)
    return r.json()

def createHistogram_RAW(token, payload):
    url = genUrlWithWiId(ROOT_API + '/project/histogram/new', payload, token)
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()

def editHistogram_RAW(token, payload):
    url = genUrlWithWiId(ROOT_API + '/project/histogram/edit', payload, token)
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()

def deleteHistogram_RAW(token, histogramId):
    url = genUrlWithWiId(ROOT_API + '/project/histogram/delete', {"idHistogram": histogramId}, token)
    r = requests.delete(url, json={'idHistogram': histogramId}, headers=tokenHeader(token), verify=False)
    return r.json()