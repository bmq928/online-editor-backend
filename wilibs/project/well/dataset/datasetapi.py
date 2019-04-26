from ....api_url import ROOT_API
from ....common import *
import requests


def getDatasetInfo(token, datasetId):
    r = getDatasetInfo_RAW(token, datasetId)
    return verifyAndReturn(r)

def editDatasetInfo(token, datasetId, **data):
    payload = {
        'idDateset': datasetId
    }
    if 'idWell' in data:
        payload['idWell'] = data['idWell']
    if 'name' in data:
        payload['name'] = data['name']
    if 'datasetKey' in data:
        payload['datasetKey'] = data['datasetKey']
    if 'datasetLabel' in data:
        payload['datasetLabel'] = data['datasetLabel']
    r = editDatasetInfo_RAW(token, payload)
    return verifyAndReturn(r)


#RAW:

def getDatasetInfo_RAW(token, datasetId):
    url = ROOT_API + '/project/well/dataset/info'
    r = requests.post(url, json = {'idDataset': datasetId}, headers = tokenHeader(token))
    return r.json()

def editDatasetInfo_RAW(token, payload):
    url = ROOT_API + '/project/well/dataset/edit'
    r = requests.post(url, json = payload, headers = tokenHeader(token))
    return r.json()
