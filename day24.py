import itertools
import operator

input_raw = """1
3
5
11
13
17
19
23
29
31
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113""".split('\n')
input_raw = sorted((map(lambda x: int(x), input_raw)),reverse=True)

def recursiveSumTest():
    array = input_raw
    summ = 20
    result = []
    for i in range(0,len(array)):
        result.append(recursiveSum(summ,array))
        array = rotate(array)
    print result


def recursiveSumRotateArray(array,summ):
    result = []
    for i in range(0,len(array)):
        result.append(recursiveSum(summ,array))
        array = rotate(array)
    return result

def recursiveSumCombArray(array,summ):
    result = []
    for i in range(len(array)):
        for a in  (z for z in itertools.combinations(array, i)):
            if (sum(a)==summ):
                result.append(a)
    return result


def rotate(l):
    return l[1:] + l[:1]

def recursiveSum(summ, array):
    i = 0
    result = []
    while (i < len(array)-1):
        result.append(array[i])
        if (sum(result)==summ):
            return result
        elif(sum(result)>summ):
            result.pop()
        i = i+1
    return result

def multiply(array):
    result = 1
    for i in array:
        result = result * i
    return result

def push(array,value):
    result = array[:]
    result.append(value)
    return result

def recursiveCfromNforK(array):
    result = []
    if (len(array)==2):
        result.append(array)
        result.append([array[0]])
        result.append([array[1]])
    else:
        temp = recursiveCfromNforK(array[1:])
        result = list(temp)
        temp2 =  map(lambda x: push(x,array[0]),temp)
        result.extend(temp2)
    return result

#goalSum =  sum(input_raw)/3
#result = recursiveCfromNforK(input_raw)
#print '1'
#result = filter(lambda x: sum(x)==goalSum, result)  
#print '2'
#print sorted(map (lambda x: multiply(x), result))

#recursiveSumTest()

result =  recursiveSumCombArray(input_raw,sum(input_raw)/4)
result = filter(lambda x: len(x)<=5, result)
#print sorted(result)
print sorted(map (lambda x: multiply(x), result))