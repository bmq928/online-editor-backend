"""
    This module help you interact with project/well (crud, edit)
"""
from ...api_url import ROOT_API
from ...common import *
import requests


def getWellInfo(token, wellId):
    r = getWellInfo_RAW(token, wellId)
    return verifyAndReturn(r)


def getWellFullInfo(token, wellId):
    r = getWellFullInfo_RAW(token, wellId)
    return verifyAndReturn(r)


def listWell(token, projectId, **data):
    """Get well list from projectId


    Returns:
        None if get error
        Well list as obj contain info (array)
    
    """

    payload = {
        'idProject': projectId
    }
    if 'start' in data:
        payload['start'] = data['start']
    if 'limit' in data:
        payload['limit'] = data['limit']
    if 'forward' in data:
        payload['forward'] = data['forward']
    if 'match' in data:
        payload['match'] = data['match']
    r = listWell_RAW(token, payload)
    if 'content' in r:
        return r['content']
    return None


def createWell(token, projectId, **data):
    """Create well with projectId, created by username
    """
    payload = {
        'idProject': projectId
    }
    if 'name' in data:
        payload['name'] = data['name']
    else:
        return False, "Name field can't be null"
    if 'topDepth' in data:
        payload['topDepth'] = data['topDepth']
    if 'bottomDepth' in data:
        payload['bottomDepth'] = data['bottomDepth']
    if 'step' in data:
        payload['step'] = data['step']
    if 'unit' in data:
        payload['unit'] = data['unit']
    if 'color' in data:
        payload['color'] = data['color']
    if 'idWell' in data:
        payload['idWell'] = data['idWell']
    r = createWell_RAW(token, payload)
    return verifyAndReturn(r)


def getWellHeaders(token, wellId):
    r = getWellHeaders(token, wellId)
    return verifyAndReturn(r)


def editWellInfo(token, wellId, **data):
    payload = {
        'idWell': wellId
    }
    if 'name' in data:
        payload['name'] = data['name']
    if 'topDepth' in data:
        payload['topDepth'] = data['topDepth']
    if 'bottomDepth' in data:
        payload['bottomDepth'] = data['bottomDepth']
    if 'step' in data:
        payload['step'] = data['step']
    r = editWellInfo_RAW(token, payload)
    return verifyAndReturn(r)


def deleteWell(token, wellId):
    r = deleteWell_RAW(token, wellId)
    return verifyAndReturn(r)


def createNewZoneSet(token, payload):
    r = createZoneSet_RAW(token, payload)
    return verifyAndReturn(r)


def editZoneSetTemplate(token, payload):
    r = editZoneSetTemplate_RAW(token, payload)
    return verifyAndReturn(r)


def editZoneTemplate(token, payload):
    r = editZoneTemplate_RAW(token, payload)
    return verifyAndReturn(r)


def editZoneSet(token, payload):
    r = editZoneSet_RAW(token, payload)
    return verifyAndReturn(r)


def deleteZoneSet(token, idZoneSet):
    r = deleteZoneSet_RAW(token, idZoneSet)
    return verifyAndReturn(r)


def infoZoneSet(token, idZoneSet):
    r = infoZoneSet_RAW(token, idZoneSet)
    return verifyAndReturn(r)


def listZoneSet(token, idWell):
    r = listZoneSet_RAW(token, idWell)
    return verifyAndReturn(r)


def deleteZoneSetTemplate(token, idZoneSetTemplate):
    r = deleteZoneSetTemplate_RAW(token, idZoneSetTemplate)
    return verifyAndReturn(r)


def createZoneSetTemplate(token, payload):
    r = createZoneSetTemplate_RAW(token, payload)
    return verifyAndReturn(r)


# RAW:

def getWellFullInfo_RAW(token, wellId):
    url = ROOT_API + '/project/well/full-info'
    r = requests.post(url, json={'idWell': wellId}, headers=tokenHeader(token))
    return r.json()


def createWell_RAW(token, payload):
    url = ROOT_API + '/project/well/new'
    r = requests.post(url, json=payload, headers=tokenHeader(token))
    return r.json()


def getWellInfo_RAW(token, wellId):
    url = ROOT_API + '/project/well/info'
    r = requests.post(url, json={'idWell': wellId}, headers=tokenHeader(token))
    return r.json()


def listWell_RAW(token, payload):
    url = ROOT_API + '/project/well/list'
    r = requests.post(url, json=payload, headers=tokenHeader(token))
    return r.json()


def getWellHeaders_RAW(token, wellId):
    url = ROOT_API + '/project/well/get-well-header'
    r = requests.post(url, json={'idWell': wellId}, headers=tokenHeader(token))
    return r.json()


def editWellInfo_RAW(token, payload):
    url = ROOT_API + '/project/well/edit'
    r = requests.post(url, json=payload, headers=tokenHeader(token))
    return r.json()


def deleteWell_RAW(token, wellId):
    url = ROOT_API + '/project/well/delete'
    r = requests.post(url, json={'idWell': wellId}, headers=tokenHeader(token))
    return r.json()


def createZoneSet_RAW(token, payload):
    url = ROOT_API + '/project/well/zone-set/new'
    r = requests.post(url, json=payload, headers=tokenHeader(token))
    return r.json()


def editZoneSetTemplate_RAW(token, payload):
    url = ROOT_API + '/zone-set-template/edit'
    r = requests.post(url, json=payload, headers=tokenHeader(token))
    return r.json()


def editZoneTemplate_RAW(token, payload):
    url = ROOT_API + '/zone-set-template/zone-template/edit'
    r = requests.post(url, json=payload, headers=tokenHeader(token))
    return r.json()


def editZoneSet_RAW(token, payload):
    url = ROOT_API + '/project/well/zone-set/edit'
    r = requests.post(url, json=payload, headers=tokenHeader(token))
    return r.json()


def listZoneSet_RAW(token, wellId):
    url = ROOT_API + '/project/well/zone-set/list'
    r = requests.post(url, json={'idWell': wellId}, headers=tokenHeader(token))
    return r.json()


def deleteZoneSet_RAW(token, idZoneSet):
    url = ROOT_API + '/dustbin/delete'
    r = requests.post(url, json={'idObject': idZoneSet, 'type': 'zoneset'}, headers=tokenHeader(token))
    return r.json()


def infoZoneSet_RAW(token, idZoneSet):
    url = ROOT_API + '/project/well/zone-set/info'
    r = requests.post(url, json={'idZoneSet': idZoneSet}, headers=tokenHeader(token))
    return r.json()


def createZoneSetTemplate_RAW(token, payload):
    url = ROOT_API + '/zone-set-template/new'
    r = requests.post(url, json=payload, headers=tokenHeader(token))
    return r.json()


def deleteZoneSetTemplate_RAW(token, idZoneSetTemplate):
    url = ROOT_API + '/zone-set-template/delete'
    r = requests.delete(url, json={'idZoneSetTemplate': idZoneSetTemplate}, headers=tokenHeader(token))
    return r.json()
