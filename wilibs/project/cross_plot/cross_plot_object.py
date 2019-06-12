from .cross_plotapi import *

class CrossPlot:
    def __init__(self, token, crossPlotId, name):
        self.token = token
        self.crossPlotId = crossPlotId
        self.crossPlotName = name

    def __repr__(self):
        payload = {
            'idCrossPlot': self.crossPlotId,
            'name': self.crossPlotName,
        }
        return str(payload)

    def __str__(self):
        return self.__repr__()

    def deleteCrossPlot(self):
        check, content = deleteCrossPlot(self.token, self.crossPlotId)
        if check:
            return False
        else:
            print(content)
        return True
    
    def editCrossPlot(self, **kwargs):
        check, content = editCrossPlot(self.token, self.crossPlotId, **kwargs)
        if check:
            return False
        else:
            print(content)
        return True

    def getInfoCrossPlot(self):
        result = {}
        check, content = getCrossPlotInfo(self.token, self.crossPlotId)
        if check:
            result = content
        else:
            print(content)
        return result

    def addTags(self, tags):
        info = self.getInfoCrossPlot()
        relatedTo = info['relatedTo']
        if relatedTo == None:
            relatedTo = {}
        oldTags = []
        if 'tags' in relatedTo:
            oldTags = relatedTo['tags']
        for i in tags:
            if i not in oldTags:
                oldTags.append(i)
        relatedTo['tags'] = oldTags
        return self.editCrossPlot(relatedTo = relatedTo)
    
    def removeTags(self, tags):
        info = self.getInfoCrossPlot()
        relatedTo = info['relatedTo']
        if relatedTo == None:
            return True
        oldTags = []
        if 'tags' in relatedTo:
            oldTags = relatedTo['tags']
        else:
            return True
        for i in tags:
            if i in oldTags:
                oldTags.remove(i)
        relatedTo['tags'] = oldTags
        return self.editCrossPlot(relatedTo = relatedTo)
