from .....api_url import ROOT_API
from .....common import *
import requests


def getCurveInfo(token, curveId):
    r = getCurveInfo_RAW(token, curveId)
    return verifyAndReturn(r)

def getCurveData(token, curveId):
    r = getCurveData_RAW(token, curveId)
    return verifyAndReturn(r)

def updateCurveData(token, datasetId, desCurveId, data, name):
    payload = {
        'idDataset': datasetId,
        'idDesCurve': desCurveId,
    }
    if name:
        payload['curveName'] = name
    data = {'data': data}
    r = updateCurveData_RAW(token, payload, data)
    return verifyAndReturn(r)

def editCurveInfo(token, username, curveId, **data):
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
    payload['updatedBy'] = username
    r = editCurveInfo_RAW(token, payload)
    return verifyAndReturn(r)

def deleteCurve(token, curveId):
    r = deleteCurve_RAW(token, {'idCurve' : curveId})
    return verifyAndReturn(r)

def createCurve(token, datasetId, **data ) :
    payload = {
        "idDataset": datasetId
    }
    if 'name' in data:
        payload['name'] = data['name']
    else:
        return False, "Name field can't be empty"
    if 'duplicate' in data:
        payload['duplicate'] = data['duplicate']
    if 'unit' in data:
        payload['unit'] = data['unit']
    if 'initValue' in data:
        payload['initValue'] = data['initValue']
    r = createCurve_RAW(token, payload)
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
    return r.json()

def editCurveInfo_RAW(token, payload):
    url = ROOT_API + '/project/well/dataset/curve/edit'
    r = requests.post(url, json = payload, headers = tokenHeader(token))
    return r.json()

def deleteCurve_RAW(token, payload):
    url = ROOT_API + '/project/well/dataset/curve/delete'
    r = requests.delete(url, json = payload, header = tokenHeader(token))
    return r.json()
    
def createCurve_RAW(token, payload):
    url = ROOT_API + '/project/well/dataset/curve/new'
    r = requests.post(url, json = payload, header = tokenHeader(token))
    return r.json()