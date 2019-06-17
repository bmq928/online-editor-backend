from .marker_template_api import *
class MarkerTemplate:
    def __init__(self, token, MarkerTemplateInfo):
        self.token = token
        self.MarkerTemplateInfo = {
           'idMarkerTemplate': MarkerTemplateInfo['idMarkerTemplate'],
           'name': MarkerTemplateInfo['name'],
           'lineWidth': MarkerTemplateInfo['lineWidth'],
           'lineStyle': MarkerTemplateInfo['lineStyle'],
           'depth':  MarkerTemplateInfo['depth'],
           'color':  MarkerTemplateInfo['color']

        }
        self.MarkerTemplateId = MarkerTemplateInfo['idMarkerTemplate']
        self.MarkerTemplateName = MarkerTemplateInfo['name']
        self.LineWidth = MarkerTemplateInfo['lineWidth']
        self.LineStyle = MarkerTemplateInfo['lineStyle']
        self.Depth = MarkerTemplateInfo['Depth']
        self.Color = MarkerTemplateInfo['color']

    def __repr__(self):
        obj = dict(self.MarkerTemplateInfo)
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
    