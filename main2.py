import wilibs.wilib as wilib
from wilibs.project import project_obj
from wilibs.project.well import well_obj
from wilibs.project.well.dataset import dataset_obj
from wilibs.project.well.dataset.curve import curve_obj
from wilibs.common import *
import json
from wilibs.common import convertUnit



 

#login
import wilibs.wilib
client = wilib.login("hoang","1")
test = client.getMarkerSetTemplateById(4)
print(test.getInfo())