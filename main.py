import wilibs.wilib as wilib
from wilibs.project import project_obj
from wilibs.project.well import well_obj
from wilibs.project.well.dataset import dataset_obj
from wilibs.project.well.dataset.curve import curve_obj


#login
client = wilib.login("tunghx","123456")


"""project demo"""


#list project
projectList = client.getListProject()

# create project 
project_obj.createProject(client.token, name = "Thinh_test")

#edit project (token, projectID, **data)
project_obj.editProject(client.token, 35, name = "changedName")

#delete project(token, project ID)
project_obj.deleteProject(client.token, 16)



"""well demo"""
#create well
project_obj.createWell(client.token, 43, name = "test_well", unit = "cm")

#list well
project = client.getProjectById(43)
list_well_in_project = project.getListWell()

print(list_well_in_project)

#get well info (token, wellID)

well_info = well_obj.getWellFullInfo(client.token, 51)

#edit well

well_obj.editWellInfo(client.token, 51, name = "changed_name_test-well", topDepth = 50, bottomDepth = 60)

#delete well (token, wellID)

well_obj.deleteWell(client.token, 51)

"""dataset demo"""

#create dataset 
"""loi code ?"""
 # list dataset



"""curve demo"""

# curve = client.getCurveById(99)

# err = curve.editCurveInfo(unit = 'cm', name = 'Demo')

# if err:
#     print(err)
# else:
#     print(curve.getCurveInfo())


dataset = client.getDatasetById(30)

curve = dataset.createCurve('new Curve check', initValue = 10)


