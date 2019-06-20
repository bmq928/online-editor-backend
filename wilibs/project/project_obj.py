from .projectapi import *
from .well.wellapi import *
from .well.well_obj import Well
from .plot.plotapi import *
from .plot.plot_object import LogPlot
from .histogram.histogramapi import *
from .histogram.histogram_object import Histogram
from .cross_plot.cross_plot_object import CrossPlot
from .cross_plot.cross_plotapi import *
from .well.zoneset_template.zoneset_template_api import getlistZoneSetTemplate
from .well.zoneset_template.zoneset_template_obj import ZoneSetTemplate
from .well.zoneset_template.zoneset_template_api import *
from .markerset_template.markerset_template_api import *
from .markerset_template.markerset_template_obj import MarkerSetTemplate



class Project:
    def __init__(self, token, projectInfo):
        self.token = token
        self.projectInfo = projectInfo
        self.projectId = projectInfo['idProject']
        self.name = projectInfo['name']
        self.projectName = self.name
        self.alias = projectInfo['alias']
        self.shared = projectInfo['shared'] if 'shared' in projectInfo else False
        self.owner = projectInfo['owner'] if 'owner' in projectInfo else projectInfo['createdBy']

    def __repr__(self):
        payload = {
            'idProject': self.projectId,
            'name': self.projectName,
            'shared': self.shared
        }
        return str(payload)

    def __str__(self):
        return self.__repr__()

    def getListPlot(self):
        check, list = getListPlot(self.token, self.projectId)
        if check is False and list is None:
            return []
        listObj = []
        for i in list:
            listObj.append(LogPlot(self.token, i))
        return listObj

    def getAllLogPlots(self):
        return self.getListPlot()
    
    def getAllPlots(self):
        return self.getListPlot()
    

    def getListWell(self, **data):
        """Get list well from this project

        Args:
            **data: option dict type.
            start (number), limit (numer), forward (boolean), match(string) 
            all optional

            default:
            start = 0, limit = 50, forward = true, match = '*'

        Returns:
            List well object        
        """
        list = listWell(self.token, self.projectId, **data)
        if list is None:
            return []
        listObj = []
        for i in list:
            listObj.append(Well(self.token, i))
        return listObj
    
    def getAllWells(self, **data):
        return self.getListWell(**data)

    def createBlankPlot(self, **data):
        check, content = createNewPlot(self.token, self.projectId, **data)
        if check:
            return content
        else:
            print(content)
            return False

    def newBlankPlot(self, name):
        return self.createBlankPlot(name=name)

    def createWell(self, **data):
        """Create well and put it into this project.

        Args:
            **data (dict): contain name (required) for well.
            bottomDepth, topDepth, step: string (optional)
            idWell: number (optional)
        
        Returns:
            None if create false
            Well obj when create successful
        
        Example:
            wellObj = project.createWell(name = 'hello', idWell = 2, step = 30)
        """
        check, content = createWell(self.token, self.projectId, **data)
        if check:
            return Well(self.token, content)
        else:
            return None

    def newWell(self, **data):
        return self.createWell(**data)

    def createMarkerSetTemplate(self, name):
        check, content = createMarkerSetTemplate(self.token, self.projectId, name)
        if check:
            return MarkerSetTemplate(self.token, content)
        else:
            return None
    
    def newMarketSetTemplate(self, name):
        return self.createMarkerSetTemplate(name)

    def getId(self):
        """Get this project Id
        """
        return self.projectId

    def getInfo(self):
        """Return project info mini ver
        """
        check, content = getInfoProject(self.token, self.projectId)
        if check:
            return content
        print(content)
        return None

    def getFullInfo(self, **data):
        """Return full version for project.
        """
        payload = {'idProject': self.projectId}
        if 'shared' and 'owner' in data:
            payload['shared'] = data['shared']
            payload['owner'] = data['owner']
            payload['name'] = self.projectName
        return getFullInfoProject(self.token, payload)

    # def edit(self, **data):
    #     check, content = editProject(self.token, self.projectId, **data)
    #     if check:
    #         newInfo = self.getInfo()
    #         if newInfo == None:
    #             return False
    #         self.projectInfo = newInfo
    #         self.projectId = newInfo['idProject']
    #         self.projectName = newInfo['name']
    #         self.alias = newInfo['alias']
    #         self.shared = newInfo['shared'] if 'shared' in newInfo else False
    #         self.owner = newInfo['owner'] if 'owner' in newInfo else newInfo['createdBy']
    #         self.name = self.projectName
    #         return True
    #     print(content)
    #     return False

    # def rename(self, newName):
    #     return self.edit(name = newName)

    def delete(self):
        """Delete project

        Returns: 
            Return err, it's None if no error, delete sucessful
            If there is err, then return string which describe that error
        """

        check, reason = deleteProject(self.token, self.projectId)
        if check:
            return True
        print(reason)
        return False

    def isExistsTag(self, relatedTo, tag):
        if relatedTo and "tags" in relatedTo:
            if tag in relatedTo["tags"]:
                return True
        return False

    def findWellsByTag(self, tag):
        wells = self.getAllWells()
        result = []
        for well in wells:
            relatedTo = well.getWellInfo()["relatedTo"]
            if self.isExistsTag(relatedTo, tag):
                result = result + [well]
        return result

    def findDatasetsByTag(self, tag):
        wells = self.getAllWells()
        result = []
        for well in wells:
            datasets = well.getAllDatasets()
            for dataset in datasets:
                relatedTo = dataset.getDatasetInfo()["relatedTo"]
                if self.isExistsTag(relatedTo, tag):
                    result = result + [dataset]
        return result

    def findCurvesByTag(self, tag):
        wells = self.getAllWells()
        result = []
        for well in wells:
            datasets = well.getAllDatasets()
            for dataset in datasets:
                curves = dataset.getAllCurves()
                print("Processing curves in Dataset ", dataset.datasetName)
                for curve in curves:
                    relatedTo = curve.getCurveInfo()["relatedTo"]
                    if self.isExistsTag(relatedTo, tag):
                        result = result + [curve]
        return result
    
    def findLogPlotsByTag(self,tag):
        plots = self.getAllLogPlots()
        result = []
        for plot in plots:
            relatedTo = plot.getInfo()['relatedTo']
            if self.isExistsTag(relatedTo, tag):
                result = result + [plot]
        return result
    
    def findCrossPlotsByTag(self,tag):
        crossPlots = self.getAllCrossPlots()
        result = []
        for crossPlot in crossPlots:
            relatedTo = crossPlot.getInfoCrossPlot()['relatedTo']
            if self.isExistsTag(relatedTo, tag):
                result = result + [crossPlot]
        return result

    def findHistogramsByTag(self,tag):
        histograms = self.getAllHistograms()
        result = []
        for histogram in histograms:
            relatedTo = histogram.getInfoHistogram()['relatedTo']
            if self.isExistsTag(relatedTo, tag):
                result = result + [histogram]
        return result

    def findAllByTag(self, tag):
        wells = self.getAllWells()
        plots = self.getAllLogPlots()
        crossPlots = self.getAllCrossPlots()
        histograms = self.getAllHistograms()

        result = {
            "wells": [],
            "datasets": [],
            "curves": [],
            "plots": [],
            "crossPlots": [],
            "histograms": []
        }

        for plot in plots:
            relatedTo = plot.getInfo()['relatedTo']
            if self.isExistsTag(relatedTo, tag):
                result['plots'] = result['plots'] + [plot]

        for crossPlot in crossPlots:
            relatedTo = crossPlot.getInfo()['relatedTo']
            if self.isExistsTag(relatedTo, tag):
                result['crossPlots'] = result['crossPlots'] + [crossPlot]

        for histogram in histograms:
            relatedTo = histogram.getInfo()['relatedTo']
            if self.isExistsTag(relatedTo, tag):
                result['histogram'] = result['histogram'] + [histogram]

        for well in wells:
            relatedTo = well.getInfo()["relatedTo"]
            if self.isExistsTag(relatedTo, tag):
                result["wells"] = result["wells"] + [well]
            # else:
            datasets = well.getAllDatasets()
            for dataset in datasets:
                relatedToDataset = dataset.getInfo()["relatedTo"]
                if self.isExistsTag(relatedToDataset, tag):
                    result["datasets"] = result["datasets"] + [dataset]
                # else:
                curves = dataset.getAllCurves()
                for curve in curves:
                    relatedToCurve = curve.getInfo()["relatedTo"]
                    if self.isExistsTag(relatedToCurve, tag):
                        result["curves"] = result["curves"] + [curve]
        return result

    def renameTag(self, oldTag, newtag):
        result = True
        objects = self.findAllByTag(oldTag)
        print(objects)
        for curve in objects["curves"]:
            # print("do curve ", curve.curveName)
            result = result and curve.removeTags([oldTag])
            result = result and curve.addTags([newtag])
        for dataset in objects["datasets"]:
            # print("do dataset ", dataset.datasetName)
            result = result and dataset.removeTags([oldTag])
            result = result and dataset.addTags([newtag])
        for well in objects["wells"]:
            # print("do well ", well.wellName)
            result = result and well.removeTags([oldTag])
            result = result and well.addTags([newtag])
        for plot in objects["plots"]:
            result = result and plot.removeTags([oldTag])
            result = result and plot.addTags([newtag])
        for crossPlot in objects["crossPlots"]:
            result = result and crossPlot.removeTags([oldTag])
            result = result and crossPlot.addTags([newtag])
        for histogram in objects["histograms"]:
            result = result and histogram.removeTags([oldTag])
            result = result and histogram.addTags([newtag])
        return result

    def getAllHistograms(self):
        result = []
        check, content = getHistogramList(self.token, self.projectId)
        if check:
            for i in content:
                result.append(Histogram(self.token, i['idHistogram'], i['name']))
        else:
            print(content)
        return result
    
    def createBlankHistogram(self, **kwargs):
        check, content = createHistogram(self.token, self.projectId, **kwargs)
        if check:
            return Histogram(self.token, content['idHistogram'], content['name'])
        else:
            return None
    
    def newBlankHistogram(self, name):
        return self.createBlankHistogram(name=name)

    def getAllCrossPlots(self):
        result = []
        check, content = getCrossPlotList(self.token, self.projectId)
        if check:
            for i in content:
                result.append(CrossPlot(self.token, i['idCrossPlot'], i['name']))
        else:
            print(content)
        return result
    
    def createBlankCrossPlot(self, **kwargs):
        check, content = createCrossPlot(self.token, self.projectId, **kwargs)
        if check:
            return Histogram(self.token, content['idCrossPlot'], content['name'])
        else:
            return None
    
    def newBlankCrossPlot(self, name):
        return self.createBlankCrossPlot(name=name)

    def getAllMarkerSetTemplates(self):
        check, content = listMarkerSetTemplate(self.token, self.projectId)
        listObj = []
        if check :
            for i in content:
                listObj.append(MarkerSetTemplate(self.token, i))
            return listObj
        print(content)   
        return listObj
    
    def getAllZoneSetTemplates(self):
        check, content = getlistZoneSetTemplate(self.token, self.projectId)
        listObj = []
        if check:
            for i in content:
                listObj.append(ZoneSetTemplate(self.token,i))
            return listObj
        print(content)
        return listObj

    def createZoneSetTemplate(self, zoneSetTemplateName):
        check, content = createZoneSetTemplate(self.token,{'idProject' : self.projectId, 'name' : zoneSetTemplateName})
        if check:
            return ZoneSetTemplate(self.token, content)
        else:
            print(content)
            return None

    def newZoneSetTemplate(self, name):
        return self.createZoneSetTemplate(name)