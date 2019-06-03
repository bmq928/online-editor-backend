client = wilib.loginByToken(
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImhvYW5nIiwicm9sZSI6MiwiY29tcGFueSI6IkVTUyIsImlhdCI6MTU1OTU2NDcwMSwiZXhwIjoxNTU5NzM3NTAxfQ.RIlHsInhoilshezrCReAJJCZR2y3UQAe08n-uTFbo-Q")

well = client.findWellByName("w4", "hoang")
if well:
    well.updateWellHeader(header='WTYPE', value='abababab', unit='m')
else:
    print("Well not found")
