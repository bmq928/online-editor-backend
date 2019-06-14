import wilibs.wilib as wilib
from wilibs.project import project_obj
from wilibs.project.well import well_obj
from wilibs.project.well.dataset import dataset_obj
from wilibs.project.well.dataset.curve import curve_obj
from wilibs.common import *
import json
from wilibs.common import convertUnit

#login
# client = wilib.login("hoang","1")

# arrayCurve = client.findCurveByName("array_curve","source","g_1x","demo_edit_curve")
# textCurve = client.findCurveByName("text_curve","source","g_1x","demo_edit_curve")
# singleCurve = client.findCurveByName("bs","source","g_1x","demo_edit_curve")

# well = client.getWellById(31)

# well.limitWell(10,1300,'m')

print(convertUnit(1000,'.0005 M','.01 M'))