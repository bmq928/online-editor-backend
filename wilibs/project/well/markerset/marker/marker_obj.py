from  .marker_api import *

class Marker:
    def __init__(self, token, markerInfo):
        self.token = token
        self.markerInfo = {
            'idMarker': markerInfo['idMarker'],
            'idMarkerTemplate': markerInfo['idMarkerTemplate'],
            'idMarkerSet': markerInfo['idMarkerTemplate'],
            # 'name': markerInfo['name']
        }
        self.markerId = markerInfo['idMarker']
        self.Depth = markerInfo['depth']
        

    def __repr__(self):
        obj = dict(self.markerInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()
    
    def deleteMarker(self):
        check, content = deleteMarker(self.token, self.markerId)
        if check:
            return True
        else:
            print(content)
        return False
    
    def getMarkerInfo(self):
        check, content = getMarkerInfo(self.token, self.markerId)
        if check:
            return content
        else:
            print(content)
        return {}

    def delete(self):
        return self.deleteMarker()
    
    def getInfo(self):
        return self.getMarkerInfo()