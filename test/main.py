import wilibs.wilib as wilib
import wilibs.project.project_obj as project
import wilibs.project.well.well_obj as Well
import wilibs.project.well.dataset.dataset_obj as dataset
import wilibs.project.well.dataset.curve.curve_obj as curve
from tempfile import mkstemp
import os
from tempfile import TemporaryFile


client = wilib.login("tunghx","123456")

"""user"""
#get user info
userData = client.getUserInfo()
#get user name
userName = client.getUserName()

"""project"""
#list project
projectList = client.getListProject()

#getproject with id
projectByID = client.getProjectById(12)

# create project (edit,delete)
project.createProject(client.token, name = "THINH1")

#delete project
client.deleteProject(14)


"""well"""
#create well
project.createWell(client.token, 16,username = "tunghx" , name = "test_well")

#list well
list_Well = Well.listWell(client.token, 1)


"""curve"""
#update curve
curve = client.getCurveById(78)

curves = curve.getCurveData()

curves.append({'x':45400, 'y': 4645})

curve.updateCurveData(curves)

print(curve.getCurveData())


