from .curveapi import *
from tempfile import TemporaryFile

class Curve:
    def __init__(self, token, user, curveInfo):
        self.token = token
        self.user = user
        self.curveInfo = {
            'idDataset': curveInfo['idDataset'],
            'idCurve': curveInfo['idCurve'],
            'name': curveInfo['name'],
            'description': curveInfo['description']
        }
        self.curveId = curveInfo['idCurve']

    def __repr__(self):
        obj = dict(self.curveInfo)
        obj['sessionUser'] = self.user['username']
        return str(obj)

    def __str__(self):
        return self.__repr__()

    def getCurveInfo(self):
        """Return curve meta data (info)
        """
        check, content =  getCurveInfo(self.token, self.curveId)
        if check:
            return content
        return None

    def getCurveData(self):
        """Return object contain data of curve
        """
        check, content = getCurveData(self.token, self.curveId)
        if check:
            return content
        return None
    

    def updateCurveData(self, curveData, name = False) :
        tempFile = TemporaryFile('r+')
        temp = []
        for i in curveData:
            arr = []
            arr.append(i['y'])
            arr.append(i['x'])
            temp.append(arr)
        tempFile.write(str(temp))
        tempFile.seek(0)
        return self.updateCurveDataByFile(tempFile)


    def updateCurveDataByFile(self, data, name = False):
        """Update data to curve

        Args: 
            data: file object
            name (optional): name you want to change
        
        Returns:
            None if no error
            err as string to describe what err is

        Example:
            data.txt:
            [[1,2],[3,4],[5,6]]  

            #[1,2] mean {x:2, y:1}

            curve = app.getCurveById(78)
            file = open('data.txt', 'rb')
            err = curve.updateCurveData(file) // array 
            if err:
                print(err)

        """
        check,  content = updateCurveData(self.token, self.curveInfo['idDataset'], self.curveInfo['idCurve'], data, name)
        if check:
            return None
        return content
    
    def editCurveInfo(self, **data):
        """Edit curve info

        Args:
            name, duplicate, unit, initValue (**kwargs) (optional)
        
        Returns:
            None if edit success
            String describe err if false
        
        Example:
            err = curve.editCurveInfo(name = 'new name', unit = 'cm', initValue = '60', duplicate = 1)
            if err:
                print(err)

        """
        check, content = editCurveInfo(self.token,self.user['username'] ,self.curveInfo['idCurve'], **data)
        if check:
            return None
        return content
    
