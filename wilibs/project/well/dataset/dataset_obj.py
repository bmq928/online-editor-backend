from .datasetapi import *
from .curve.curve_obj import Curve
from .curve.curveapi import createCurve
from .curve.curveapi import checkIfCurveExisted
import math
from tempfile import TemporaryFile
import json


class Dataset:
    def __init__(self, token, datasetInfo):
        self.token = token
        self.datasetInfo = {
            'idWell': datasetInfo['idWell'],
            'idDataset': datasetInfo['idDataset'],
            'name': datasetInfo['name'],
            'datasetKey': datasetInfo['datasetKey']
        }
        self.datasetName = datasetInfo['name']
        self.datasetId = datasetInfo['idDataset']
        self.wellId = datasetInfo['idWell']

    def __repr__(self):
        obj = dict(self.datasetInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()

    def getDatasetInfo(self):
        """Get dataset info as dict
        """
        check, content = getDatasetInfo(self.token, self.datasetInfo['idDataset'])
        if check:
            del content['curves']
            return content
        return None

    def createCurve(self, name, **kwargsData):
        """Create new Curve for this Dataset
        
        Args:
            name: curve name
            **kwargsData: type, unit, idFamily (optional)

        Returns:
            If curve name is existed, return curve obj for that curve
            Else create new curve and return
            Return None if there is err
        """
        # check if existed
        checkIfExisted, content = checkIfCurveExisted(self.token, self.datasetInfo['idDataset'], name)
        if checkIfExisted:
            return Curve(self.token, content)
        initValue = None
        if 'initValue' in kwargsData:
            initValue = kwargsData['initValue']
        datasetInfo = self.getDatasetInfo()
        top = float(datasetInfo['top'])
        bottom = float(datasetInfo['bottom'])
        step = float(datasetInfo['step'])
        length = math.ceil((bottom - top) / step)
        tempArray = []
        for i in range(0, length + 1):
            arr = []
            arr.append(i)
            arr.append(initValue)
            tempArray.append(arr)
        tempFile = TemporaryFile('r+')
        tempFile.write(str(json.dumps(tempArray)))
        tempFile.seek(0)
        check, content = createCurve(self.token, self.datasetInfo['idDataset'], name, tempFile, **kwargsData)
        if check:
            return Curve(self.token, content)
        return None

    def getListCurve(self):
        """Get list object curve in this dataset
        """
        check, content = getDatasetInfo(self.token, self.datasetInfo['idDataset'])
        if check:
            list = content['curves']
            listObj = []
            for i in list:
                listObj.append(Curve(self.token, i))
            return listObj
        return None

    def editDatasetInfo(self, **data):
        """Edit dataset info

        Args:
            optional (**kwargs): name, idWell, datasetKey, datasetLabel
        
        Returns:
            None if success
            str describe err if fail
        
        Example:
            err = datasetobj.editDatasetInfo(name = 'hello', datasetKey='new key', idWell='2')
            if err:
                print(err)
        """
        check, content = editDatasetInfo(self.token, self.datasetInfo['idDataset'], **data)
        if check:
            return None
        return content

    def deleteDataset(self):
        check, content = deleteDataset(self.token, self.datasetInfo['idDataset'])
        if check:
            return True
        else:
            print(content)
        return False

    def createBlankCurve(self, curveName, **data):
        return self.createCurve(curveName, **data)

    def getAllCurves(self):
        curves = self.getListCurve()
        for curve in curves:
            if curve.curveName == "__MD":
                curves.remove(curve)
        return curves

    def renameDataset(self, newName):
        check, content = self.editDatasetInfo(name=newName, datasetKey=newName, datasetLabel=newName)
        if check:
            return True
        else:
            print(content)
        return False
