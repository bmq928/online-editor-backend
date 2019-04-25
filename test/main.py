import wilibs.wilib as wilib
import wilibs.project.project_obj as project
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
# client.deleteProject(14)


"""well"""
#create well
project.createWell(client.token, 16,username = "tunghx" , name = "test_well")

# getListWell




"""dataset"""



"""curve"""
# craate well 
# create dataset
# create curve ()
project = client.getListProject()
# well = project.createWell()
# dataset = well.createDataset()
# curve = dataset.createCurve()

print(project)
