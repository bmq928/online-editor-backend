import wilibs.wilib as wilib
from wilibs.project import project_obj
from wilibs.project.well import well_obj
from wilibs.project.well.dataset import dataset_obj
from wilibs.project.well.dataset.curve import curve_obj


#login
client = wilib.login("tunghx","123456")


"""project demo"""


#list project

print(client.getDatasetById(27).getListCurve())

err = client.getCurveById(109).deleteCurve()
print(err)

print(client.getDatasetById(27).getListCurve())
