from .zone_template_api import *

class ZoneTemplate:
    def __init__(self, token, ZoneTemplateInfo):
        self.token = token
        self.ZoneTemplateInfo = {
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
    