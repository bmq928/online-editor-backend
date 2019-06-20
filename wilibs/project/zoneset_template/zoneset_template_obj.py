from .zoneset_template_api import *

class ZoneSetTemplate:
    def __init__(self, token, ZoneSetTemplateInfo):
        self.token = token
        self.ZoneSetTemplateInfo = {
            'idProject': ZoneSetTemplateInfo['idProject'],
            'idZoneSetTemplate': ZoneSetTemplateInfo['idZoneSetTemplate'],
            'name': ZoneSetTemplateInfo['name']
        }
        self.ZoneSetTemplateId = ZoneSetTemplateInfo['idZoneSetTemplate']
   
    def __repr__(self):
        obj = dict(self.ZoneSetTemplateInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()  
    
    def getZoneSetTemplateInfo(self):
        check, info = getZoneSetTeamplateInfo(self.token, self.ZoneSetTemplateId)
        if check:
            return info
        else:
            print(info)
        return {}

    def deleteZoneSetTemplate(self):
        check , content = deleteZoneSetTemplate(self.token, self.ZoneSetTemplateId)
        if check:
            return None
        return content
    
    def delete(self):
        return self.deleteZoneSetTemplate()
    
    def getInfo(self):
        return self.getZoneSetTemplateInfo()