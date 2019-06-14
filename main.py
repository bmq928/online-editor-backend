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

well = client.getWellById(34)

well.limitWell(1,5,'m')

# curve = client.getCurveById(527)

# data = curve.getCurveData()

# print(data[3000])
