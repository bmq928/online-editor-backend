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
            'datasetKey': datasetInfo['datasetKey'],
            'tags': datasetInfo['relatedTo']['tags'] if datasetInfo["relatedTo"] is not None and "tags" in datasetInfo[
                "relatedTo"] else []
        }
        self.datasetName = datasetInfo['name']
        self.datasetId = datasetInfo['idDataset']
        self.wellId = datasetInfo['idWell']
        self.top = float(datasetInfo['top'])
        self.step = float(datasetInfo['step'])
        self.bottom = float(datasetInfo['bottom'])
        self.sampleRate = float(datasetInfo['step'])
        self.unit = datasetInfo['unit']

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
            return None
        return content

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

    # def limitAllCurves(self, top, bottom):
    #     if top <= self.top and bottom >= self.bottom:
    #         return
    #     newTopIndex = top // self.step + 1
    #     newBottomIndex = bottom // self.step
    #     depthInTopIndex = round(newTopIndex * self.step, 4)
    #     depthInBottomIndex = round(newBottomIndex * self.step, 4)
    #     self.editDatasetInfo(top=newTop, bottom=newBottom)
    #     # newTop = top if top > self.top else self.top
    #     # newBottom = bottom if bottom < self.bottom else self.bottom
    #     # curves = self.getAllCurves()
    #     return
    def limitAllCurves(self, top, bottom):
        if top <= self.top and bottom >= self.bottom:
            return
        # find top:
        if self.step == 0:
            newTop = top if top > self.top else self.top
            newBottom = bottom if bottom < self.bottom else self.bottom
            curves = self.getAllCurves()
            datas = [i.getCurveData() for i in curves]
            for data in datas:
                if len(data) > 0:
                    while data[0]['y'] < newTop:
                        del data[0]
                        if len(data) <= 0:
                            break
                if len(data) > 0:
                    while data[len(data) - 1]['y'] > newBottom:
                        del data[len(data) - 1]
                        if len(data) <= 0:
                            break
            for i in range(0, len(curves)):
                curves[i].updateRawCurveData(datas[i])
                print(curves[i].curveName, self.datasetName, "Done")
            self.editDatasetInfo(top=newTop, bottom=newBottom)
            return
        newTopInteger = 0
        delStep = 0
        while self.top + newTopInteger * self.step < top:
            newTopInteger += 1
        newBottomInteger = int((self.bottom - self.top) / self.step)
        while self.top + newBottomInteger * self.step > bottom:
            newBottomInteger -= 1
            delStep += 1
        oldBottomInteger = int((self.bottom - self.top) / self.step)
        newTop = self.top + round(newTopInteger * self.step, 4)
        newBottom = self.top + round(newBottomInteger * self.step, 4)

        curves = self.getAllCurves()
        datas = [i.getCurveData() for i in curves]

        for i in datas:
            for j in range(0, newTopInteger):
                if len(i) > 0:
                    del i[0]
                else:
                    break
            for j in range(0, oldBottomInteger - newBottomInteger):
                if len(i) > 0:
                    del i[len(i) - 1]

        for i in range(0, len(curves)):
            k = 0
            for j in datas[i]:
                j['y'] = k
                k += 1
            curves[i].updateRawCurveData(datas[i])
            print(curves[i].curveName, self.datasetName, "Done")
        self.editDatasetInfo(top=newTop, bottom=newBottom)
        return

    def getDepth(self):
        result = []
        if self.step == 0:
            curves = self.getAllCurves()
            if len(curves) == 0:
                print("This discrete dataset has no curve")
                return []
            else:
                curveData = curves[0].getCurveData()
                result = []
                for row in curveData:
                    result.append(row["y"])
                return result
        else:
            top = self.top
            bottom = self.bottom
            step = self.step
            while top <= bottom:
                result.append(top)
                top += step
        return result

    def getSampleRate(self):
        return self.sampleRate

    def getTotalDepth(self):
        return self.bottom - self.top

    def addTags(self, tags):
        datasetInfo = self.getDatasetInfo()
        relatedTo = datasetInfo["relatedTo"]
        if relatedTo and "tags" in relatedTo:
            oldTags = relatedTo["tags"]
            newTags = oldTags
            for t in tags:
                if not (t in oldTags):
                    newTags = newTags + [t]
            relatedTo["tags"] = newTags
            self.datasetInfo["tags"] = relatedTo["tags"]
        else:
            relatedTo = {
                "tags": tags
            }
        check = self.editDatasetInfo(relatedTo=relatedTo)
        return check

    def removeTags(self, tags):
        datasetInfo = self.getDatasetInfo()
        relatedTo = datasetInfo["relatedTo"]
        if relatedTo and "tags" in relatedTo:
            for t in tags:
                if t in relatedTo["tags"]:
                    relatedTo["tags"].remove(t)
                    self.datasetInfo["tags"] = relatedTo["tags"]
        check = self.editDatasetInfo(relatedTo=relatedTo, name=datasetInfo["name"])
        return check
