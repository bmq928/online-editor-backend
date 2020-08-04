import requests
from ...api_url import ROOT_API
from ...common import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def getListPlot(token, idProject):
    r = getListPlot_RAW(token, {'idProject': idProject})
    return verifyAndReturn(r)


def editPlot(token, idPlot, **data):
    payload = {
        'idPlot': idPlot
    }
    if 'name' in data:
        payload['name'] = data['name']
    if 'relatedTo' in data:
        payload['relatedTo'] = data['relatedTo']
    if 'option' in data:
        payload['option'] = data['option']
    if 'currentState' in data:
        payload['currentState'] = data['currentState']
    if 'cropDisplay' in data:
        payload['cropDisplay'] = data['cropDisplay']
    if 'printSetting' in data:
        payload['printSetting'] = data['printSetting']
    if 'unit' in data:
        payload['unit'] = data['unit']
    if 'depthRefSpec' in data:
        payload['depthRefSpec'] = data['depthRefSpec']
    if 'notShowPatterns' in data:
        payload['notShowPatterns'] = data['notShowPatterns']
    if 'tickMode' in data:
        payload['tickMode'] = data['tickMode']
    if 'majorTickLength' in data:
        payload['majorTickLength'] = data['majorTickLength']
    if 'minorTickNum' in data:
        payload['minorTickNum'] = data['minorTickNum']
    if 'note' in data:
        payload['note'] = data['note']
    r = editPlot_RAW(token, payload)
    return verifyAndReturn(r)


def deletePlot(token, idPlot):
    r = deletePlot_RAW(token, {'idPlot': idPlot})
    return verifyAndReturn(r)


def createNewPlot(token, idProject, **data):
    payload = {
        'name': data['name'],
        'idProject': idProject,
        'plotTemplate': None,
        'option': 'blank-plot'
    }
    r = createNewPlot_RAW(token, payload)
    return verifyAndReturn(r)


def infoPlot(token, idPlot):
    r = infoPlot_Raw(token, {'idPlot': idPlot})
    return verifyAndReturn(r)


# RAW

def getListPlot_RAW(token, payload):
    url = genUrlWithWiId(ROOT_API + '/project/plot/list', payload, token)
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()


def infoPlot_Raw(token, payload):
    url = genUrlWithWiId(ROOT_API + '/project/plot/info', payload, token)
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()


def createNewPlot_RAW(token, payload):
    url = genUrlWithWiId(ROOT_API + '/project/plot/new', payload, token)
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()


def editPlot_RAW(token, payload):
    url = genUrlWithWiId(ROOT_API + '/project/plot/edit', payload, token)
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()


def deletePlot_RAW(token, payload):
    url = genUrlWithWiId(ROOT_API + '/project/plot/delete', payload, token)
    r = requests.delete(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()
