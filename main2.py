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
import wilibs.wilib
from wilibs.project.well.zoneset.zoneset_obj import ZoneSet
client = wilib.login("hoang","1")
test = client.getWellById(61)
tmp_obj = test.getAllZoneSets()
for i in tmp_obj:
    if(type(i) is ZoneSet):
        i.delete()
    
