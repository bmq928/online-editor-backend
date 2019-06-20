from .zone_template_api import *
from ..zoneset_template_obj import getZoneSetTeamplateInfo

class ZoneTemplate:
    def __init__(self, token, ZoneTemplateInfo):
        self.token = token
        self.ZoneTemplateInfo = {
            'idZoneTemplate': ZoneTemplateInfo['idZoneTemplate'],
            'idZoneSetTemplate': ZoneTemplateInfo['idZoneSetTemplate'],
            'name': ZoneTemplateInfo['name']
        }
        self.ZoneTemplateId = ZoneTemplateInfo['idZoneTemplate']
        self.ZoneSetTeamplateId = ZoneTemplateInfo['idZoneSetTemplate']
        self.name = ZoneTemplateInfo['name']
   
    def __repr__(self):
        obj = dict(self.ZoneTemplateInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()  
    def getZoneTemplateInfo(self):
        check, content = getZoneSetTeamplateInfo(self.token, self.ZoneSetTeamplateId)
        if check:
            tmpObj = content['zone_templates']
            for i in tmpObj:
                if self.ZoneTemplateId == i['idZoneTemplate']:
                    return(ZoneTemplate(self.token, i))
        return None
    
    def getInfo(self):
        return self.getZoneTemplateInfo()
    
    def deleteZoneTemplate(self):
        check , content = deleteZoneTemplate(self.token, self.ZoneTemplateId)
        if check:
            return True
        print(content)
        return False
    
    def delete(self):
        return self.deleteZoneTemplate()

    
    
