client = wilib.loginByToken(
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImhvYW5nIiwid2hvYW1pIjoibWFpbi1zZXJ2aWNlIiwicm9sZSI6MCwiY29tcGFueSI6IkkyRyIsImlhdCI6MTU2MDE2MDA3MiwiZXhwIjoxNTYxMDI0MDcyfQ.xRklj-GxV3VetnPsoW8xJMaGWMAcN5_dqL5PFQHBfKA")

project = client.findProjectByName("a")

# plots = project.getListPlot()
# pl = project.createPlot(name='hi-hoang-1')
# print(pl)
plot = client.findPlotByName("hi-hoang-1", "a")
print(plot.editPlot(name="hi"))