"""
    This module help you interact with project/well (crud, edit)
"""
from ...api_url import ROOT_API
from ...api_url import EXPORT_PATH
import os as os
from ...common import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


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
    payload = data
    payload['idWell'] = wellId
    r = editWellInfo_RAW(token, payload)
    return verifyAndReturn(r)


def deleteWell(token, wellId):
    r = deleteWell_RAW(token, wellId)
    return verifyAndReturn(r)


# def createNewZoneSet(token, payload):
#     r = createZoneSet_RAW(token, payload)
#     return verifyAndReturn(r)


# def editZoneSetTemplate(token, payload):
#     r = editZoneSetTemplate_RAW(token, payload)
#     return verifyAndReturn(r)


# def editZoneTemplate(token, payload):
#     r = editZoneTemplate_RAW(token, payload)
#     return verifyAndReturn(r)


# def editZoneSet(token, payload):
#     r = editZoneSet_RAW(token, payload)
#     return verifyAndReturn(r)


# def deleteZoneSet(token, idZoneSet):
#     r = deleteZoneSet_RAW(token, idZoneSet)
#     return verifyAndReturn(r)


# def infoZoneSet(token, idZoneSet):
#     r = infoZoneSet_RAW(token, idZoneSet)
#     return verifyAndReturn(r)


# def listZoneSet(token, idWell):
#     r = listZoneSet_RAW(token, idWell)
#     return verifyAndReturn(r)


# def deleteZoneSetTemplate(token, idZoneSetTemplate):
#     r = deleteZoneSetTemplate_RAW(token, idZoneSetTemplate)
#     return verifyAndReturn(r)


# def createZoneSetTemplate(token, payload):
#     r = createZoneSetTemplate_RAW(token, payload)
#     return verifyAndReturn(r)


def exportCsvWDRV(token, payload):
    r = exportCsvRDRV_RAW(token, payload)
    return verifyAndReturn(r)


def exportCsvRV(token, payload):
    r = exportCsvRV_RAW(token, payload)
    return verifyAndReturn(r)


def downloadExportedFile(token, payload):
    r = downloadExportedFile_RAW(token, payload)
    path = os.path.join(EXPORT_PATH, payload['fileName'])
    open(path, 'wb').write(r.content)
    return payload['fileName']


def updateWellHeaders(token, payload):
    r = updateWellHeaders_RAW(token, payload)
    return verifyAndReturn(r)


# RAW:

def getWellFullInfo_RAW(token, wellId):
    url = ROOT_API + '/project/well/full-info'
    r = requests.post(url, json={'idWell': wellId}, headers=tokenHeader(token), verify=False)
    return r.json()


def createWell_RAW(token, payload):
    url = ROOT_API + '/project/well/new'
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()


def getWellInfo_RAW(token, wellId):
    url = ROOT_API + '/project/well/info'
    r = requests.post(url, json={'idWell': wellId}, headers=tokenHeader(token), verify=False)
    return r.json()


def listWell_RAW(token, payload):
    url = ROOT_API + '/project/well/list'
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()


def getWellHeaders_RAW(token, wellId):
    url = ROOT_API + '/project/well/get-well-header'
    r = requests.post(url, json={'idWell': wellId}, headers=tokenHeader(token), verify=False)
    return r.json()


def editWellInfo_RAW(token, payload):
    url = ROOT_API + '/project/well/edit'
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()


def deleteWell_RAW(token, wellId):
    url = ROOT_API + '/project/well/delete'
    r = requests.delete(url, json={'idWell': wellId}, headers=tokenHeader(token), verify=False)
    return r.json()


# def createZoneSet_RAW(token, payload):
#     url = ROOT_API + '/project/well/zone-set/new'
#     r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
#     return r.json()


# def editZoneSetTemplate_RAW(token, payload):
#     url = ROOT_API + '/zone-set-template/edit'
#     r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
#     return r.json()


# def editZoneTemplate_RAW(token, payload):
#     url = ROOT_API + '/zone-set-template/zone-template/edit'
#     r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
#     return r.json()


# def editZoneSet_RAW(token, payload):
#     url = ROOT_API + '/project/well/zone-set/edit'
#     r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
#     return r.json()


# def listZoneSet_RAW(token, wellId):
#     url = ROOT_API + '/project/well/zone-set/list'
#     r = requests.post(url, json={'idWell': wellId}, headers=tokenHeader(token), verify=False)
#     return r.json()


<<<<<<< HEAD
# def deleteZoneSet_RAW(token, idZoneSet):
#     url = ROOT_API + '/dustbin/delete'
#     r = requests.post(url, json={'idObject': idZoneSet, 'type': 'zoneset'}, headers=tokenHeader(token), verify=False)
#     return r.json()
=======
def deleteZoneSet_RAW(token, idZoneSet):
    url = ROOT_API + '/dustbin/delete'
    r = requests.delete(url, json={'idObject': idZoneSet, 'type': 'zoneset'}, headers=tokenHeader(token), verify=False)
    return r.json()
>>>>>>> 704f063a1ec4c17ee29334824af90c8ff4a6b93a


# def infoZoneSet_RAW(token, idZoneSet):
#     url = ROOT_API + '/project/well/zone-set/info'
#     r = requests.post(url, json={'idZoneSet': idZoneSet}, headers=tokenHeader(token), verify=False)
#     return r.json()


# def createZoneSetTemplate_RAW(token, payload):
#     url = ROOT_API + '/zone-set-template/new'
#     r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
#     return r.json()


# def deleteZoneSetTemplate_RAW(token, idZoneSetTemplate):
#     url = ROOT_API + '/zone-set-template/delete'
#     r = requests.delete(url, json={'idZoneSetTemplate': idZoneSetTemplate}, headers=tokenHeader(token), verify=False)
#     return r.json()


def exportCsvRDRV_RAW(token, payload):
    url = ROOT_API + '/export/CSV/wdrv'
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()


def exportCsvRV_RAW(token, payload):
    url = ROOT_API + '/export/CSV/rv'
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()


def downloadExportedFile_RAW(token, payload):
    url = ROOT_API + '/export/files'
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r


def updateWellHeaders_RAW(token, payload):
    url = ROOT_API + '/project/well/bulk-update-well-header'
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()
