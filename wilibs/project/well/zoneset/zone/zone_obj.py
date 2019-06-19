from .zone_api import *

class Zone:
    def __init__(self, token, ZoneInfo):
        self.token = token
        self.ZoneInfo = {
            'idZoneTemplate': ZoneInfo['idWell'],
            'idZoneSet': ZoneInfo['idZoneSet'],
            'idZone': ZoneInfo['idZone'],
            'name': ZoneInfo['name'],
            'endDepth': ZoneInfo['endDepth'],
            'endDepthTemp': ZoneInfo['endDepthTemp'],
            'startDepth': ZoneInfo['startDepth'],
            'startDepthTemp': ZoneInfo['startDepthTemp']
        }
        self.ZoneId = ZoneInfo['idZone']
        self.name = ZoneInfo['name']
    
    def __repr__(self):
        obj = dict(self.ZoneInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__() 

    def deleteZone(self):
        check, content = deleteZone(self.token, self.ZoneId)
        if check:
            return None
        return content

    def delete(self):
        return self.deleteZone()
    
    def editZone(self, **data):
        check, content = editZone(self.token, **data)
        if check:
            self.ZoneInfo = {
            'idZoneTemplate': ZoneInfo['idWell'],
            'idZoneSet': ZoneInfo['idZoneSet'],
            'idZone': ZoneInfo['idZone'],
            'name': ZoneInfo['name'],
            'endDepth': ZoneInfo['endDepth'],
            'endDepthTemp': ZoneInfo['endDepthTemp'],
            'startDepth': ZoneInfo['startDepth'],
            'startDepthTemp': ZoneInfo['startDepthTemp']
            }
            self.ZoneId = ZoneInfo['idZone']
            self.name = ZoneInfo['name']
            return True
        print(content)
        return False
    
    def edit(self,**data):
        return self.editZone(**data)