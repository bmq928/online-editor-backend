client = wilib.loginByToken(
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImVzc19kZW1vIiwid2hvYW1pIjoibWFpbi1zZXJ2aWNlIiwicm9sZSI6MiwiY29tcGFueSI6IkVTUyIsImlhdCI6MTU1OTk4MjQwMCwiZXhwIjoxNTYwODQ2NDAwfQ.kjfUmW84UeRSRW8sZBgzFIc9QIyEN520cJzLQOl-P00')
# print(client.getListProject());
project = client.findProjectByName("B9_HARMONIZE")

wells = project.getAllWells()
for well in wells:
    rs = well.updateWellHeader(header='FLD', value='ESS', unit='')
    print(well.wellName, " : ", rs)