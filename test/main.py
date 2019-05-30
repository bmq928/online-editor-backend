from random import random

client = wilib.loginByToken(
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImhvYW5nIiwicm9sZSI6MCwiY29tcGFueSI6IkkyRyIsImlhdCI6MTU1OTAyODg1NiwiZXhwIjoxNTU5MjAxNjU2fQ.TOF8Q2QU8rcCowD26lDXqcEa-TID7yKxzuMvRVwl3q8")

# curveObj = client.getCurveById(661)
# curveInfo = curveObj.getCurveInfo()
# curveObj.clipDataCurve(0,1)
# print(curveObj.getCurveData())
# obj = client.findWellByName("A", "hoang")
# obj = client.findDatasetByName("myDataset","A", "hoang")
# curve1 = client.findCurveByName("a", "newdataset", "a", "hoAng")
# curve2 = client.findCurveByName("test", "newdataset", "a", "hoAng")
# if curve1 and curve2:
#     result = curve1.copyFamily(curve2)
#     print(result)
# else:
#     print(curve1, curve2)
# dataset = client.findDatasetByName("newdataset", "a", "hoang")
# if dataset:
#     curve = dataset.createBlankCurve("MyCurve123456", unit="M", idFamily=1)
#     print(curve)
# else:
#     print("dataset not found")

# well = client.findWellByName("w4", "hoang")
# dataset = well.createDataset(name="myData", top=1, step=2, bottom=100, unit="M")
# z = well.createZoneSet("12345")
# z = well.getAllZones("2")
# for i in z:
#     print(i)
# r = well.getWellHeaders()
# well = client.findWellByName("mimi", "hoang")
# well.deleteAllZoneSets()
# print(curve.getCurveData())
# print(random())

# curve = client.findCurveByName("m", "mai", "mimi", "hoang");
# data = curve.getCurveData()
# print("oldData: ", data)
# for row in data:
#     row['x'] = 555
# curve.updateCurveData(data)
# newData = curve.getCurveData();
# print("newData: ", newData)

# well = client.findWellByName("w4", "hoang")
# well.renameZone("2", "newZoneSetName", "123")

project = client.findProjectByName("hoang")
wells = project.getAllWells()
print(wells)