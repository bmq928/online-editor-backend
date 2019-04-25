from tempfile import mkstemp

import wilibs.wilib as wilib
client = wilib.login("tunghx","123456")

tempFile = mkstemp()

tempFile.write("[[1,2][3,4]]")

curve = client.getCurveById(78)
print(curve)

curve.updateCurveDataByFile(tempFile.open())

tempFile.close()

