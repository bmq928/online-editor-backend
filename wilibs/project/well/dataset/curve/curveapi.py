from .....api_url import ROOT_API
from .....common import *
import requests


def getCurveInfo(token, curveId):
    r = getCurveInfo_RAW(token, curveId)
    return verifyAndReturn(r)

def getCurveData(token, curveId):
    r = getCurveData_RAW(token, curveId)
    return verifyAndReturn(r)

def createCurve(token, datasetId, name, data, **kwargsData):
    payload = {
        'curveName': name,
        'idDataset': datasetId
    }
    if 'unit' in kwargsData:
        payload['unit'] = kwargsData['unit']
    if 'idFamily' in kwargsData:
        payload['idFamily'] = kwargsData['idFamily']
    if 'type' in kwargsData:
        payload['type'] = kwargsData['type']
    data = {'data': data}
    r = updateCurveData_RAW(token, payload, data)
    return verifyAndReturn(r)

def updateCurveData(token, datasetId, desCurveId, data, name):
    payload = {
        'idDataset': datasetId,
        'idDesCurve': desCurveId,
        'curveIndex': desCurveId
    }
    if name:
        payload['curveName'] = name
    data = {'data': data}
    r = updateCurveData_RAW(token, payload, data)
    return verifyAndReturn(r)

def editCurveInfo(token, curveId, **data):
    payload = {
        'idCurve': curveId
    }
    if 'name' in data:
        payload['name'] = data['name']
    if 'duplicate' in data:
        payload['duplicate'] = data['duplicate']
    if 'unit' in data:
        payload['unit'] = data['unit']
    if 'initValue' in data:
        payload['initValue'] = data['initValue']
    r = editCurveInfo_RAW(token, payload)
    return verifyAndReturn(r)

def checkIfCurveExisted(token, datasetId, name):
    r = checkIfCurveExisted_RAW(token, datasetId, name)
    if r['reason'] == 'No curve found by name':
        return False, 'nothing'
    if r['reason'] == 'Found curve':
        return True, r['content']
    return False, r['reason']

def deleteCurve(token, curveId):
    r = deleteCurve_RAW(token, curveId)
    return verifyAndReturn(r)

#RAW:

def getCurveInfo_RAW(token, curveId):
    url = ROOT_API + '/project/well/dataset/curve/info'
    r = requests.post(url, json = {'idCurve': curveId}, headers = tokenHeader(token))
    return r.json()

def getCurveData_RAW(token, curveId):
    url = ROOT_API + '/project/well/dataset/curve/getData'
    r = requests.post(url, json = {'idCurve': curveId}, headers = tokenHeader(token))
    return r.json()

def updateCurveData_RAW(token, payload, data):
    url = ROOT_API + '/project/well/dataset/curve/processing'
    r = requests.post(url, data = payload, files = data, headers = tokenHeader(token))
    try:
        r = r.json()
    except:
        r = {'code': 501, 'reason': 'Format wrong'}
    return r

def editCurveInfo_RAW(token, payload):
    url = ROOT_API + '/project/well/dataset/curve/edit'
    r = requests.post(url, json = payload, headers = tokenHeader(token))
    return r.json()

def deleteCurve_RAW(token, payload):
    url = ROOT_API + '/project/well/dataset/curve/delete'
    r = requests.delete(url, json = payload, headers = tokenHeader(token))
    return r.json()
    
def checkIfCurveExisted_RAW(token, datasetId, name):
    url = ROOT_API + '/project/well/dataset/curve/is-existed'
    r = requests.post(url, json = {'idDataset': datasetId, 'name': name}, headers = tokenHeader(token))
    return r.json()
