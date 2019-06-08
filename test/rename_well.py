import time
client = wilib.loginByToken(
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImVzc19kZW1vIiwicm9sZSI6MiwiY29tcGFueSI6IkVTUyIsImlhdCI6MTU1OTg5ODgxNiwiZXhwIjoxNTYwMDcxNjE2fQ.pRvh45jxdtVP8-lwswaagNTReaRJftQES1tGXoGA2rM")

project = client.findProjectByName("B9_HARMONIZE")
wells = project.getAllWells()

for well in wells:
    result = well.editWellInfo(name=well.wellName.replace("SD", "ESS"))
    print("Edit well ", well.wellName, " result : ", result)
    time.sleep(10)
