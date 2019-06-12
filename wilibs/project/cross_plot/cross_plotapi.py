import requests
from ...api_url import ROOT_API
from ...common import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def getCrossPlotList(token, projectId):
    r = getCrossPlotList_RAW(token, projectId)
    return verifyAndReturn(r)

def getCrossPlotInfo(token, crossPlotId):
    r = getCrossPlotInfo_RAW(token, crossPlotId)
    return verifyAndReturn(r)

def createCrossPlot(token, projectId, **kwargs):
    kwargs['idPrject'] = projectId 
    r = createCrossPlot_RAW(token, kwargs)
    return verifyAndReturn(r)

def editCrossPlot(token, crossPlotId, **kwargs):
    kwargs['idCrossPlot'] = crossPlotId
    r = editCrossPlot_RAW(token, kwargs)
    return verifyAndReturn(r)

def deleteCrossPlot(token, crossPlotId):
    r =  deleteCrossPlot_RAW(token, crossPlotId)
    return verifyAndReturn(r)



#RAW:

def getCrossPlotList_RAW(token, projectId):
    url = ROOT_API + '/project/cross-plot/list'
    r = requests.post(url, json={'idProject': projectId}, headers=tokenHeader(token), verify=False)
    return r.json()
    
def getCrossPlotInfo_RAW(token, crossPlotId):
    url = ROOT_API + '/project/cross-plot/info'
    r = requests.post(url, json={'idCrossPlot': crossPlotId}, headers=tokenHeader(token), verify=False)
    return r.json()

def createCrossPlot_RAW(token, payload):
    url = ROOT_API + '/project/cross-plot/new'
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()

def editCrossPlot_RAW(token, payload):
    url = ROOT_API + '/project/cross-plot/edit'
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()

def deleteCrossPlot_RAW(token, crossPlotId):
    url = ROOT_API + '/project/cross-plot/delete'
    r = requests.post(url, json={'idCrossPlot': crossPlotId}, headers=tokenHeader(token), verify=False)
    return r.json()