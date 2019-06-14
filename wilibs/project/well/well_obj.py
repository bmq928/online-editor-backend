from .wellapi import *
from .dataset.dataset_obj import Dataset
from .dataset.datasetapi import createDataSet
from ...api_url import DOWNLOAD_BASE_URL

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
        self.wellName = wellInfo['name']
        self.headers = wellInfo['well_headers']

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

    def getWellFullInfo(self):
        """Returns well full info as dict
        """
        check, info = getWellFullInfo(self.token, self.wellId)
        if check:
            return info
        return None

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
            None if there is no err
            err as string
        
        Example: 
            err = wellobj.editWellInfo(name = 'new name well', step = '10')
            if err:
                print(err)
        
        """
        check, _ = editWellInfo(self.token, self.wellId, **data)
        if check:
            return True
        return False

    def deleteWell(self):
        check, content = deleteWell(self.token, self.wellId)
        if check:
            return None
        return content

    def createZoneSet(self, zoneSetName):
        check, content = createZoneSetTemplate(self.token, {'name': zoneSetName, 'idProject': self.projectId})
        if check:
            check, content = createNewZoneSet(self.token, {'name': zoneSetName, 'idWell': self.wellId,
                                                           'idZoneSetTemplate': content['idZoneSetTemplate']})
            if check:
                print("Created zoneset ", zoneSetName)
                return content
            else:
                print(content)
                return None
        else:
            print(content)
            return None

    def limitWell(self, top, bottom, unit):
        datasets = self.getAllDatasets()
        for dataset in datasets:
            dataset.limitAllCurves(top, bottom, unit)


    def getAllZoneSets(self):
        check, content = listZoneSet(self.token, self.wellId)
        if check:
            return content
        else:
            print(check)
            return []

    def getAllZones(self, zonesetname):
        zonesets = self.getAllZoneSets()
        for zoneset in zonesets:
            if zoneset["name"].lower() == zonesetname.lower():
                return zoneset["zones"]
        return []

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
        check, content = self.editWellInfo(name=newName, idGroup=self.getWellInfo()["idGroup"])
        if check:
            self.wellName = newName
            self.wellInfo["name"] = newName
            return True
        else:
            print(content)
        return False

    def deleteAllZoneSets(self):
        zonesets = self.getAllZoneSets()
        for zoneset in zonesets:
            # if zoneset["zone_set_template"]["name"].lower() == zonesetName.lower():
            check, content = deleteZoneSet(self.token, zoneset["idZoneSet"])
            if check:
                print("Deleted zoneset ", zoneset["name"])
            else:
                print(content)
        return True

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

    def renameZoneSet(self, zonesetName, newZoneSetName):
        zonesets = self.getAllZoneSets()
        for zoneset in zonesets:
            if zoneset["name"].lower() == zonesetName.lower():
                check, content = editZoneSetTemplate(self.token, {
                    'idZoneSetTemplate': zoneset["zone_set_template"]["idZoneSetTemplate"], 'name': newZoneSetName})
                c, co = editZoneSet(self.token, {'idZoneSet': zoneset["idZoneSet"], 'name': newZoneSetName})
                if check and c:
                    print("Update zoneset name successfull")
                    return True
                else:
                    print(content, co)
                    return False
        return False

    def renameZone(self, zoneName, zoneSetname, newZoneName):
        zonesets = self.getAllZoneSets()
        for zoneset in zonesets:
            if zoneset["name"].lower() == zoneSetname.lower():
                for zone in zoneset["zones"]:
                    if zone["zone_template"]["name"].lower() == zoneName.lower():
                        check, content = editZoneTemplate(self.token,
                                                          {'idZoneTemplate': zone["zone_template"]["idZoneTemplate"],
                                                           'name': newZoneName})
                        if check:
                            print("Update zone name successfull")
                            return True
                        else:
                            print(content)
        return False

    def getZoneSetByName(self, zonesetName):
        zonesets = self.getAllZoneSets()
        for zoneset in zonesets:
            if zoneset["name"].lower() == zonesetName.lower():
                return zoneset
        return None

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
