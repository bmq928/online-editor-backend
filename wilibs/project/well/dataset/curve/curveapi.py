from .....api_url import ROOT_API
from .....common import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# format convert tool
def arrayTypeConverter(data):
    result = []
    for i in data:
        line = ''
        line += str(i['y'])
        for j in i['x']:
            if j != None:
                line += ' ' + str(j)
            else:
                line += ' ' + 'null'
        result.append(line)
    return result


def numberTypeConverter(data):
    result = []
    for i in data:
        line = ''
        line += str(i['y'])
        if i['x'] != None:
            line += ' ' + str(i['x'])
        else:
            line += ' ' + 'null'
        result.append(line)
    return result


def textTypeConverter(data):
    result = []
    for i in data:
        line = ''
        line += str(i['y'])
        line += ' "' + str(i['x']) + '"'
        result.append(line)
    return result


# api

def getCurveInfo(token, curveId):
    r = getCurveInfo_RAW(token, curveId)
    return verifyAndReturn(r)


def getCurveData(token, curveId):
    r = getCurveData_RAW(token, curveId)
    return verifyAndReturn(r)


# def createCurve(token, datasetId, name, data, **kwargsData):
#     payload = {
#         'curveName': name,
#         'idDataset': datasetId
#     }
#     if 'unit' in kwargsData:
#         payload['unit'] = kwargsData['unit']
#     if 'idFamily' in kwargsData:
#         payload['idFamily'] = kwargsData['idFamily']
#     if 'type' in kwargsData:
#         payload['type'] = kwargsData['type']
#     if 'description' in kwargsData:
#         payload['description'] = kwargsData['description']
#     if 'initValue' in kwargsData:
#         payload['initValue'] = kwargsData['initValue']
#     data = {'data': data}
#     r = updateCurveData_RAW(token, payload, data)
#     return verifyAndReturn(r)


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


def createCurve(token, datasetId, file, **data):
    payload = data
    payload['curveName'] = data['name']
    payload['idDataset'] = datasetId
    r = createCurveData_RAW(token, payload, file)
    return verifyAndReturn(r)


def updateRawCurveData(token, curveId, data):
    payload = {
        'idCurve': curveId
    }
    r = createCurveData_RAW(token, payload, data)
    return verifyAndReturn(r)


def editCurveInfo(token, curve, **data):
    payload = {
        'idCurve': curve.curveId,
        'name': curve.curveName
    }
    if 'name' in data:
        payload['name'] = data['name']
    if 'duplicate' in data:
        payload['duplicate'] = data['duplicate']
    if 'unit' in data:
        payload['unit'] = data['unit']
    if 'type' in data:
        payload['type'] = data['type']
    if 'dimension' in data:
        payload['dimension'] = data['dimension']
    if 'columnsTitle' in data:
        payload['columnsTitle'] = data['columnsTitle']
    if 'idDataset' in data:
        payload['idDataset'] = data['idDataset']
    if 'idFamily' in data:
        payload['idFamily'] = data['idFamily']
    if 'relatedTo' in data:
        payload['relatedTo'] = data['relatedTo']
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
    r = deleteCurve_RAW(token, {'idCurve': curveId})
    return verifyAndReturn(r)


def getRawCurveData(token, curveId, columnIndex):
    r = getRawCurveData_RAW(token, curveId, columnIndex)
    return verifyAndReturn(r)


# RAW:

def getCurveInfo_RAW(token, curveId):
    url = genUrlWithWiId(ROOT_API + '/project/well/dataset/curve/info', {'idCurve': curveId}, token)
    r = requests.post(url, json={'idCurve': curveId}, headers=tokenHeader(token), verify=False)
    return r.json()


def getCurveData_RAW(token, curveId):
    url = genUrlWithWiId(ROOT_API + '/project/well/dataset/curve/getData', {'idCurve': curveId}, token)
    r = requests.post(url, json={'idCurve': curveId}, headers=tokenHeader(token), verify=False)
    return r.json()


def createCurveData_RAW(token, payload, data):
    url = ROOT_API + '/project/well/dataset/curve/new-raw-curve'
    print(payload)
    r = requests.post(url, data=payload, files={'data': data}, headers=tokenHeader(token), verify=False)
    try:
        r = r.json()
    except:
        r = {'code': 501, 'reason': 'Format wrong'}
    return r


def updateCurveData_RAW(token, payload, data):
    url = ROOT_API + '/project/well/dataset/curve/processing'
    r = requests.post(url, data=payload, files=data, headers=tokenHeader(token, "multipart/form-data"), verify=False)
    try:
        r = r.json()
    except:
        r = {'code': 501, 'reason': 'Format wrong'}
    return r


def editCurveInfo_RAW(token, payload):
    url = genUrlWithWiId(ROOT_API + '/project/well/dataset/curve/edit', payload, token)
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()


def deleteCurve_RAW(token, payload):
    url = genUrlWithWiId(ROOT_API + '/project/well/dataset/curve/delete', payload, token)
    r = requests.delete(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()


def checkIfCurveExisted_RAW(token, datasetId, name):
    url = genUrlWithWiId(ROOT_API + '/project/well/dataset/curve/is-existed', {'idDataset': datasetId, 'name': name},
                         token)
    r = requests.post(url, json={'idDataset': datasetId, 'name': name}, headers=tokenHeader(token), verify=False)
    return r.json()


def getRawCurveData_RAW(token, curveId, columnIndex):
    url = genUrlWithWiId(ROOT_API + '/project/well/dataset/curve/getRawData',
                         {'idCurve': curveId, 'columnIndex': columnIndex}, token)
    r = requests.post(url, json={'idCurve': curveId, 'columnIndex': columnIndex}, headers=tokenHeader(token),
                      verify=False)
    return r.json()
