from .marker_template_api import *
from .marker_api import createMarker
class MarkerTemplate:
    def __init__(self, token, MarkerTemplateInfo):
        self.token = token
        self. = {
           'idMarkerTemplate': MarkerTemplateInfo['idMarkerTemplate'],
           'name' : MarkerTemplateInfo['name'],
           'lineWidth' : MarkerTemplateInfo['lineWidth'],
           'lineStyle' : MarkerTemplateInfo['lineStyle'],
           'depth' :  MarkerTemplateInfo['depth'],
           'color' :  MarkerTemplateInfo['color']

        }
        self.MarkerTemplateId =  markerInfo['idMarkerTemplate']
        self.MarkerTemplateName =  markerInfo['name']
        self.LineWidth =  markerInfo['lineWidth']
        self.LineStyle =  markerInfo['lineStyle']
        self.Depth =  markerInfo['Depth']
        self.Color =  markerInfo['color']

    def __repr__(self):
        obj = dict(self.imagesetInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()
    
    def createMarker(self, name):
        check, content = createMarker(self.token, self.MarkerTemplateId, name)
        if check:
            return True
        else:
            print(content)
        return False
    