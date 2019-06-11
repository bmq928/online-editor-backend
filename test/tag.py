client = wilib.loginByToken(
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImVzc19kZW1vIiwid2hvYW1pIjoibWFpbi1zZXJ2aWNlIiwicm9sZSI6MiwiY29tcGFueSI6IkVTUyIsImlhdCI6MTU2MDEzODE3NywiZXhwIjoxNTYxMDAyMTc3fQ.LFvR3ZkE67gqUTKQXgN3E7YY7XuyM5SMdmY6wGE3XQE")
project = client.findProjectByName("S1")
print(project.renameTag("1","hoang"))
print(project.findAllByTag("hoang"))
# wells = project.getAllWells()
# for well in wells:
#     if well.wellName == "1" :
#         print(well)
#         well.removeTags(["1","2","3","hi","ba"])
#         print(well)
# dataset = client.findDatasetByName("newDataset","1","s1")
# dataset.addTags(["1","2","3","4","5","6","7","8"])
# print(dataset)
# curve = client.findCurveByName("A","newDataset","1","s1")
# curve.removeTags(["1","2","3","4","5","11"])
# print(curve)