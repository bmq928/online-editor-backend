from .project.projectapi import getInfoProject
from .project.project_obj import Project
from .project.projectapi import deleteProject
from .project.well.wellapi import getWellInfo
from .project.well.well_obj import Well
from .project.projectapi import listProject
from .project.well.dataset.datasetapi import getDatasetInfo
from .project.well.dataset.dataset_obj import Dataset
from .project.well.dataset.curve.curveapi import getCurveInfo
from .project.well.dataset.curve.curve_obj import Curve
from .project.projectapi import createProject

class Wilib:
    def __init__(self, user):
        self.token = user['token']
        self.user = user['user']
    
    def deleteProject(self, projectId):
        """Delete project

        Returns: 
            Return err, it's None if no error, delete sucessful
            If there is err, then return string which describe that error
        """
        check, reason = deleteProject(self.token, projectId)
        if check:
            return None
        return reason

    

    def getProjectById(self, projectId):
        check, projectInfo = getInfoProject(self.token, projectId)
        if not check:
            return None
        return Project(self.token, self.user, projectInfo)

    def getWellById(self, wellId):
        check, wellInfo = getWellInfo(self.token, wellId)
        if not check:
            return None
        return Well(self.token, self.user, wellInfo['idProject'], wellInfo)

    def getUserInfo(self):
        """Return user info like username, company id.
        """
        return self.user
    
    def getDatasetById(self, datasetId):
        check, datasetInfo = getDatasetInfo(self.token, datasetId) 
        if check:
            return Dataset(self.token, self.user, datasetInfo)
        return None
    
    def getCurveById(self, curveId):
        check, curveInfo = getCurveInfo(self.token, curveId)
        if check:
            return Curve(self.token, self.user, curveInfo)
        return None

    def getUserName(self):
        """Return username for this account
        """
        return self.user['username']
    
    def getListProject(self):
        obj = listProject(self.token)
        if obj == None:
            return obj
        listProjectObj = []
        for i in obj:
            listProjectObj.append(Project(self.token,self.user, i))
        return listProjectObj

    def createProject(self, **data):
        """Create project for this account.

        pass info for project as name, company, department, description to create new project

        Args:
            **data: need name* (required), company, department, description, all as STRING
        
        Returns:
            (bool, any):
            A tuple.
            If success, :bool: is false, :any: is object contain project info which created.
            If false, :bool: is false, :any: is string tell what error happened.

        Example:
            check, project = createProject(name = 'test project', description='example for lib')

        **name field is required
        """
        check, content = createProject(self.token, **data)
        if check:
            return Project(self.token, self.token, content)
        return None

