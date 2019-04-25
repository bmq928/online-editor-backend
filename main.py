import wilibs.wilib as wilib
client = wilib.login("tunghx","123456")

curve = client.getCurveById(99)

err = curve.editCurveInfo(unit = 'cm', name = 'Demo')

#lấy về thông tin người dùng
getuserinfo = client.getUserInfo()

#list các project
listProject = client.getListProject()

#lấy về 
