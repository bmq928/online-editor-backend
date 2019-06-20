from .markerset_template_api import *
from .marker_template.marker_template_api import createMarkerTemplate
from .marker_template.marker__template_obj import MarkerTemplate
# from .markerset.markerset_api import createMarkerSets
# from .markerset.markerset_obj import MarkerSets
from ..well.markerset.markerset_api import *
from ..well.markerset.markerset_obj import MarkerSets
from .marker_template.marker_template_api import *


class MarkerSetTemplate:
    def __init__(self, token, markerSetTemplateInfo):
        self.token = token
        self.markerSetTempateInfo = {
            'idProject': markerSetTemplateInfo['idProject'],
            'idMarkerSetTemplate': markerSetTemplateInfo['idMarkerSetTemplate'],
            'name': markerSetTemplateInfo['name']
        }
        self.markerSetTemplateId = markerSetTemplateInfo['idMarkerSetTemplate']
   
    def __repr__(self):
        obj = dict(self.markerSetTempateInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()  

    def deleteMarkerSetTemplate(self):
        check, content = deleteMarkerSetTemplate(self.token, self.markerSetTemplateId)
        if check:
            return True
        print(content)
        return False

    def createMarkerTemplate(self, name):
        check, content = createMarkerTemplate(self.token, self.markerSetTemplateId, name)
        if check:
            return MarkerTemplate(self.token, content)
        else:
            return None
    
    def newMarkerSetTemplate(self,name):
        return self.createMarkerTemplate(name)

    def createMarkerSets(self, wellId, name):
        check, content = createMarkerSets(self.token, wellId, name)
        if check:
            return MarkerSets(self.token, content)
        else:
            return None
    
    
    def getAllMarkerTemplate(self):
        markerTemplates = self.getMarkerSetTemplateInfo()
        listObj = markerTemplates['marker_templates']
        return listObj
    
    def getMarkerSetTemplateInfo(self):
        check, content = getMarkerSetTeamplateInfo(self.token, self.markerSetTemplateId)
        if check:
            return content
        else:
            print(content)
        return {}

    def delete(self):
        return self.deleteMarkerSetTemplate()


