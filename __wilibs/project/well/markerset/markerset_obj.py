from .markerset_api import *
from .marker.marker_api import *
from .marker.marker_obj import Marker


class MarkerSets:
    def __init__(self, token, markersetsInfo):
        self.token = token
        self.markersetsInfo = {
            'idWell': markersetsInfo['idWell'],
            'idMarkerSet': markersetsInfo['idMarkerSet'],
            'name': markersetsInfo['name']
        }
        self.markersetId = self.markersetsInfo['idMarkerSet']

    def __repr__(self):
        obj = dict(self.markersetsInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()
    
    
    def deleteMarkerSets(self):
        check, content = deleteMarkerSets(self.token, self.markersetId)
        if check:
            return True
        else:
            print(content)
        return False

    def createMarker(self, MarkerTemplateId, Depth):
        check, content = createMarker(self.token, self.markersetId, MarkerTemplateId, Depth)
        if check:
            return Marker(self.token, content)
        else:
            print(content)
        return None
    
    def getListMarker(self):
        check, list = getListMarker(self.token, self.markersetId)
        if check is False and list is None:
            return []
        listObj = []
        for i in list:
            listObj.append(Marker(self.token, i))
        return listObj
    
    def getMarkerSetInfo(self):
        check, content = getMarkerSetInfo(self.token, self.markersetId)
        if check:
            return content
        else:
            print(content)
        return {}
    
    def delete(self):
        return self.deleteMarkerSets()
    
    def getInfo(self):
        return self.getMarkerSetInfo()
    
    def getAllMarkers(self):
        markers = self.getMarkerSetInfo()
        if markers:
            listObj = markers['markers']
            newArr = []
            for i in listObj:
                newArr.append(Marker(self.token, i))
            return newArr
        return []