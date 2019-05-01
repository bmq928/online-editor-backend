import builtins
import wilibs.wilib as wilib
from wilibs.project import project_obj
from wilibs.project.well import well_obj
from wilibs.project.well.dataset import dataset_obj
from wilibs.project.well.dataset.curve import curve_obj
builtins.wilib = wilib
builtins.project_obj = project_obj
builtins.well_obj = well_obj
builtins.dataset_obj = dataset_obj
builtins.curve_obj = curve_obj
welcome = """
+---------------------------------------------------------
|                     WELCOME 
+---------------------------------------------------------
"""
print(welcome)
