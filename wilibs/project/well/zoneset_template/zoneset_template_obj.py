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
    
    def getMarkerSetTemplateInfo(self):
        check, content = getZoneSetTeamplateInfo(self.token, self.ZoneSetTemplateId)
        if check:
            return content
        else:
            print(content)
        return {}