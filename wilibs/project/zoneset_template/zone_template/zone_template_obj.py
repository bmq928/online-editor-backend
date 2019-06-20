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
   
    def __repr__(self):
        obj = dict(self.ZoneTemplateInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()  
    def getZoneTemplateInfo(self):
        tmp = getZoneSetTeamplateInfo(self.token, self.ZoneSetTeamplateId)
        listObj = []
        tmpObj = tmp['zone_templates']
        for i in tmpObj:
            if self.ZoneTemplateId == tmpObj[i]['idZoneTemplate']:
                return(ZoneTemplate(self.token, i))
        return False
    
    def getInfo(self):
        return self.getZoneTemplateInfo()
    
    
    