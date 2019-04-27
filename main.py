import wilibs.wilib as wilib
client = wilib.login("tunghx","123456")

dataset = client.getDatasetById(30)

curve = dataset.createCurve('new Curve check', initValue = 10)

print(curve)