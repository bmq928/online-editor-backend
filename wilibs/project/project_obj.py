from .projectapi import *
from .well.wellapi import *
from .well.well_obj import Well
from .plot.plotapi import *
from .plot.plot_object import Plot
from .histogram.histogramapi import *
from .histogram.histogram_object import *
from .cross_plot.cross_plot_object import *
from .cross_plot.cross_plotapi import *


class Project:
    def __init__(self, token, projectInfo):
        self.token = token
        self.projectInfo = {
            'idProject': projectInfo['idProject'],
            'name': projectInfo['name'],
            'alias': projectInfo['alias']
        }
        self.projectId = projectInfo['idProject']

    def __repr__(self):
        payload = {
            'idProject': self.projectId,
            'name': self.projectInfo['name'],
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
            listObj.append(Plot(self.token, i))
        return listObj

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
            return None
        listObj = []
        for i in list:
            listObj.append(Well(self.token, i))
        return listObj

    def newBlankPlot(self, **data):
        check, content = createNewPlot(self.token, self.projectId, **data)
        if check:
            return content
        else:
            print(content)
            return False

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

    def getProjectId(self):
        """Get this project Id
        """
        return self.projectId

    def getProjectInfo(self):
        """Return project info mini ver
        """
        return getInfoProject(self.token, self.projectId)

    def getFullProjectInfo(self):
        """Return full version for project.
        """
        return getFullInfoProject(self.token, self.projectId)

    def createProject(self, **data):
        """Create project for this account.

        pass info for project as name, company, department, description to create new project

        Args:
            **data: need name* (required), company, department, description, all as STRING
        
        Retunns:
            (bool, any):
            A tuple.
            If success, :bool: is false, :any: is object contain project info which created.
            If false, :bool: is false, :any: is string tell what error happened.

        Example:
            check, project = createProject(name = 'test project', description='example for lib')

        **name field is required
        """
        return createProject(self.token, **data)

    def editProjectInfo(self, **data):
        """Edit project for this account
        
        pass info need to modify (name, company, department, description)

        Args:
            projectId (int): project id.
            **data: need name, company, department, description, all as STRING and optional
        
        Retunns:
            None if no err.
            String describe error if fail

        Example:
            err = editProject(1, name = 'test project', description='example for lib')
            if (err):
                print(err)
        """
        check, content = editProject(self.token, self.projectId, **data)
        if check:
            return None
        return content

    def changeNameProject(self, name):
        """change name of project

        Returns: 
            True if success, false if false

        """
        check, _ = self.editProjectInfo(name=name)
        return check

    def changeDescriptionProject(self, description):
        """change description of project

        Returns: 
            True if success, false if false

        """
        check, _ = self.editProjectInfo(description=description)
        return check

    def changeCompanyInfoProject(self, company):
        """change company info of project

        Returns: 
            True if success, false if false
        """
        check, _ = self.editProjectInfo(company=company)
        return check

    def changeDepartmentInfoProject(self, department):
        """change department info of project

        Returns: 
            True if success, false if false
        """

        check, _ = self.editProjectInfo(department=department)
        return check

    def deleteProject(self):
        """Delete project

        Returns: 
            Return err, it's None if no error, delete sucessful
            If there is err, then return string which describe that error
        """

        check, reason = deleteProject(self.token, self.projectId)
        if check:
            return None
        return reason

    def getAllWells(self):
        return self.getListWell()

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
    
    def findPlotByTag(self,tag):
        plots = self.getAllPlots()
        result = []
        for plot in plots:
            relatedTo = plot.getPlotInfo()['relatedTo']
            if self.isExistsTag(relatedTo, tag):
                result = result + [plot]
        return result
    
    def findCrossPlotByTag(self,tag):
        crossPlots = self.getAllCrossPlots()
        result = []
        for crossPlot in crossPlots:
            relatedTo = crossPlot.getInfoCrossPlot()['relatedTo']
            if self.isExistsTag(relatedTo, tag):
                result = result + [crossPlot]
        return result

    def findHistogramByTag(self,tag):
        histograms = self.getAllHistograms()
        result = []
        for histogram in histograms:
            relatedTo = histogram.getInfoHistogram()['relatedTo']
            if self.isExistsTag(relatedTo, tag):
                result = result + [histogram]
        return result

    def findAllByTag(self, tag):
        """ Find by tag in this project.

            Args:
                tag: String

            Returns:
                None if empty
                else List Wells

            Example:
                wells = project.findWellsByTag("tag1")
        """

        wells = self.getAllWells()
        plots = self.getAllPlots()
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
            relatedTo = plot.getPlotInfo()['relatedTo']
            if self.isExistsTag(relatedTo, tag):
                result['plots'] = result['plots'] + [plot]

        for crossPlot in crossPlots:
            relatedTo = crossPlot.getInfoCrossPlot()['relatedTo']
            if self.isExistsTag(relatedTo, tag):
                result['crossPlots'] = result['crossPlots'] + [crossPlot]
                
        for histogram in histograms:
            relatedTo = histogram.getInfoHistogram()['relatedTo']
            if self.isExistsTag(relatedTo, tag):
                result['histogram'] = result['histogram'] + [histogram]

        for well in wells:
            relatedTo = well.getWellInfo()["relatedTo"]
            if self.isExistsTag(relatedTo, tag):
                result["wells"] = result["wells"] + [well]
            # else:
            datasets = well.getAllDatasets()
            for dataset in datasets:
                relatedToDataset = dataset.getDatasetInfo()["relatedTo"]
                if self.isExistsTag(relatedToDataset, tag):
                    result["datasets"] = result["datasets"] + [dataset]
                # else:
                curves = dataset.getAllCurves()
                for curve in curves:
                    relatedToCurve = curve.getCurveInfo()["relatedTo"]
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
    
    def newBlankHistogram(self, **kwargs):
        check, content = createHistogram(self.token, self.projectId, **kwargs)
        if check:
            return Histogram(self.token, content['idHistogram'], content['name'])
        else:
            return None
    
    def getAllCrossPlots(self):
        result = []
        check, content = getCrossPlotList(self.token, self.projectId)
        if check:
            for i in content:
                result.append(CrossPlot(self.token, i['idCrossPlot'], i['name']))
        else:
            print(content)
        return result
    
    def newBlankCrossPlot(self, **kwargs):
        check, content = createCrossPlot(self.token, self.projectId, **kwargs)
        if check:
            return Histogram(self.token, content['idCrossPlot'], content['name'])
        else:
            return None