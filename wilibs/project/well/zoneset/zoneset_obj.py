from .zoneset_api import *
from .zone.zone_api import *
from .zone.zone_obj import Zone

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
        self.name = ZoneSetInfo['name']
   
    def __repr__(self):
        obj = dict(self.ZoneSetInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()  
    
    def getZoneSetInfo(self):
        check, content = getZoneSetInfo(self.token, self.ZoneSetId)
        if check:
            return content
        else:
            print(content)
        return {}
    
    def getAllZones(self):
        check, list = getZoneSetInfo(self.token, self.ZoneSetId)
        if check is False and list is None:
            return [] 
        listObj = list['zones']
        print(listObj)
        # for i in list:
        #     listObj.append(Zone(self.token,i))
        # return listObj
        return None