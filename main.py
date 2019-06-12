import wilibs.wilib as wilib
from wilibs.project import project_obj
from wilibs.project.well import well_obj
from wilibs.project.well.dataset import dataset_obj
from wilibs.project.well.dataset.curve import curve_obj


#login
client = wilib.login("tunghx","123456")

client.getCrossPlotById(2).removeTags(['helloTag2'])

print(client.getCrossPlotById(2).getInfoCrossPlot())

# """project demo"""




# #list project
# projectList = client.getListProject()

# # create project 
# project_obj.createProject(client.token, name = "Thinh_test")

# #edit project (token, projectID, **data)
# project_obj.editProject(client.token, 35, name = "changedName")

# #delete project(token, project ID)
# project_obj.deleteProject(client.token, 16)



# """well demo"""
# #create well
# project_obj.createWell(client.token, 43, name = "test_well", unit = "cm")

# #list well
# project = client.getProjectById(43)
# list_well_in_project = project.getListWell()

# #print(list_well_in_project)

# #get well info (token, wellID)

# well_info = well_obj.getWellFullInfo(client.token, 51)

# #edit well

# well_obj.editWellInfo(client.token, 51, name = "changed_name_test-well", topDepth = 50, bottomDepth = 60)

# #delete well (token, wellID)
# '''
# well_to_delete = client.getWellById(54)
# well_to_delete.deleteWell()
# '''


# """dataset demo"""

# #create dataset 

# w = client.getWellById(51)
# w.createDataset(name= '1234', unit = 'm', step = 0.1, bottom = 10, top = 1)

# # list dataset
# list_dataset = w.getListDataset()

# #edit dataset

# dataset_to_edit = client.getDatasetById(32)
# err = dataset_to_edit.editDatasetInfo(name = 'hello', datasetKey='new key', idWell='2')
# if err:
#     print('hell1')

# #delete dataset


# """curve demo"""


# #create curve

# dataset = client.getDatasetById(32)
# curve = dataset.createCurve('456', initValue = 10, unit = 'm')

# #list curve
# data = client.getDatasetById(32)

# list_curve_in_dataset = data.getListCurve()

# #update curve by file

# curve_to_edit = client.getCurveById(124)
# # file = open('F:\Workspace\wi-python-backend\data.txt', 'rb')
# # err = curve_to_edit.updateCurveDataByFile(file)
# # if err:
# #     print(err)

# #edit curve info
# err = curve.editCurveInfo(name = '789', initValue = 69, unit = 'cm', dulplicate = 1)
# if err:
#     print('hell2')

# #delete curve

# # curve_to_edit.deleteCurve()
