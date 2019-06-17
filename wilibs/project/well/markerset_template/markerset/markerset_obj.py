from .markerset_api import *
from .marker.marker_api import createMarker
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

    def createMarker(self, MarkerSetTemplateId, name):
        check, content = createMarker(self.token, self.markersetId, MarkerSetTemplateId, name)
        if check:
            return Marker(self.token, content)
        else:
            print(content)
        return None