from .datasetapi import *
from .curve.curve_obj import Curve

class Dataset:
    def __init__(self, token, user, datasetInfo):
        self.token =  token
        self.user = user
        self.datasetInfo = {
            'idWell': datasetInfo['idWell'],
            'idDataset': datasetInfo['idDataset'],
            'name': datasetInfo['name'],
            'datasetKey': datasetInfo['datasetKey'],
            'datasetLabel': datasetInfo['datasetLabel']
        }

    def __repr__(self):
        obj = dict(self.datasetInfo)
        obj['sessionUser'] = self.user['username']
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

    def getListCurve(self):
        """Get list object curve in this dataset
        """
        check, content = getDatasetInfo(self.token, self.datasetInfo['idDataset'])
        if check:
            list = content['curves']
            listObj = []
            for i in list:
                listObj.append(Curve(self.token, self.user, i))
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
    
    def createCurve(self, **data):
        pass