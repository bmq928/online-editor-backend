client = wilib.loginByToken(
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImVzc19tYXJ0aW4iLCJ3aG9hbWkiOiJtYWluLXNlcnZpY2UiLCJyb2xlIjoyLCJjb21wYW55IjoiRVNTIiwiaWF0IjoxNTU5OTA1MTg4LCJleHAiOjE1NjA3NjkxODh9.GrNuvlzKjT9-V5WAl8wBDlW0wTIui49He-b6RGFGhvw')

project = client.findProjectByName("B9_HARMONIZE");

zonesetSearchName = "2017"

wells = project.getAllWells()
for well in wells:
    zonesets = well.getAllZoneSets()
    for zoneset in zonesets:
        if zoneset['name'] == zonesetSearchName:
            print(well.wellName)
