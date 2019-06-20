from .marker_template_api import *

class MarkerTemplate:
    def __init__(self, token, markerTemplateInfo):
        self.token = token
        self.markerTemplateInfo = {
           'idMarkerTemplate': markerTemplateInfo['idMarkerTemplate'],
           'name': markerTemplateInfo['name'],
           'lineWidth': markerTemplateInfo['lineWidth']
        }
        
    def __repr__(self):
        obj = dict(self.markerTemplateInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()
    def deleteMarkerTemplate(self):
        check, content = deleteMarkerTemplate(self.token, self.MarkerTemplateId)
        if check:
            return True
        else:
            print(content)
        return False
    def getMarkerTemplateInfo(self):
        check, content = getMarkerTemplateInfo(self.token, self.MarkerTemplateId)
        if check:
            return content
        else:
            print(content)
        return None

    def delete(self):
        return self.deleteMarkerTemplate()
    
    def getInfo(self):
        return self.getMarkerTemplateInfo()