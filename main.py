from tempfile import mkstemp
import os
from tempfile import TemporaryFile

import wilibs.wilib as wilib
client = wilib.login("tunghx","123456")


curve = client.getCurveById(78)

curves = curve.getCurveData()

curves.append({'x':1111, 'y': 1234})

curve.updateCurveData(curves)

print(curve.getCurveData())

