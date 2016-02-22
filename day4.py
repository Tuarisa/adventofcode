import hashlib
input_raw = 'bgvyzdsv'

def checkLeadZero(s):
    countZero = 0
    for i in list(s):
        if (i=='0'):
            countZero = countZero+1
        else:
            if (countZero < 6):
                return False
    return (countZero >=6)

i=1
while (True):
    current = input_raw+str(i)
    if checkLeadZero(hashlib.md5(current).hexdigest()):
        print i
        break
    i = i+1

