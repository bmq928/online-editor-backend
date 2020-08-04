from .imageset_api import *
from .image.image_api import getImageInfo
from .image.image_obj import *

class ImageSet:
    def __init__(self, token, imagesetInfo):
        self.token = token
        self.imagesetInfo = {
            'idWell': imagesetInfo['idWell'],
            'idImageSet': imagesetInfo['idImageSet'],
            'name': imagesetInfo['name']
        }
        self.imageSetId = self.imagesetInfo['idImageSet']

    def __repr__(self):
        obj = dict(self.imagesetInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()
    
    def getImageSetInfo(self):
        check, content = getImageSetInfo(self.token, self.imageSetId)
        if check:
            return content
        else:
            print(content)
        return {}
    
    def editImageSet(self, **data):
        check, content = editImageSet(self.token, self.imageSetId, **data)
        if check:
            return True
        else:
            print(content)
        return False
    
    def deleteImageSet(self):
        check, content = deleteImageSet(self.token, self.imageSetId)
        if check:
            return True
        else:
            print(content)
        return False
    
    def getAllImages(self):
        info = self.getImageSetInfo()
        result = []
        if 'images' in info:
            for i in info['images']:
                result.append(Image(self.token, i))
        return result