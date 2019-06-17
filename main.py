import wilibs.wilib as wilib
from wilibs.project import project_obj
from wilibs.project.well import well_obj
from wilibs.project.well.dataset import dataset_obj
from wilibs.project.well.dataset.curve import curve_obj
from wilibs.common import *
import json
from wilibs.common import convertUnit
import wilibs.export as obj
from wilibs.project.well.markerset_template import markerset_template_obj
from wilibs.project.well.markerset_template.markerset import markerset_obj



#login
client = wilib.login("hoang","1")

# arrayCurve = client.findCurveByName("array_curve","source","g_1x","demo_edit_curve")
# textCurve = client.findCurveByName("text_curve","source","g_1x","demo_edit_curve")
# singleCurve = client.getCurveByName("bs","source","g_1x","demo_edit_curve")
# print(singleCurve)

# well = client.getWellById(31)

# well.limitWell(10,1300,'m')

# for i in obj.__dict__:
#     if (i[0] != '_'):
#         print("----'"+i+"'-----")
#         for j in getattr(obj, i).__dict__:
#             if (j[0] != '_'):
#                 print(j)

#{'idProject': 3, 'name': 'hoang'

# well_obj.createMarkerSets(client.token, 61,name = "thinhjjj")
# list_set = well_obj.getListMarkerSets(client.token, 61)
# print(list_set)
# markersets_obj.deleteMarkerSets(client.token, 24)
#proto = client.getProjectById(2)
# tpm = markerset_template_obj.deleteMarkerSetTemplate(client.token,16)

# project_obj.createMarkerSetTemplate(client.token, 2, "please")

# please = project_obj.listMarkerSetTemplate(client.token, 2)
# print(please)

# markerset_template_obj.deleteMarkerSetTemplate(client.token, 27)
# markerset_template_obj.createMarkerTemplate(client.token,27, "thiithtithti")

pro = client.getProjectById(2)
# pro.createMarkerSetTemplate("hthththt")

# markerset_template_obj.createMarkerTemplate(client.token, 27, "please")
# list_markertemplate = markerset_template_obj.getListMarkerTemplate(client.token,61)
# print(list_markertemplate)
# markerset_template_obj.createMarkerSets(client.token, 61, 27, "troi oi la troi")
# markerset_obj.createMarker(client.token, 25, 105)
# tmp = client.getWellById(61)
# mar = tmp.getListMarkerSets()

tm = client.getMarkerSetTemplateById(34)
tm.deleteMarkerSetTemplate()
