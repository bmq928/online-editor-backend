import wilibs.wilib as wilib
from wilibs.project import project_obj
from wilibs.project.well import well_obj
from wilibs.project.well.dataset import dataset_obj
from wilibs.project.well.dataset.curve import curve_obj
import json


#login
client = wilib.login("hoang","1")

arrayCurve = client.findCurveByName("array_curve","source","g_1x","demo_edit_curve")
textCurve = client.findCurveByName("text_curve","source","g_1x","demo_edit_curve")
singleCurve = client.findCurveByName("bs","source","g_1x","demo_edit_curve")

arr = arrayCurve.getCurveData()
# arr2 = [arr[i] for i in range(0,10)]

# print(arrayCurve)

# arrayCurve.updateRawCurveData(arr2)

print(arr)
# print(textCurve)

# print(singleCurve)
