from .zone_template_api import *

class ZoneTemplate:
    def __init__(self, token, ZoneTemplateInfo):
        self.token = token
        self.ZoneTemplateInfo = {
            'idProject': ZoneTemplateInfo['idProject'],
            'idZoneSetTemplate': ZoneTemplateInfo['idZoneSetTemplate'],
            'name': ZoneTemplateInfo['name']
        }
        self.ZoneSetTemplateId = ZoneTemplateInfo['idZoneSetTemplate']
   
    def __repr__(self):
        obj = dict(self.ZoneSetTemplateInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()  
    
    
    
