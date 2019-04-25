import wilibs.wilib as wilib
client = wilib.login("thinh","1")
# create project (edit,delete)
# craate well 
# create dataset
# create curve ()
project = client.getListProject()
well = project.createWell()
dataset = well.createDataset()
curve = dataset.createCurve()

print(project)
