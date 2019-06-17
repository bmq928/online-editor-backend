from .histogramapi import *

class Histogram:
    def __init__(self, token, histogramId, name):
        self.token = token
        self.histogramId = histogramId
        self.histogramName = name

    def __repr__(self):
        payload = {
            'idHistogram': self.histogramId,
            'name': self.histogramName,
        }
        return str(payload)

    def __str__(self):
        return self.__repr__()

    def deleteHistogram(self):
        check, content = deleteHistogram(self.token, self.histogramId)
        if check:
            return True
        else:
            print(content)
        return False
    
    def delete(self):
        return self.deleteHistogram()
    
    def editHistogram(self, **kwargs):
        check, content = editHistogram(self.token, self.histogramId, **kwargs)
        if check:
            return True
        else:
            print(content)
        return False
    
    def edit(self, **data):
        return self.editHistogram(**data)

    def getInfoHistogram(self):
        check, content = getHistogramInfo(self.token, self.histogramId)
        if check:
            return content
        else:
            print(content)
        return None
    
    def getInfo(self):
        return self.getInfoHistogram()

    def addTags(self, tags):
        info = self.getInfoHistogram()
        relatedTo = info['relatedTo']
        if relatedTo == None:
            relatedTo = {}
        oldTags = []
        if 'tags' in relatedTo:
            oldTags = relatedTo['tags']
        for i in tags:
            if i not in oldTags:
                oldTags.append(i)
        relatedTo['tags'] = oldTags
        return self.editHistogram(relatedTo = relatedTo)
    
    def removeTags(self, tags):
        info = self.getInfoHistogram()
        relatedTo = info['relatedTo']
        if relatedTo == None:
            return True
        oldTags = []
        if 'tags' in relatedTo:
            oldTags = relatedTo['tags']
        else:
            return True
        for i in tags:
            if i in oldTags:
                oldTags.remove(i)
        relatedTo['tags'] = oldTags
        return self.editHistogram(relatedTo = relatedTo)

    
    
