client = wilib.login("su_test", "123456")

# project = client.findProjectByName("SD - B9 project - ESS2CLJOC")

projects = client.getListProject()
for project in projects:
    print(project)

project = client.findProjectByName('Test release 1')
print("==", len(project.getAllWells()))
