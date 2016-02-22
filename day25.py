def generateMatrixArray(xy):
    x = xy[0]
    y = xy[1]

    i=0
    xi = 0
    yi = 0
    resultArray = {}
    resultArray[xy]=0

    while (resultArray[xy]==0):
        i = i+1
        resultArray[(xi, yi)] = i
        xi = xi + 1
        yi = yi - 1
        if (yi < 0):
            yi = xi
            xi = 0

    return resultArray

def countCodeByNumberOf(intVal):
    current = 20151125
    i = 0
    resultArray = {}
    while (i<intVal):
        resultArray[i]=current
        current = (current * 252533)%33554393
        i = i+1
    return resultArray


row = 2947-1
col = 3029-1

matrix =  generateMatrixArray((col,row))
codes = countCodeByNumberOf(matrix[(col,row)])
print codes[matrix[(col,row)]-1]