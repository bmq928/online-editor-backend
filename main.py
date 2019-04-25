import wilibs.wilib as wilib
client = wilib.login("tunghx","123456")

curve = client.getCurveById(99)

err = curve.editCurveInfo(unit = 'cm', name = 'Demo')

if err:
    print(err)
else:
    print(curve.getCurveInfo())
