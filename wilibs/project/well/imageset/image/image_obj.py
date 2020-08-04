from .image_api import *

class Image:
    def __init__(self, token, imageInfo):
        self.token = token
        self.imageInfo = {
            'idImage': imageInfo['idImage'],
            'idImageSet': imageInfo['idImageSet'],
            'name': imageInfo['name']
        }
        self.imageId = self.imageInfo['idImage']
        self.bottom = imageInfo['bottomDepth']
        self.top = imageInfo['topDepth']

    def __repr__(self):
        obj = dict(self.imageInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()
    
    def getImageInfo(self):
        check, content = getImageInfo(self.token, self.imageId)
        if check:
            return content
        else:
            print(content)
        return {}
    
    def editImage(self, **data):
        check, content = editImage(self.token, self.imageId, **data)
        if check:
            return True
        else:
            print(content)
        return False
    
    def deleteImage(self):
        check, content = deleteImage(self.token, self.imageId)
        if check:
            return True
        else:
            print(content)
        return False