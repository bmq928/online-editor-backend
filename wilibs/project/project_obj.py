from .projectapi import *
from .well.wellapi import *
from .well.well_obj import Well

class Project:
    def __init__(self, token, projectInfo):
        self.token = token
        self.projectInfo = {
            'idProject': projectInfo['idProject'],
            'name': projectInfo['name'],
            'alias': projectInfo['alias']
        }
        self.projectId = projectInfo['idProject']

    def __repr__(self):
        payload = {
            'idProject': self.projectId,
            'name': self.projectInfo['name'],
        }
        return str(payload)

    def __str__(self):
        return self.__repr__()
    
    def getListWell(self, **data):
        """Get list well from this project

        Args:
            **data: option dict type.
            start (number), limit (numer), forward (boolean), match(string) 
            all optional

            default:
            start = 0, limit = 50, forward = true, match = '*'

        Returns:
            List well object        
        """
        list = listWell(self.token, self.projectId, **data)
        if list == None:
            return None
        listObj = []
        for i in list:
            listObj.append(Well(self.token, i))
        return listObj
    
    def createWell(self, **data):
        """Create well and put it into this project.

        Args:
            **data (dict): contain name (required) for well.
            bottomDepth, topDepth, step: string (optional)
            idWell: number (optional)
        
        Returns:
            None if create false
            Well obj when create successful
        
        Example:
            wellObj = project.createWell(name = 'hello', idWell = 2, step = 30)
        """
        check, content = createWell(self.token, self.projectId, **data)
        if check:
            return Well(self.token, content)
        else:
            return None
        

    def getProjectId(self):
        """Get this project Id
        """
        return self.projectId

    def getProjectInfo(self):
        """Return project info mini ver
        """
        return getInfoProject(self.token, self.projectId)
    
    def getFullProjectInfo(self):
        """Return full version for project.
        """
        return getFullInfoProject(self.token, self.projectId)

    
    def createProject(self, **data):
        """Create project for this account.

        pass info for project as name, company, department, description to create new project

        Args:
            **data: need name* (required), company, department, description, all as STRING
        
        Retunns:
            (bool, any):
            A tuple.
            If success, :bool: is false, :any: is object contain project info which created.
            If false, :bool: is false, :any: is string tell what error happened.

        Example:
            check, project = createProject(name = 'test project', description='example for lib')

        **name field is required
        """
        return createProject(self.token, **data)

    def editProjectInfo(self, **data):
        """Edit project for this account
        
        pass info need to modify (name, company, department, description)

        Args:
            projectId (int): project id.
            **data: need name, company, department, description, all as STRING and optional
        
        Retunns:
            None if no err.
            String describe error if fail

        Example:
            err = editProject(1, name = 'test project', description='example for lib')
            if (err):
                print(err)
        """
        check, content = editProject(self.token, self.projectId, **data)
        if check:
            return None
        return content

    def changeNameProject(self, name):
        """change name of project

        Returns: 
            True if success, false if false

        """
        check, _ = self.editProjectInfo(name = name)
        return check
    
    def changeDescriptionProject(self, description):
        """change description of project

        Returns: 
            True if success, false if false

        """
        check, _ = self.editProjectInfo(description = description)
        return check

    def changeCompanyInfoProject(self, company):
        """change company info of project

        Returns: 
            True if success, false if false
        """
        check, _ = self.editProjectInfo(company = company)
        return check

    def changeDepartmentInfoProject(self, department):
        """change department info of project

        Returns: 
            True if success, false if false
        """

        check, _ = self.editProjectInfo(department = department)
        return check
    
    def deleteProject(self):
        """Delete project

        Returns: 
            Return err, it's None if no error, delete sucessful
            If there is err, then return string which describe that error
        """

        check, reason = deleteProject(self.token, self.projectId)
        if check:
            return None
        return reason
    def getAllWells(self):
        return self.getListWell()