input_raw = """jio a, +18
inc a
tpl a
inc a
tpl a
tpl a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
tpl a
tpl a
inc a
jmp +22
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7
""".split('\n')

registers = {'a':1, 'b':0, 'i':0}

while (registers['i']<len(input_raw)):
    current = input_raw[registers['i']].replace(',','').split(' ')
    command = current[0]
    if (command =='hlf'):
        registers[current[1]]//=2
        registers['i'] +=1
    elif (command =='tpl'):
        registers[current[1]]*=3
        registers['i'] +=1
    elif (command =='inc'):
        registers[current[1]]+=1
        registers['i'] +=1
    elif (command =='jmp'):
        registers['i'] +=int(current[1])
    elif (command =='jie'):
        if (registers[current[1]]%2==0):
            registers['i'] +=int(current[2])
        else:
            registers['i'] +=1
    elif (command =='jio'):
        if (registers[current[1]]==1):
            registers['i'] +=int(current[2])
        else:
            registers['i'] +=1
    else:
        break
    if (registers['b']>500):
        break
    
print registers