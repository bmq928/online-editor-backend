from .project.projectapi import getInfoProject
from .project.project_obj import Project
from .project.projectapi import deleteProject
from .project.well.wellapi import getWellInfo
from .project.well.well_obj import Well
from .project.projectapi import listProject
from .project.well.dataset.datasetapi import getDatasetInfo
from .project.well.dataset.dataset_obj import Dataset
from .project.well.dataset.curve.curveapi import getCurveInfo
from .project.well.dataset.curve.curve_obj import Curve
from .api_url import EXPORT_PATH
from .api_url import DOWNLOAD_BASE_URL
from .project.histogram.histogramapi import getHistogramInfo
from .project.histogram.histogram_object import Histogram
from .project.cross_plot.cross_plot_object import CrossPlot
from .project.cross_plot.cross_plotapi import getCrossPlotInfo
from .project.well.imageset.imageset_api import getImageSetInfo
from .project.well.imageset.imageset_obj import ImageSet
from .project.projectapi import createProject


class Wilib:
    def __init__(self, token):
        self.token = token

    def deleteProject(self, projectId):
        """Delete project

        Returns: 
            Return err, it's None if no error, delete sucessful
            If there is err, then return string which describe that error
        """
        check, reason = deleteProject(self.token, projectId)
        if check:
            return None
        return reason

    def getProjectById(self, projectId):
        check, projectInfo = getInfoProject(self.token, projectId)
        if not check:
            return None
        return Project(self.token, projectInfo)

    def getWellById(self, wellId):
        check, wellInfo = getWellInfo(self.token, wellId)
        if not check:
            return None
        return Well(self.token, wellInfo)
        

    def getDatasetById(self, datasetId):
        check, datasetInfo = getDatasetInfo(self.token, datasetId)
        if check:
            return Dataset(self.token, datasetInfo)
        return None

    def getCurveById(self, curveId):
        check, curveInfo = getCurveInfo(self.token, curveId)
        if check:
            return Curve(self.token, curveInfo)
        return None

    def getHistogramById(self, histogramId):
        check, info = getHistogramInfo(self.token, histogramId)
        if check:
            return Histogram(self.token, histogramId, info['name'])
        return None

    def getCrossPlotById(self, crossPlotId):
        check, info = getCrossPlotInfo(self.token, crossPlotId)
        if check:
            return CrossPlot(self.token, crossPlotId, info['name'])
        return None

    def getImageSetById(self, imageSetId):
        check, info = getImageSetInfo(self.token, imageSetId)
        if check:
            return ImageSet(self.token, info)
        return None

    def getAllProjects(self):
        obj = listProject(self.token)
        if obj is None:
            return obj
        listProjectObj = []
        for i in obj:
            listProjectObj.append(Project(self.token, i))
        return listProjectObj

    def getProjectByName(self, projectName):
        projects = self.getAllProjects()
        for project in projects:
            if project.alias.lower() == projectName.lower() or project.projectName.lower() == projectName.lower():
                if project.shared:
                    print("Working in sharing project ...")
                    project = project.getFullInfo(shared=project.shared, owner=project.owner)
                    return Project(self.token, project)
                else:
                    project = project.getFullInfo()
                    return Project(self.token, project)
        return False

    def getWellByName(self, wellName, projectName):
        project = self.getProjectByName(projectName)
        if project:
            wells = project.getListWell()
            for well in wells:
                wellObj = well.getWellInfo()
                if wellObj["name"].lower() == wellName.lower():
                    return well
        print("No well found for name query.")
        return False

    def getDatasetByName(self, datasetName, wellName, projectName):
        well = self.getWellByName(wellName, projectName)
        if well:
            datasets = well.getListDataset()
            for dataset in datasets:
                datasetObj = dataset.getDatasetInfo()
                if datasetObj["name"].lower() == datasetName.lower():
                    return dataset
        print("No dataset found for name query.")
        return False

    def getCurveByName(self, curveName, datasetName, wellName, projectName):
        dataset = self.getDatasetByName(datasetName, wellName, projectName)
        if dataset:
            curves = dataset.getListCurve()
            for curve in curves:
                curveObj = curve.getCurveInfo()
                if curveObj["name"].lower() == curveName.lower():
                    return curve
        print("No curve found for name query.")
        return False

    def getPlotByName(self, plotName, projectName):
        project = self.getProjectByName(projectName)
        if project:
            plots = project.getAllPlots()
            for plot in plots:
                if plot.plotName == plotName:
                    return plot
        print("No plot found for name query.")
        return False

    def wiSavefig(self, plt, fileName, **data):
        filePath = EXPORT_PATH + '/' + fileName
        plt.savefig(filePath, **data)
        str = "Your donwload files are ready:\n\n"
        str += "Donwload url: " + DOWNLOAD_BASE_URL + "/download/exported-files/" + fileName + "\n"
        str += "\n*** Warning: All files will be deleted after 1 hour ***\n"
        print(str)
        return True

    def getCrossPlotByName(self, crossPlotName, projectName):
        project = self.getProjectByName(projectName)
        if project:
            cps = project.getAllCrossPlots()
            for cplot in cps:
                if cplot.crossPlotName == crossPlotName:
                    return cplot
        print("No cross plot found for name query.")
        return False

    def getHistogramByName(self, histogramName, projectName):
        project = self.getProjectByName(projectName)
        if project:
            htgs = project.getAllHistograms()
            for htg in htgs:
                if htg.histogramName == histogramName:
                    return htg
        print("No histogram found for name query.")
        return False

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
    
    def newProject(self, **data):
        return createProject(self.token, **data)