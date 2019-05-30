from .wellapi import *
from .dataset.dataset_obj import Dataset
from .dataset.datasetapi import createDataSet


class Well:
    def __init__(self, token, wellInfo):
        self.token = token
        self.wellInfo = {
            'idProject': wellInfo['idProject'],
            'idWell': wellInfo['idWell'],
            'name': wellInfo['name'],
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
        print(dataset)
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
        check, content = editWellInfo(self.token, self.wellId, **data)
        if check:
            return None
        return content

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