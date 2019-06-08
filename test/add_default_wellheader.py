# martin client
client = wilib.loginByToken(
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImVzc19tYXJ0aW4iLCJ3aG9hbWkiOiJtYWluLXNlcnZpY2UiLCJyb2xlIjoyLCJjb21wYW55IjoiRVNTIiwiaWF0IjoxNTU5OTA1MTg4LCJleHAiOjE1NjA3NjkxODh9.GrNuvlzKjT9-V5WAl8wBDlW0wTIui49He-b6RGFGhvw')
# client = wilib.loginByToken(
#     'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImkyZ19hZG1pbmlzdHJhdG9yIiwid2hvYW1pIjoibWFpbi1zZXJ2aWNlIiwicm9sZSI6MCwiY29tcGFueSI6IkkyRyIsImlhdCI6MTU1OTk4MDYyMCwiZXhwIjoxNTYwODQ0NjIwfQ.z2DtzGQxQalTHi-b5JjqVUseTm00D8aGMhe-Ax8fjJ0')

project = client.findProjectByName("B9_HARMONIZE")

wells = project.getAllWells()
for well in wells:
    rs = well.updateWellHeader(header='FLD', value='SU TU DEN', unit='')
    print(well.wellName, " : ", rs)

# wells = project.findWellsByTag("EXPLORATION")
# for well in wells:
#     rs = well.updateWellHeader(header='WTYPE', value='EXPLORATION', unit='')
#     print(well.wellName, " : ", rs)

# wells = project.findWellsByTag("PRODUCTION")
# wells = project.findWellsByTag("Injection")
# for well in wells:
#     rs = well.updateWellHeader(header='WTYPE', value='INJECTION', unit='')
#     print(well.wellName, " : ", rs)
