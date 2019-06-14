from .param_api import *
class Param:
    def __init__(self, token, paramInfo):
        self.token = token
        self.paramInfo = {
            'idProject': paramInfo['idProject'],
            'idParameterSet': paramInfo['idParameterSet'],
            'name': paramInfo['name'],
            'content' : paramInfo['content']
        }
        self.paramId = paramInfo['idParameterSet']
    def __repr__(self):
        obj = dict(self.paramInfo)
        return str(obj)
    
    def __str__(self):
        return self.__repr__()

    def getParamInfo(self):
        check, info = getParamInfo(self.token, self.paramId)
        if check:
            return info
        return None

    def editParam(self, **data):
      
        check, content = editParam(self.token, self.paramId, **data)
        if check:
            return None
        return content

    def deleteParam(self):
        check, content = deleteParam(self.token, self.paramId)
        if check:
            return None
        return content