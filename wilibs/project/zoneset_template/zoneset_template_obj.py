from .zoneset_template_api import *
from .zone_template.zone_template_obj import ZoneTemplate

class ZoneSetTemplate:
    def __init__(self, token, ZoneSetTemplateInfo):
        self.token = token
        self.ZoneSetTemplateInfo = {
            'idProject': ZoneSetTemplateInfo['idProject'],
            'idZoneSetTemplate': ZoneSetTemplateInfo['idZoneSetTemplate'],
            'name': ZoneSetTemplateInfo['name']
        }
        self.name = self.ZoneSetTemplateInfo['name']
        self.ZoneSetName = self.name
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
        return None

    def deleteZoneSetTemplate(self):
        check , content = deleteZoneSetTemplate(self.token, self.ZoneSetTemplateId)
        if check:
            return True
        print(content)
        return False

    def delete(self):
        return self.deleteZoneSetTemplate()
    
    def getInfo(self):
        return self.getZoneSetTemplateInfo()
    
    def getAllZoneTemplates(self):
        zoneSetInfo = self.getZoneSetTemplateInfo()
        listObj = []
        if zoneSetInfo:
            listObj = zoneSetInfo['zone_templates']
            newArr = []
            for i in listObj:
                newArr.append(ZoneTemplate(self.token, i))
            return newArr
        return []