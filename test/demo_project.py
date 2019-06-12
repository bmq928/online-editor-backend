client = wilib.login("hoang","1")

project = client.findProjectByName("my")

print(project.newBlankHistogram(name="hoang"))