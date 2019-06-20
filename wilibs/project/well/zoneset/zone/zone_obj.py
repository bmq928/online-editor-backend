from .zone_api import *
# from ...zoneset_template.zone_template.zone_template_api import *
from ....zoneset_template.zone_template.zone_template_api import *

class Zone:
    def __init__(self, token, ZoneInfo):
        self.token = token
        self.ZoneInfo = {
            'idZoneTemplate': ZoneInfo['idZoneTemplate'],
            'idZoneSet': ZoneInfo['idZoneSet'],
            'idZone': ZoneInfo['idZone'],
            'zone_template': ZoneInfo['zone_template'],
            'endDepth': ZoneInfo['endDepth'],
            'startDepth': ZoneInfo['startDepth'],
        }
        self.ZoneId = ZoneInfo['idZone']
        
    
    def __repr__(self):
        obj = dict(self.ZoneInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__() 

    def deleteZone(self):
        check, content = deleteZone(self.token, self.ZoneId)
        if check:
            return True
        print(content)
        return False

    def delete(self):
        return self.deleteZone()
    
    # def editZone(self, **data):
    #     check, content = editZone(self.token, **data)
    #     if check:
    #         self.ZoneInfo = {
    #         'idZoneTemplate': ZoneInfo['idWell'],
    #         'idZoneSet': ZoneInfo['idZoneSet'],
    #         'idZone': ZoneInfo['idZone'],
    #         'name': ZoneInfo['name'],
    #         'endDepth': ZoneInfo['endDepth'],
    #         'endDepthTemp': ZoneInfo['endDepthTemp'],
    #         'startDepth': ZoneInfo['startDepth'],
    #         'startDepthTemp': ZoneInfo['startDepthTemp']
    #         }
    #         self.ZoneId = ZoneInfo['idZone']
    #         self.name = ZoneInfo['name']
    #         return True
    #     print(content)
    #     return False
    
    # def edit(self,**data):
    #     return self.editZone(**data)
        
    def renameZone(self, newZoneName):
        zone = self.getZoneInfo()
        check, content = editZoneTemplate(self.token,{'idZoneTemplate': zone["idZoneTemplate"],'name': newZoneName})
        if check:
            return True
        else:
            print(content)
        return False
    
    def rename(self, newZoneName):
        return self.renameZone(newZoneName)
    
    def getZoneInfo(self):
        check, content = getZoneInfo(self.token, self.ZoneId)
        if check:
            return content
        else:
            print(content)
        return {}
    
    def getInfo(self):
        return self.getZoneInfo()