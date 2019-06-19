from .zoneset_api import *

class ZoneSet:
    def __init__(self, token, ZoneSetInfo):
        self.token = token
        self.ZoneSetInfo = {
            'idWell': ZoneSetInfo['idWell'],
            'idZoneSetTemplate': ZoneSetInfo['idZoneSetTemplate'],
            'idZoneSet': ZoneSetInfo['idZoneSet'],
            'name': ZoneSetInfo['name']
        }
        self.ZoneSetId = ZoneSetInfo['idZoneSet']
   
    def __repr__(self):
        obj = dict(self.ZoneSetTemplateInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()  
    
    def getMarkerSetTemplateInfo(self):
        check, content = getZoneSetInfo(self.token, self.ZoneSetId)
        if check:
            return content
        else:
            print(content)
        return {}