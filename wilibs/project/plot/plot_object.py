from .plotapi import *


class LogPlot:
    def __init__(self, token, plotInfo):
        self.token = token
        self.plotInfo = {
            "plotId": plotInfo["idLogPlot"],
            "plotName": plotInfo["name"],
            "tags": plotInfo["relatedTo"]["tags"] if plotInfo["relatedTo"] is not None and "tags" in plotInfo[
                "relatedTo"] else []
        }
        self.plotId = plotInfo["idLogPlot"]
        self.projectId = plotInfo["idProject"]
        self.name = plotInfo["name"]
        self.tags = self.plotInfo["tags"]

    def __repr__(self):
        payload = {
            'idProject': self.projectId,
            'name': self.name,
        }
        return str(payload)

    def __str__(self):
        return self.__repr__()

    def editLogPlot(self, **data):
        check, content = editPlot(self.token, self.plotId, **data)
        if check:
            self.plotInfo = {
            "plotId": content["idLogPlot"],
            "plotName": content["name"],
            "tags": content["relatedTo"]["tags"] if content["relatedTo"] is not None and "tags" in content[
                "relatedTo"] else []
            }
            self.plotId = content["idLogPlot"]
            self.projectId = content["idProject"]
            self.name = content["name"]
            self.tags = self.plotInfo["tags"]
            return True
        else:
            print(content)
            return False
    
    def edit(self, **data):
        return self.editLogPlot(**data)

    def deleteLogPlot(self):
        check, content = deletePlot(self.token, self.plotId)
        if check:
            return True
        else:
            print(content)
            return False
    
    def delete(self):
        return self.deleteLogPlot()

    def getLogPlotInfo(self):
        check, content = infoPlot(self.token, self.plotId)
        if check:
            return content
        else:
            print(content)
            return False

    def getInfo(self):
        return self.getLogPlotInfo()

    def addTags(self, tags):
        plotInfo = self.getLogPlotInfo()
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
        check = self.editLogPlot(relatedTo=relatedTo)
        return check

    def removeTags(self, tags):
        plotInfo = self.getLogPlotInfo()
        relatedTo = plotInfo["relatedTo"]
        if relatedTo and "tags" in relatedTo:
            for t in tags:
                if t in relatedTo["tags"]:
                    relatedTo["tags"].remove(t)
                    self.plotInfo["tags"] = relatedTo["tags"]
        check = self.editLogPlot(relatedTo=relatedTo)
        return check
