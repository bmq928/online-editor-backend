from .wellapi import *
from .dataset.dataset_obj import Dataset
from .dataset.datasetapi import createDataSet
from ...api_url import DOWNLOAD_BASE_URL
from .imageset.imageset_obj import *
from .imageset.imageset_api import createImageSet
from .imageset.imageset_api import getListImageSet
from ...common import convertUnit
from ..well.markerset.markerset_api import *
from ..well.markerset.markerset_obj import MarkerSets
from ..zoneset_template.zoneset_template_api import *
from ..zoneset_template.zoneset_template_obj import ZoneSetTemplate
from .zoneset.zoneset_api import *
from .zoneset.zoneset_obj import ZoneSet

defaultHeaders = [
    {'header': 'NULL', 'value': '-9999', 'unit': ''},
    {'header': 'WELL', 'value': '', 'unit': ''},
    {'header': 'UWI', 'value': '', 'unit': ''},
    {'header': 'API', 'value': '', 'unit': ''},
    {'header': 'LATI', 'value': '', 'unit': ''},
    {'header': 'LONG', 'value': '', 'unit': ''},
    {'header': 'E', 'value': '', 'unit': ''},
    {'header': 'N', 'value': '', 'unit': ''},
    {'header': 'KB', 'value': '', 'unit': ''},
    {'header': 'GL', 'value': '', 'unit': ''},
    {'header': 'ID', 'value': '', 'unit': ''},
    {'header': 'NAME', 'value': '', 'unit': ''},
    {'header': 'COMP', 'value': '', 'unit': ''},
    {'header': 'OPERATOR', 'value': '', 'unit': ''},
    {'header': 'AUTHOR', 'value': '', 'unit': ''},
    {'header': 'DATE', 'value': '', 'unit': ''},
    {'header': 'LOGDATE', 'value': '', 'unit': ''},
    {'header': 'SRVC', 'value': '', 'unit': ''},
    {'header': 'GDAT', 'value': '', 'unit': ''},
    {'header': 'LIC', 'value': '', 'unit': ''},
    {'header': 'CNTY', 'value': '', 'unit': ''},
    {'header': 'STATE', 'value': '', 'unit': ''},
    {'header': 'PROV', 'value': '', 'unit': ''},
    {'header': 'CTRY', 'value': '', 'unit': ''},
    {'header': 'LOC', 'value': '', 'unit': ''},
    {'header': 'FLD', 'value': '', 'unit': ''},
    {'header': 'PROJ', 'value': '', 'unit': ''},
    {'header': 'CODE', 'value': '', 'unit': ''},
    {'header': 'AREA', 'value': '', 'unit': ''},
    {'header': 'TYPE', 'value': '', 'unit': ''},
    {'header': 'STATUS', 'value': '', 'unit': ''},
    {'header': 'WTYPE', 'value': '', 'unit': ''},
    {'header': 'filename', 'value': '', 'unit': ''},
    {'header': 'STEP', 'value': '', 'unit': ''},
    {'header': 'STRT', 'value': '', 'unit': ''},
    {'header': 'STOP', 'value': '', 'unit': ''}
]


class Well:
    def __init__(self, token, wellInfo):
        self.token = token
        self.wellInfo = {
            'idProject': wellInfo['idProject'],
            'idWell': wellInfo['idWell'],
            'name': wellInfo['name'],
            'tags': wellInfo['relatedTo']['tags'] if wellInfo["relatedTo"] is not None and "tags" in wellInfo[
                "relatedTo"] else []
        }
        self.wellId = wellInfo['idWell']
        self.projectId = wellInfo['idProject']
        self.name = wellInfo['name']
        self.wellName = self.name
        _, info = getWellInfo(self.token, self.wellId)
        self.headers = info['well_headers']

    def __repr__(self):
        obj = dict(self.wellInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()

    def getWellInfo(self):
        """Get info of well

        Returns:
            Dict contain well info
        """
        check, info = getWellInfo(self.token, self.wellId)
        if check:
            return info
        return None
    
    def getInfo(self):
        return self.getWellInfo()

    def getListDataset(self):
        """Get list dataset in this well

        Returns:
            array contain dataset object
        """
        check, info = getWellInfo(self.token, self.wellId)
        if check:
            list = info['datasets']
            listObj = []
            for i in list:
                listObj.append(Dataset(self.token, i))
            return listObj
        return []
    
    def getListMarkerSets(self):
        check, content = getListMarkerSets(self.token,self.wellId)
        listObj = []
        if check:
            for i in content:
                listObj.append(MarkerSets(self.token, i))
            return listObj
        print(content)
        return listObj

    def getAllMarkerSets(self):
        return self.getListMarkerSets()

    def createImageSet(self, name):
        check, content = createImageSet(name, self.wellId, name)
        if check:
            return ImageSet(self.token, content)
        else:
            print(content)
        return None
    
   
    def createDataset(self, **data):
        """Add dataset to this well

        Args:
            dict: name, datasetKey, datasetLabel (string), unit, top, bottom, step
            datasetLabel is optional, others required
        
        Returns:
            Dataset object if success
            None if fail
        """
        check, dataset = createDataSet(self.token, self.wellId, **data)
        if check:
            return Dataset(self.token, dataset)
        else:
            return None
    
    def newDataset(self, **data):
        return self.createDataset(**data)

    def getWellFullInfo(self):
        """Returns well full info as dict
        """
        check, info = getWellFullInfo(self.token, self.wellId)
        if check:
            return info
        return None
    
    def getFullInfo(self, **data):
        return self.getWellFullInfo(**data)

    # def getWellHeaders(self):
    #     """Returns list well headers for this well as array of dict
    #     """
    #     check, info = getWellHeaders(self.token, self.wellId)
    #     if check:
    #         return info
    #     return []

    def editWellInfo(self, **data):
        """Edit info for this well

        Args:
            Dict optional: name, bottomDepth, topDepth, step
        
        Returns:
            True if success, false if fail
        
        """
        check, content = editWellInfo(self.token, self.wellId, **data)
        if check:
            newInfo = self.getWellInfo()
            self.wellInfo = {
            'idProject': newInfo['idProject'],
            'idWell': newInfo['idWell'],
            'name': newInfo['name'],
            'tags': newInfo['relatedTo']['tags'] if newInfo["relatedTo"] is not None and "tags" in newInfo[
                "relatedTo"] else []
            }
            self.wellId = newInfo['idWell']
            self.projectId = newInfo['idProject']
            self.wellName = newInfo['name']
            self.headers = newInfo['well_headers']
            self.name = self.wellName
            return True
        print(content)
        return False

    def deleteWell(self):
        check, content = deleteWell(self.token, self.wellId)
        if check:
            return True
        print(content)
        return False
    
    def delete(self):
        return self.deleteWell()
    
    def edit(self, **data):
        return self.editWellInfo(**data)

    def createZoneSet(self, zoneSetName):
        check, content = createZoneSetTemplate(self.token, {'name': zoneSetName, 'idProject': self.projectId})
        if check:
            check, content = createZoneSet(self.token, {'name': zoneSetName, 'idWell': self.wellId,'idZoneSetTemplate': content['idZoneSetTemplate']})
            if check:
                print("Created zoneset ", zoneSetName)
                return content
            else:
                print(content)
                return None
        else:
            print(content)
            return None
        
    
    def newZoneSet(self, zoneSetName):
        return self.createZoneSet(zoneSetName)

    def limitWell(self, top, bottom, unit):
        top = convertUnit(top, unit)
        bottom = convertUnit(bottom, unit)
        datasets = self.getAllDatasets()
        for dataset in datasets:
            print("Processing dataset ", dataset.datasetName)
            dataset.limitAllCurves(top, bottom)
        # imageSets = self.getAllImageSets()
        # images = []
        # for i in imageSets:
        #     for j in i.getAllImages():
        #         images.append(j)
        # for i in images:
        #     if i.top < top or i.bottom > bottom:
        #         i.deleteImage()

    # def getAllZoneSets(self):
    #     check, content = listZoneSet(self.token, self.wellId)
    #     if check:
    #         return content
    #     else:
    #         print(check)
    #         return []

    # def getAllZones(self, zonesetname):
    #     zonesets = self.getAllZoneSets()
    #     for zoneset in zonesets:
    #         if zoneset["name"].lower() == zonesetname.lower():
    #             return zoneset["zones"]
    #     return []

    def getAllDatasets(self):
        return self.getListDataset()

    def getWellHeaders(self):
        headers = []
        for header in self.headers:
            headers.append({'name': header['header'], 'value': header['value'], 'unit': header['unit']})
        return headers

    def getWellHeader(self, headerName):
        for header in self.headers:
            if header['header'].lower() == headerName.lower():
                return {'value': header['value'], 'unit': header['unit']}
        return None

    def renameWell(self, newName):
        return self.editWellInfo(name = newName)
    
    def rename(self, newName):
        return self.renameWell(newName)

    # def deleteAllZoneSets(self):
    #     zonesets = self.getAllZoneSets()
    #     for zoneset in zonesets:
    #         # if zoneset["zone_set_template"]["name"].lower() == zonesetName.lower():
    #         check, content = deleteZoneSet(self.token, zoneset["idZoneSet"])
    #         if check:
    #             print("Deleted zoneset ", zoneset["name"])
    #         else:
    #             print(content)
    #     return True

    def deleteZoneSet(self, zonesetName):
        zonesets = self.getAllZoneSets()
        for zoneset in zonesets:
            if zoneset["name"].lower() == zonesetName.lower():
                check, content = deleteZoneSet(self.token, zoneset["idZoneSet"])
                if check:
                    print("Deleted zoneset ", zonesetName)
                else:
                    print(content)
        return True

    # def renameZoneSet(self, zonesetName, newZoneSetName):
    #     zonesets = self.getAllZoneSets()
    #     for zoneset in zonesets:
    #         print(zoneset)
    #         if zoneset['name'].lower() == zonesetName.lower():
    #             check, content = editZoneSetTemplate(self.token, {
    #                 'idZoneSetTemplate': zoneset["zone_set_template"]["idZoneSetTemplate"], 'name': newZoneSetName})
    #             c, co = editZoneSet(self.token, {'idZoneSet': zoneset["idZoneSet"], 'name': newZoneSetName})
    #             if check and c:
    #                 print("Update zoneset name successfull")
    #                 return True
    #             else:
    #                 print(content, co)
    #                 return False
    #     return False

    # def renameZone(self, zoneName, zoneSetname, newZoneName):
    #     zonesets = self.getAllZoneSets()
    #     for zoneset in zonesets:
    #         if zoneset["name"].lower() == zoneSetname.lower():
    #             for zone in zoneset["zones"]:
    #                 if zone["zone_template"]["name"].lower() == zoneName.lower():
    #                     check, content = editZoneTemplate(self.token,
    #                                                       {'idZoneTemplate': zone["zone_template"]["idZoneTemplate"],
    #                                                        'name': newZoneName})
    #                     if check:
    #                         print("Update zone name successfull")
    #                         return True
    #                     else:
    #                         print(content)
    #     return False

    # def getZoneSetByName(self, zonesetName):
    #     zonesets = self.getAllZoneSets()
    #     for zoneset in zonesets:
    #         if zoneset["name"].lower() == zonesetName.lower():
    #             return zoneset
    #     return None

    def exportWellDatacsv(self):
        payload = {'idObjs': [{'idProject': self.projectId, 'idWell': self.wellId, 'datasets': []}]}
        datasets = self.getAllDatasets()
        for dataset in datasets:
            datasetObj = {'idDataset': dataset.datasetId, 'idCurves': []}
            curves = dataset.getAllCurves()
            for curve in curves:
                datasetObj['idCurves'].append(curve.curveId)
            payload['idObjs'][0]['datasets'].append(datasetObj)
        check, content = exportCsvWDRV(self.token, payload)
        if check:
            str = "Your donwload files are ready for well" + self.wellName + ":\n\n"
            for file in content:
                f = downloadExportedFile(self.token, file)
                str += "Donwload url: " + DOWNLOAD_BASE_URL + "/download/exported-files/" + f + "\n"
            str += "\n*** Warning: All files will be deleted after 1 hour ***\n"
            print(str)
            return True
        else:
            print(content)
        return False

    def downloadExportedFile(self):
        downloadExportedFile(self.token, {'fileName': 'W4_W4_1559360192540.csv'})
        return None

    def updateDefaultWellHeaders(self):
        # print(self.headers)
        for defaultHeader in defaultHeaders:
            for wellHeader in self.headers:
                if defaultHeader['header'] == wellHeader['header']:
                    defaultHeader['value'] = wellHeader['value']
                    defaultHeader['unit'] = wellHeader['unit']
                    defaultHeader['idWell'] = wellHeader['idWell']
                    defaultHeader['idWellHeader'] = wellHeader['idWellHeader']
        check, content = updateWellHeaders(self.token, {'idWell': self.wellId, 'headers': defaultHeaders})
        if check:
            return True
        else:
            print(content)
            return False

    def updateWellHeader(self, **data):
        for header in self.headers:
            if header['header'] == data['header']:
                header['value'] = data['value']
                header['unit'] = data['unit']
                check, content = updateWellHeaders(self.token, {'idWell': self.wellId, 'headers': [header]})
                if check:
                    return True
                else:
                    print(content)
                    return False

    def addTags(self, tags):
        wellInfo = self.getWellInfo()
        relatedTo = wellInfo["relatedTo"]
        if relatedTo and "tags" in relatedTo:
            oldTags = relatedTo["tags"]
            newTags = oldTags
            for t in tags:
                if not (t in oldTags):
                    newTags = newTags + [t]
            relatedTo["tags"] = newTags
            wellInfo["tags"] = relatedTo["tags"]
        else:
            relatedTo = {
                "tags": tags
            }
        check = self.editWellInfo(relatedTo=relatedTo)
        return check

    def removeTags(self, tags):
        wellInfo = self.getWellInfo()
        relatedTo = wellInfo["relatedTo"]
        if relatedTo and "tags" in relatedTo:
            for t in tags:
                if t in relatedTo["tags"]:
                    relatedTo["tags"].remove(t)
                    self.wellInfo["tags"] = relatedTo["tags"]
        check = self.editWellInfo(relatedTo=relatedTo, name=wellInfo["name"])
        return check

    def getAllImageSets(self):
        check, content = getListImageSet(self.token, self.wellId)
        result = []
        if check:
            for i in content:
                result.append(ImageSet(self.token, i))
        else:
            print(content)
        return result
    
    def getListZoneSets(self):
        check, content = getListZoneSets(self.token, self.wellId)
        result = []
        if check:
            for i in content:
                result.append(ZoneSet(self.token, i))
        else:
            print(content)
        return result
    
    def getAllZoneSets(self):
        return self.getListZoneSets()
    
    def deleteAllZoneSets(self):
        tmp_obj = self.getAllZoneSets()
        for i in tmp_obj:
            if(type(i) is ZoneSet):
                i.delete()
        return None