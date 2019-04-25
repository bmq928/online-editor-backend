import wilibs.wilib as wilib
client = wilib.login("hoang","1")

# curve = client.getCurveById(99)

# err = curve.editCurveInfo(unit = 'cm', name = 'Demo')

# #lấy về thông tin người dùng
# getuserinfo = client.getUserInfo()

# #list các project
# listProject = client.getListProject()

# #lấy về 

dataset = client.getDatasetById(41)

curve = dataset.createCurve(name = 'new Curve yoho2', initValue='60', unit = 'cm/h')

# print(curve)