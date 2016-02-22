arrayOfDelimeters = {}

def findDelimeters(n):
    d = n/2+n%2
    result = [n]
    while (d>0):
        if (n%d==0):
            if (arrayOfDelimeters.has_key(d)):
                result.extend(arrayOfDelimeters[d])
                break
            else:
                result.append(d)
        d-=1
    arrayOfDelimeters[n]=result
    return result



i = 1
while(True):
    t = sum(findDelimeters(i))
    if (t-1>=3600000):
        print i
        print t
        break
    if (i%10000==1):
        print 'ahtung',i
    i+=1
