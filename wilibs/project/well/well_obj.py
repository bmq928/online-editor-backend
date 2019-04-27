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

    def getWellHeaders(self):
        """Returns list well headers for this well as array of dict
        """
        check, info = getWellHeaders(self.token, self.wellId)
        if check:
            return info
        return []
    
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