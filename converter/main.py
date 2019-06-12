
def rowConvert(row):
    result = ''
    result += str(row['y'])
    if type(row['x']) == type([]):
        for i in row['x']:
            result += ' ' + str(i)
    else:
        result += ' ' + str(row['x'])
    return result

def writeData(file, data):
    convertedData = []
    for i in data:
        convertedData.append(rowConvert(i))
    for i in convertedData:
        file.write(i)
        file.write('\n')
    print(convertedData)

file = open('data.txt', 'w')


writeData(file,[{'y': 0, 'x': [100,200,300]},{'y': 1, 'x': [200,300,400]}, {'y': 2, 'x': [300,400,500]}, {'y':3, 'x': [400,500,600]}])