from .zone_template_api import *

class ZoneTemplate:
    def __init__(self, token, ZoneTemplateInfo):
        self.token = token
        self.ZoneTemplateInfo = {
            'idZoneTemplate': ZoneTemplateInfo['idZoneTemplate'],
            'idZoneSetTemplate': ZoneTemplateInfo['idZoneSetTemplate'],
            'name': ZoneTemplateInfo['name']
        }
        self.ZoneTemplateId = ZoneTemplateInfo['idZoneTemplate']
   
    def __repr__(self):
        obj = dict(self.ZoneTemplateInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()  
    
    
    
