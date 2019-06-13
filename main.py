import wilibs.wilib as wilib
from wilibs.project import project_obj
from wilibs.project.well import well_obj
from wilibs.project.well.dataset import dataset_obj
from wilibs.project.well.dataset.curve import curve_obj
import json


#login
client = wilib.login("hoang","1")

# arrayCurve = client.findCurveByName("array_curve","source","g_1x","demo_edit_curve")
# textCurve = client.findCurveByName("text_curve","source","g_1x","demo_edit_curve")
# singleCurve = client.findCurveByName("bs","source","g_1x","demo_edit_curve")

well = client.findWellByName("g_3x","demo_edit_curve")
dataset = well.getAllDatasets()[0]
curve = dataset.getAllCurves()[1]
data = curve.getCurveData()
print ([data[i] for i in range(0,20)])
print ([data[i] for i in range(len(data)-20,len(data)-1)])
print(dataset.getDatasetInfo())
well.limitWell(1300,2000, 'm')
print(dataset.getDatasetInfo())
data = curve.getCurveData()
print ([data[i] for i in range(0,20)])
print ([data[i] for i in range(len(data)-20,len(data)-1)])