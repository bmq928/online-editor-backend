import wilibs.wilib as wilib
from wilibs.project import project_obj
from wilibs.project.well import well_obj
from wilibs.project.well.dataset import dataset_obj
from wilibs.project.well.dataset.curve import curve_obj
from wilibs.common import *
import json
from wilibs.common import convertUnit
from wilibs.project.well.markerset_template import markerset_template_obj
from wilibs.project.well.markerset_template.markerset import markerset_obj




#login
client = wilib.login("hoang","1")

project = client.getProjectById(11)

<<<<<<< HEAD
# well = client.getWellById(31)

# well.limitWell(10,1300,'m')

# for i in obj.__dict__:
#     if (i[0] != '_'):
#         print("----'"+i+"'-----")
#         for j in getattr(obj, i).__dict__:
#             if (j[0] != '_'):
#                 print(j)

#{'idProject': 3, 'name': 'hoang'

tmp = client.getProjectById(2)
print(tmp.getListZoneSetTemplate())
=======
print(project.rename('A new name'))



>>>>>>> 704f063a1ec4c17ee29334824af90c8ff4a6b93a
