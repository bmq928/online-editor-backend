from .markersets_api import *   
from wilibs.project.well.markersets_template.markersets.marker_template.marker.marker_api import createMarker 

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