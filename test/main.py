import math
import sys
client = wilib.loginByToken(
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImhvYW5nIiwicm9sZSI6MCwiY29tcGFueSI6IkkyRyIsImlhdCI6MTU1OTQ5MjIzNCwiZXhwIjoxNTU5NjY1MDM0fQ.FSFbuOaYi0XvBgrkHDo89_O1EUiPXADmf1Xxd2-aMo0")


# limit function
def Limit(value, minValue, maxValue):
    if value < minValue:
        value = minValue
    if value > maxValue:
        value = maxValue
    return value


# variables
i = 0
m = 2.0
n = 2.0
rw = 0.03
rhom = 2700.0
rhog = 150.0
rhoo = 800.0
rhow = 1000.0

# get project
project = client.findProjectByName("hoang")

if project:
    # get wells list
    wells = project.getAllWells()
    for well in wells:
        print('Well: ', well.wellName, ' processing...')
        # get curves in dataset STD
        dataset = client.findDatasetByName('STD', well.wellName, 'hoang')
        if dataset:
            print("STD dataset found in well ", well.wellName)
            depth = dataset.getDepth()

            # create new temp dataset
            tmpDatasetName = 'newDataset' #change this name each run or program will be exited
            tmpDataset = well.createDataset(name=tmpDatasetName, top=dataset.top, bottom=dataset.bottom,
                                            step=dataset.step, unit=dataset.unit)
            if tmpDataset is None:
                print("Dataset existed ", tmpDatasetName)
                sys.exit()
            # create eval curves in temp dataset
            vcl = tmpDataset.createBlankCurve('VCL')
            vclData = []
            if vcl:
                print('Created curve VCL')
                vclData = vcl.getCurveData()

            phit = tmpDataset.createBlankCurve('PHIT')
            phitData = []
            if phit:
                print('Created curve PHIT')
                phitData = phit.getCurveData()

            swt = tmpDataset.createBlankCurve('SWR')
            swtData = []
            if swt:
                print('Created curve SWR')
                swtData = swt.getCurveData()

            bvwt = tmpDataset.createBlankCurve('BVWT')
            bvwtData = []
            if bvwt:
                print('Created curve BVWT')
                bvwtData = bvwt.getCurveData()

            kmtrx = tmpDataset.createBlankCurve('KMTRX')
            kmtrxData = []
            if kmtrx:
                print('Created curve KMTRX')
                kmtrxData = kmtrx.getCurveData()

            netflag = tmpDataset.createBlankCurve('NETFLAG')
            netflagData = []
            if netflag:
                print('Created curve NETFLAG')
                netflagData = netflag.getCurveData()

            rsvrflag = tmpDataset.createBlankCurve('RSVRFLAG')
            rsvrflagData = []
            if rsvrflag:
                print('Created curve RSVRFLAG')
                rsvrflagData = rsvrflag.getCurveData()

            payflag = tmpDataset.createBlankCurve('PAYFLAG')
            payflagData = []
            if payflag:
                print('Created curve PAYFLAG')
                payflagData = payflag.getCurveData()

            # get curves GR, NPL, DPL, DEN, RD
            findCurveNames = ['GR', 'NPL', 'DPL', 'DEN', 'RD']
            curves = dataset.getAllCurves()
            gr = None
            grData = []
            npl = None
            nplData = []
            dpl = None
            dplData = []
            den = None
            denData = []
            rd = None
            rdData = []
            for curve in curves:
                if curve.curveName == 'GR':
                    gr = curve
                    grData = curve.getCurveData()
                elif curve.curveName == 'NPL':
                    npl = curve
                    nplData = curve.getCurveData()
                elif curve.curveName == 'DPL':
                    dpl = curve
                    dplData = curve.getCurveData()
                elif curve.curveName == 'DEN':
                    den = curve
                    denData = curve.getCurveData()
                elif curve.curveName == 'RD':
                    rd = curve
                    rdData = curve.getCurveData()

            # get all zonesets
            zonesets = well.getAllZoneSets()
            if len(zonesets) != 0:
                for zoneset in zonesets:
                    # get zone in zoneset
                    zones = well.getAllZones(zoneset['name'])
                    for zone in zones:
                        if zone['zone_template']['name'] == 'WLRB' or zone['zone_template']['name'] == 'WLRC':
                            print(well.wellName, ' Processing zone ', zone['zone_template']['name'])
                            begin = zone['startDepth']
                            end = zone['endDepth']
                            for val in depth:
                                if begin <= val <= end:
                                    # find index of depth
                                    i = depth.index(val)
                                    print("Processing index ", i)

                                    # eval curves
                                    vclData[i]['x'] = Limit((nplData[i]['x'] - dplData[i]['x']) / 0.30, 0, 1)
                                    phitData[i]['x'] = Limit((rhom - denData[i]['x']) / (rhom - rhow), 0.001, 0.20)
                                    swtData[i]['x'] = Limit(
                                        math.pow(rw / (rdData[i]['x'] * math.pow(phitData[i]['x'], m)), 1 / n),
                                        0.05, 1)
                                    bvwtData[i]['x'] = phitData[i]['x'] * swtData[i]['x']
                                    kmtrxData[i]['x'] = math.pow(10, 20 * phitData[i]['x'] - 2)

                                    # flag curves
                                    if vclData[i]['x'] < 0.30:
                                        netflagData[i]['x'] = 1
                                    else:
                                        netflagData[i]['x'] = 0
                                    if netflagData[i]['x'] == 1 and phitData[i]['x'] > 0.05:
                                        rsvrflagData[i]['x'] = 1
                                    else:
                                        rsvrflagData[i]['x'] = 0
                                    if rsvrflagData[i]['x'] == 1 and swtData[i]['x'] < 0.5:
                                        payflagData[i]['x'] = 1
                                    else:
                                        payflagData[i]['x'] = 0
                            vcl.updateCurveData(vclData)
                            phit.updateCurveData(phitData)
                            swt.updateCurveData(swtData)
                            bvwt.updateCurveData(bvwtData)
                            kmtrx.updateCurveData(kmtrxData)
                            netflag.updateCurveData(netflagData)
                            rsvrflag.updateCurveData(rsvrflagData)
                            payflag.updateCurveData(payflagData)
        else:
            print("No dataset STD found")
else:
    print('No project found')
