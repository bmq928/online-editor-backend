"""This module serve api to work with project list

Include CRUD with project list

Contain RAW API with full information return from server and main API with less information.
"""

import requests
from ..api_url import ROOT_API
from ..common import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def getInfoProject(token, projectId):
    """Get info from a project
    
    Need token and projectId and return mini version info of project

    Args:
        token (str): token for account
        projectId (int): project id need to get info

    Returns:
        (bool, any): 
        a tuple
        if :bool: is false then :any: is a string write the error
        if :bool: is true then :any: is json that contain project info 

    """
    r = getInfoProject_RAW(token, projectId)
    return verifyAndReturn(r)


def getFullInfoProject(token, payload):
    """Get info from a project
    
    Need token and projectId and return full version info of project

    Args:
        token (str): token for account
        projectId (int): project id need to get info

    Returns:
        (bool, any): 
        a tuple. 
        if :bool: is false then :any: is a string write the error. 
        if :bool: is true then :any: is json that contain project info.

    """
    r = getFullInfoProject_RAW(token, payload)
    if r['code'] == 200:
        return r['content']
    return None
    

def listProject(token):
    """Get project list

    Need token, then return list of projects as array list

    Args:
        token (str): token

    Returns:
        object: 
        array of projects if success, None if false (token verify false)
    """
    r = listProject_RAW(token)
    if r['code'] == 200:
        return r['content']
    return None

def closeProject(token, projectId):
    r = closeProject_RAW(token, projectId)
    if r['code'] == 200 :
        return True, r['reason']
    return False, r['reason']

def createProject(token, **data):
    """Create project

    Create project, need token pass.

    Args:
        token (str): token
        **data : dict style
        Need name, company, department, description
        name is required, other is optional

    Returns:
        (bool, any):
        A tuple.
        If success, :bool: is false, :any: is object contain project info which created.
        If false, :bool: is false, :any: is string tell what error happened.

    Example:
         check, payload = createProject(token, name = 'Test create project', description = 'this field is optional')
             if check:
             print(payload)
         else:
             print("Fail. Error: " + payload)
    """
    payload = {
        'name': "",
        'company': "",
        'department': "",
        'description': ""
    }
    if 'name' in data:
        payload['name'] = data['name']
    else:
        return False, "Name field can't be empty"
    if 'company' in data:
        payload['company'] = data['company']
    if 'department' in data:
        payload['department'] = data['department']
    if 'description' in data:
        payload['description'] = data['description']
    r = createProject_RAW(token, payload)
    return verifyAndReturn(r)


def deleteProject(token, projectId):
    """Delete project from database

    Delete project which projectId specified.

    Args:
        token (str): token
        projectId (int): id of project
    
    Returns:
        (bool, any):
        A tuple.
        f success, :bool: is false, :any: is object contain project info which deleted.
        If false, :bool: is false, :any: is string tell what error happened.
    """
    r = deleteProject_RAW(token, projectId)
    return verifyAndReturn(r)


def editProject(token, projectId, **modifyData):
    """Edit project

    Edit project, need token pass, project id and modify content

    Args:
        token (str): token
        projectId (int) : dict style
        Need name, company, department, description, all is optional
        name can't be empty string
    

    Returns:
        (bool, any):
        A tuple.
        If success, :bool: is false, :any: is object contain project info which edited.
        If false, :bool: is false, :any: is string tell what error happened.

    Example:
        >>> check, payload = editProject(token, name = 'Test create project', description = 'this field is optional')
        >>> if check:
        >>>     print(payload) 
        >>> else:
        >>>     print("Fail. Error: " + payload)
    """
    payload = {
        'idProject': projectId
    }
    if 'name' in modifyData:
        if modifyData['name'] != '':
            payload['name'] = modifyData['name']
    if 'company' in modifyData:
        payload['company'] = modifyData['company']
    if 'department' in modifyData:
        payload['department'] = modifyData['department']
    if 'description' in modifyData:
        payload['description'] = modifyData['description']
    if 'alias' in modifyData:
        payload['alias'] = modifyData['description']
    r = editProject_RAW(token, payload)
    return verifyAndReturn(r)


#RAW API:

def getInfoProject_RAW(token, projectId):
    url = ROOT_API + '/project/info'
    r = requests.post(url, json = {'idProject': projectId}, headers = tokenHeader(token), verify=False)
    return r.json()

def getFullInfoProject_RAW(token, payload):
    url = ROOT_API + '/project/fullinfo'
    r = requests.post(url, json = payload, headers = tokenHeader(token), verify=False)
    return r.json()

def closeProject_RAW(token, projectId):
    url = ROOT_API + '/project/close'
    r = requests.post(url, json={'idProject': projectId}, headers = tokenHeader(token), verify=False)
    return r.json()
 
def editProject_RAW(token, payload):
    url = ROOT_API + '/project/edit'
    r = requests.post(url, json = payload, headers = tokenHeader(token), verify=False)
    return r.json()

def createProject_RAW(token, payload):
    url = ROOT_API + '/project/new'
    r = requests.post(url, json = payload, headers = tokenHeader(token), verify=False)
    r = r.json()
    return r

def listProject_RAW(token):
    url = ROOT_API + '/project/list'
    r = requests.post(url, headers = tokenHeader(token), verify=False)
    return r.json()

def deleteProject_RAW(token, projectId):
    url = ROOT_API + '/project/delete'
    payload = {
        "idProject": projectId
    }
    r = requests.delete(url, json = payload, headers = tokenHeader(token), verify=False)
    r = r.json()
    return r
