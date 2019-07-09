from .project.projectapi import getInfoProject
from .project.project_obj import Project
from .project.projectapi import deleteProject
from .project.well.wellapi import getWellInfo
from .project.well.well_obj import Well
from .project.projectapi import listProject
from .project.well.dataset.datasetapi import getDatasetInfo
from .project.well.dataset.dataset_obj import Dataset
from .project.well.dataset.curve.curveapi import getCurveInfo
from .project.well.dataset.curve.curveapi import updateRawCurveData
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
from .project.markerset_template.markerset_template_api import *
from .project.markerset_template.markerset_template_obj import *
from .project.well.markerset.markerset_api import *
from .project.well.markerset.markerset_obj import *
from .project.markerset_template.marker_template.marker_template_api import *
from .project.markerset_template.marker_template.marker__template_obj import MarkerTemplate
from .project.well.markerset.marker.marker_api import *
from .project.well.markerset.marker.marker_obj import Marker
from .project.param.param_api import getParamInfo
from .project.param.param_obj import Param
# from .project.well.zoneset_template.zoneset_template_api import getZoneSetTeamplateInfo
# from .project.well.zoneset_template.zoneset_template_obj import ZoneSetTemplate
from .project.zoneset_template.zoneset_template_api import *
from .project.zoneset_template.zoneset_template_obj import ZoneSetTemplate
from .project.well.zoneset.zoneset_api import *
from .project.well.zoneset.zoneset_obj import ZoneSet
from .project.well.zoneset.zoneset_obj import getZoneSetInfo
from .project.well.well_obj import *
from .project.well.zoneset.zone.zone_api import *
from .project.well.zoneset.zone.zone_obj import Zone

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


    def getParamById(self, paramId):
        check, paramInfo = getParamInfo(self.token, paramId)
        if not check:
            return None
        return Param(self.token, paramInfo)

    def getDatasetById(self, datasetId):
        check, datasetInfo = getDatasetInfo(self.token, datasetId)
        if check:
            return Dataset(self.token, datasetInfo)
        return None
    
    def getMarkerSetTemplateById(self, MarkerSetTemplateId):
        check, markerSetTemplateInfo = getMarkerSetTeamplateInfo(self.token, MarkerSetTemplateId)
        if check:
            return MarkerSetTemplate(self.token, markerSetTemplateInfo)
        return None
    
    def getMarkerById(self, MarkerId):
        check, markerInfo = getMarkerInfo(self.token, MarkerId)
        if check:
            return Marker(self.token, markerInfo)
        return None

    def getMarkerTemplateById(self, MarkerTemplateId):
        check, markerTemplateInfo = getMarkerTemplateInfo(self.token, MarkerTemplateId)
        if check:
            return MarkerTemplate(self.token, markerTemplateInfo)
        return None
    
    def getMarkerSetById(self, MarkerSetId):
        check, markerSetInfo = getMarkerSetInfo(self.token, MarkerSetId)
        if check:
            return MarkerSets(self.token, markerSetInfo)
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
        return None

    def getWellByName(self, wellName, projectName):
        project = self.getProjectByName(projectName)
        if project:
            wells = project.getListWell()
            for well in wells:
                wellObj = well.getWellInfo()
                if wellObj["name"].lower() == wellName.lower():
                    return well
        print("No well found for name query.")
        return None

    def getDatasetByName(self, datasetName, wellName, projectName):
        well = self.getWellByName(wellName, projectName)
        if well:
            datasets = well.getListDataset()
            for dataset in datasets:
                datasetObj = dataset.getDatasetInfo()
                if datasetObj["name"].lower() == datasetName.lower():
                    return dataset
        print("No dataset found for name query.")
        return None

    def getCurveByName(self, curveName, datasetName, wellName, projectName):
        dataset = self.getDatasetByName(datasetName, wellName, projectName)
        if dataset:
            curves = dataset.getListCurve()
            for curve in curves:
                curveObj = curve.getCurveInfo()
                if curveObj["name"].lower() == curveName.lower():
                    return curve
        print("No curve found for name query.")
        return None

    def getLogPlotByName(self, plotName, projectName):
        project = self.getProjectByName(projectName)
        if project:
            plots = project.getAllPlots()
            for plot in plots:
                if plot.name == plotName:
                    return plot
        print("No plot found for name query.")
        return None

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
                if cplot.name == crossPlotName:
                    return cplot
        print("No cross plot found for name query.")
        return None

    def getHistogramByName(self, histogramName, projectName):
        project = self.getProjectByName(projectName)
        if project:
            htgs = project.getAllHistograms()
            for htg in htgs:
                if htg.name == histogramName:
                    return htg
        print("No histogram found for name query.")
        return None

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
        check, content =  createProject(self.token, **data)
        if check:
            return Project(self.token, content)
        print(content)
        return None
    
    def getZoneSetTemplateById(self, ZoneSetTemplateId):
        check, info = getZoneSetTeamplateInfo(self.token, ZoneSetTemplateId)
        if check:
            return ZoneSetTemplate(self.token, info)
        return None
    
    def getZoneSetById(self, ZoneSetId):
        check, info = getZoneSetInfo(self.token, ZoneSetId)
        if check:
            return ZoneSet(self.token, info)
        return None
     
    # def getZoneSetByName(self, zonesetName, wellName, projectName):
    #     well = self.getWellByName(wellName, projectName)
    #     if well:
    #         ZoneSets = well.getAllZoneSets()
    #         for i in ZoneSets:
    #             tmpObj = i.getZoneSetInfo()
    #             if tmpObj["name"].lower() == zonesetName.lower():
    #                 return tmpObj
    #     print("Zone Set not found")
    #     return False
    
    def getZoneById(self, zoneId):
        check, info = getZoneInfo(self.token, zoneId)
        if check:
            return Zone(self.token, info)
        return None
    
    def resamplingCurve(self, srcCurve, destCurve):
        srcDatasetId = srcCurve.curveInfo['idDataset']
        destDatasetId = destCurve.curveInfo['idDataset']

        #get Dataset for top, bottom, step
        srcDataset = self.getDatasetById(srcDatasetId)
        destDataset = self.getDatasetById(destDatasetId)
        if (not srcDataset) or (not srcDataset):
            print('get Data set false')
            return
        
        #init
        srcTop = srcDataset.top
        # srcBottom = srcDataset.bottom
        srcStep = srcDataset.step
        destTop = destDataset.top
        # destBottom = destDataset.bottom
        destStep = destDataset.step

        srcType = srcCurve.curveInfo['type']
        destType = destCurve.curveInfo['type']

        if (srcType == "TEXT") or (destType == "TEXT"):
            print('We do not cover text curve case')
            return
        
        srcData = srcCurve.getCurveData()
        destData = destCurve.getCurveData()

        #get length
        destLength = len(destData)
        srcLength = len(srcData)


        # topBoundIndex = 0
        bottomBoundIndex = 1
        depthFirstIndex = 0
        depthFirst = depthConvert(destData[depthFirstIndex]['y'], destTop, destStep)


        while (depthFirst > depthConvert(srcData[bottomBoundIndex]['y'], srcTop, srcStep)):
            bottomBoundIndex += 1
            # while (srcData[bottomBoundIndex]['x'] == None):
            #     bottomBoundIndex += 1
            #     if bottomBoundIndex >= srcLength:
            #         return
            if bottomBoundIndex >= srcLength:
                return
            # topBoundIndex = bottomBoundIndex - 1
            # while srcData[topBoundIndex]['x'] == None:
            #     topBoundIndex -= 1
        
        while (depthFirst < depthConvert(srcData[bottomBoundIndex-1]['y'], srcTop, srcStep)):
            depthFirstIndex += 1
            if depthFirstIndex >= destLength:
                return
            depthFirst = depthConvert(destData[depthFirstIndex]['y'], destTop, destStep)
        
        for i in range(depthFirstIndex, destLength):
            depth = depthConvert(destData[i]['y'], destTop, destStep)
            topBound = depthConvert(srcData[bottomBoundIndex-1]['y'], srcTop, srcStep)
            bottomBound = depthConvert(srcData[bottomBoundIndex]['y'], srcTop, srcStep)
            # print('-----------')
            # print(depth)
            # print(topBound)
            # print(depth < topBound)
            # print('-----------')
            # count += 1
            # if count > 15:
            #     return
            isRunOutOfSrc = False
            while depth > bottomBound:
                bottomBoundIndex += 1
                # while (srcData[bottomBoundIndex]['x'] == None):
                #     bottomBoundIndex += 1
                #     if bottomBoundIndex >= srcLength:
                #         break
                if bottomBoundIndex >= srcLength:
                    isRunOutOfSrc = True
                    break
                # topBound = depthConvert(srcData[bottomBoundIndex-1]['y'], srcTop, srcStep)
                bottomBound = depthConvert(srcData[bottomBoundIndex]['y'], srcTop, srcStep)
                
            if isRunOutOfSrc:
                break

            topBound = depthConvert(srcData[bottomBoundIndex-1]['y'], srcTop, srcStep)

            if bottomBound == depth:
                destData[i]['x'] = srcData[bottomBoundIndex]['x']
            elif topBound == depth:
                destData[i]['x'] = srcData[bottomBoundIndex - 1]['x']
            else:

            # if (srcData[topBoundIndex]['x'] != None) and (srcData[bottomBoundIndex]['x'] != None):
                scale = (depth - topBound)/(bottomBound - topBound)
            #     updateValueForResampling(destData[i], srcData[bottomBoundIndex], srcData[topBoundIndex], srcType, destType, scale)
            #     destData[i]['x'] = ((depth - topBound)/(bottomBound - topBound))*(srcData[bottomBoundIndex]['x'] - srcData[topBoundIndex]['x']) + srcData[topBoundIndex]['x']
                updateValueForResampling(destData[i], srcData[bottomBoundIndex], srcData[bottomBoundIndex-1], srcType, destType, scale)

            # print('----------')
            # print(depth)
            # print(topBound)
            # print(bottomBound)
            # print(srcData[bottomBoundIndex]['x'])
            # print(srcData[bottomBoundIndex - 1]['x'])
            # print(bottomBoundIndex)
            # print('----------')
        
        # print(destData)

        destCurve.updateRawCurveData(destData)


def updateValueForResampling(destData, srcDataBottom, srcDataTop, srcType, destType, scale):
    if srcType == 'NUMBER' and destType == 'NUMBER':
        #NORMAL DO IT
        if srcDataBottom['x'] == None or srcDataTop['x'] == None:
            destData['x'] = None
        else:
            destData['x'] = scale * (srcDataBottom['x'] - srcDataTop['x']) + srcDataTop['x']
    if srcType == 'ARRAY' and destType == 'ARRAY':
        destDataLength = len(destData['x'])
        for i in range(0, destDataLength):
            try:
                if srcDataBottom['x'][i] == None or srcDataTop['x'][i] == None:
                    destData['x'][i] = None
                else:
                    destData['x'][i] = scale * (srcDataBottom['x'][i] - srcDataTop['x'][i]) + srcDataTop['x'][i]
            except:
                print("TWO ARRAY MAYBE NOT IN SAME DIMENSION")

        
        

        
        

    