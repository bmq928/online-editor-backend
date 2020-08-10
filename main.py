import wilibs.wilib as wilib
from wilibs.project import project_obj
from wilibs.project.well import well_obj
from wilibs.project.well.dataset import dataset_obj
from wilibs.project.well.dataset.curve import curve_obj
import json


#login
# client = wilib.login("namphan.work@gmail.com", "@Revotech123")

# print(client.getAllProjects())

#Nam The

client = wilib.login('namnt', '1')

print(client.getMarkerByName('5.3', 'nam_nam_1', '1', 'nam').getInfo())
print(client.getMarkerById(16).getInfo())
