from .plotapi import *


class Plot:
    def __init__(self, token, plotInfo):
        self.token = token
        self.plotInfo = {
            "plotId": plotInfo["idPlot"],
            "plotName": plotInfo["name"],
            "tags": plotInfo["relatedTo"]["tags"] if plotInfo["relatedTo"] is not None and "tags" in plotInfo[
                "relatedTo"] else []
        }
        self.plotId = plotInfo["idPlot"]
        self.projectId = plotInfo["idProject"]
        self.plotName = plotInfo["name"]

    def __repr__(self):
        payload = {
            'idProject': self.projectId,
            'name': self.plotName,
        }
        return str(payload)

    def __str__(self):
        return self.__repr__()

    def editPlot(self, **data):
        check, content = editPlot(self.token, self.plotId, **data)
        if check:
            return content
        else:
            print(content)
            return False

    def deletePlot(self):
        check, content = deletePlot(self.token, self.plotId)
        if check:
            return content
        else:
            print(content)
            return False

    def getPlotInfo(self):
        check, content = infoPlot(self.token, self.plotId)
        if check:
            return content
        else:
            print(content)
            return False

    def addTags(self, tags):
        plotInfo = self.getPlotInfo()
        relatedTo = plotInfo["relatedTo"]
        if relatedTo and "tags" in relatedTo:
            oldTags = relatedTo["tags"]
            newTags = oldTags
            for t in tags:
                if not (t in oldTags):
                    newTags = newTags + [t]
            relatedTo["tags"] = newTags
            plotInfo["tags"] = relatedTo["tags"]
        else:
            relatedTo = {
                "tags": tags
            }
        check = self.editPlot(relatedTo=relatedTo)
        return check

    def removeTags(self, tags):
        plotInfo = self.getPlotInfo()
        relatedTo = plotInfo["relatedTo"]
        if relatedTo and "tags" in relatedTo:
            for t in tags:
                if t in relatedTo["tags"]:
                    relatedTo["tags"].remove(t)
                    self.plotInfo["tags"] = relatedTo["tags"]
        check = self.editPlot(relatedTo=relatedTo)
        return check
