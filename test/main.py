import wilibs.wilib as wilib
client = wilib.login("thinh","1")
project = client.getListProject()

print(project)
