import json
import os
from hashlib import sha256


def verifyAndReturn(r):
    if r['code'] == 200:
        return True, r['content']
    return False, r['reason']


def tokenHeader(token, contentType="application/json"):
    return {
        'Authorization': token,
        'Content-Type': contentType
    }


def genUrlWithWiId(base, payload, token):
    if payload is None:
        payload = {}
    wiSalt = "wi-hash"
    try:
        wiSalt = os.environ["SALT"]
    except:
        # do nothing
        pass
    salt = sha256((wiSalt + token).encode("utf-8")).hexdigest()
    wiid = sha256((json.dumps(payload, separators=(",", ":")) + salt).encode("utf-8")).hexdigest()
    return base + '?wiid=' + wiid


unitTable = [
    {
        "name": ".0005 M",
        "rate": 2000
    },
    {
        "name": ".01 M",
        "rate": 100
    },
    {
        "name": ".1IN",
        "rate": 393.70079
    },
    {
        "name": "0.1 in",
        "rate": 393.70079
    },
    {
        "name": "05mm",
        "rate": 2000
    },
    {
        "name": "1/32 in",
        "rate": 1259.84256
    },
    {
        "name": "angstrom",
        "rate": 10000000000
    },
    {
        "name": "bbl/acre",
        "rate": 25453.96
    },
    {
        "name": "ch",
        "rate": 0.0497096954
    },
    {
        "name": "chBnA",
        "rate": 0.049709739
    },
    {
        "name": "chBnB",
        "rate": 0.049709739
    },
    {
        "name": "ChCla",
        "rate": 0.0497101414329133
    },
    {
        "name": "chSe",
        "rate": 0.0497097815657
    },
    {
        "name": "chUS",
        "rate": 0.049709596
    },
    {
        "name": "CM",
        "rate": 100
    },
    {
        "name": "cm",
        "rate": 100
    },
    {
        "name": "CV",
        "rate": 0.0497096953789867
    },
    {
        "name": "deciin",
        "rate": 393.70079
    },
    {
        "name": "dm",
        "rate": 10
    },
    {
        "name": "F",
        "rate": 3.28084
    },
    {
        "name": "fathom",
        "rate": 0.54680665
    },
    {
        "name": "FEET",
        "rate": 3.28084
    },
    {
        "name": "feet",
        "rate": 3.28084
    },
    {
        "name": "fm",
        "rate": 999999999999999
    },
    {
        "name": "Ft",
        "rate": 3.28084
    },
    {
        "name": "ft",
        "rate": 3.28084
    },
    {
        "name": "ftBnA",
        "rate": 3.28084277
    },
    {
        "name": "ftBnB",
        "rate": 3.28084275
    },
    {
        "name": "ftBr(65)",
        "rate": 3.280831
    },
    {
        "name": "ftCla",
        "rate": 3.28086933
    },
    {
        "name": "ftGC",
        "rate": 3.2808430146
    },
    {
        "name": "ftInd",
        "rate": 3.280845167
    },
    {
        "name": "ftInd(37)",
        "rate": 3.28085701
    },
    {
        "name": "ftInd(62)",
        "rate": 3.2808442
    },
    {
        "name": "ftInd(75)",
        "rate": 3.280845277
    },
    {
        "name": "ftMA",
        "rate": 3.28070801
    },
    {
        "name": "ftSe",
        "rate": 3.28084559
    },
    {
        "name": "ftUS",
        "rate": 3.28083333
    },
    {
        "name": "IN",
        "rate": 39.370079
    },
    {
        "name": "in",
        "rate": 39.370079
    },
    {
        "name": "in/10",
        "rate": 393.70079
    },
    {
        "name": "in/16",
        "rate": 629.921264
    },
    {
        "name": "in/32",
        "rate": 1259.842528
    },
    {
        "name": "in/64",
        "rate": 2519.685056
    },
    {
        "name": "inches",
        "rate": 39.370079
    },
    {
        "name": "inch",
        "rate": 39.370079
    },
    {
        "name": "ins",
        "rate": 39.370079
    },
    {
        "name": "inUS",
        "rate": 39.37
    },
    {
        "name": "KM",
        "rate": 0.001
    },
    {
        "name": "km",
        "rate": 0.001
    },
    {
        "name": "lkBnA",
        "rate": 4.97097389
    },
    {
        "name": "lkBnB",
        "rate": 4.97097389
    },
    {
        "name": "lkCla",
        "rate": 4.971014137
    },
    {
        "name": "lkSe",
        "rate": 4.970978157
    },
    {
        "name": "lkUS",
        "rate": 4.9709596
    },
    {
        "name": "M",
        "rate": 1
    },
    {
        "name": "m",
        "rate": 1
    },
    {
        "name": "m3/m2",
        "rate": 1
    },
    {
        "name": "meter",
        "rate": 1
    },
    {
        "name": "meters",
        "rate": 1
    },
    {
        "name": "metres",
        "rate": 1
    },
    {
        "name": "METERS",
        "rate": 1
    },
    {
        "name": "METRES",
        "rate": 1
    },
    {
        "name": "mGer",
        "rate": 0.9999864
    },
    {
        "name": "mi",
        "rate": 0.0006213712
    },
    {
        "name": "mil",
        "rate": 39370.079
    },
    {
        "name": "miUS",
        "rate": 0.00062137
    },
    {
        "name": "mm",
        "rate": 1000
    },
    {
        "name": "Mm",
        "rate": 0.000001
    },
    {
        "name": "nautmi",
        "rate": 0.00053996
    },
    {
        "name": "nm",
        "rate": 1000000000
    },
    {
        "name": "pm",
        "rate": 1000000000000
    },
    {
        "name": "um",
        "rate": 1000000
    },
    {
        "name": "yd",
        "rate": 1.0936133
    },
    {
        "name": "ydBnA",
        "rate": 1.093614255
    },
    {
        "name": "ydBnB",
        "rate": 1.09361425
    },
    {
        "name": "ydCla",
        "rate": 1.09362311
    },
    {
        "name": "ydIm",
        "rate": 1.09362311152409
    },
    {
        "name": "ydInd",
        "rate": 1.093615055556
    },
    {
        "name": "ydInd(37)",
        "rate": 1.093619
    },
    {
        "name": "ydInd(62)",
        "rate": 1.0936147336
    },
    {
        "name": "ydInd(75)",
        "rate": 1.0936151
    },
    {
        "name": "ydSe",
        "rate": 1.09361519444
    },
    {
        "name": "FT",
        "rate": 3.28084
    }]


def getRate(unitName):
    for i in unitTable:
        if i['name'] == unitName:
            return i['rate']
    return None


def convertUnit(value, srcUnit, destUnit="m"):
    srcRate = getRate(srcUnit)
    destRate = getRate(destUnit)
    if (srcRate == None) or (destRate == None):
        return False
    return value * srcRate / destRate


def depthTransfer(arr, top, bottom, step):
    if step == 0:
        return arr
    for i in arr:
        i['y'] = top + step * i['y']
    return arr


def depthConvert(value, top, step):
    if step == 0:
        return value
    return top + step * value
