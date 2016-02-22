import itertools
import operator

from itertools import product

def getDamage(first, second):
    result =  first['damage'] - second['armor']
    if (result <=0):
        result = 1
    return result

def fight(me, boss):
    myDamage = getDamage(me,boss)
    bossDamage = getDamage(boss,me)

    myLife = me['hit']/bossDamage
    bossLife = boss['hit']/myDamage


    #print bossDamage
    #print myDamage

    #print bossLife
    #print myLife


    print bossLife * bossDamage
    print bossLife * myDamage

    if (bossLife>myLife):
        return False
    else:
        return True

def sumAttribute(d,l,attr):
    sum = 0
    for i in l:
        sum += (d[i])[attr]
    return sum

def returnMe(d,l):
    return {'hit':100,'damage':sumAttribute(d,l,'damage'),'armor':sumAttribute(d,l,'armor')}


#me = {'hit':8,'damage':5, 'armor':5}


Weapons = {
    'Dagger':{
        'cost':8,
        'damage':4,
        'armor':0
    },
    'Shortsword':{
        'cost':10,
        'damage':5,
        'armor':0
    },
    'Warhammer':{
        'cost':25,
        'damage':6,
        'armor':0
    },
    'Longsword':{
        'cost':40,
        'damage':7,
        'armor':0
    },
    'Greataxe':{
        'cost':74,
        'damage':8,
        'armor':0
    }
}

Armors = {
    'Leather':{
        'cost':13,
        'damage':0,
        'armor':1
    },
    'Chainmail':{
        'cost':31,
        'damage':0,
        'armor':2
    },
    'Splintmail':{
        'cost':53,
        'damage':0,
        'armor':3
    },
    'Bandedmail':{
        'cost':75,
        'damage':0,
        'armor':4
    },
    'Platemail':{
        'cost':102,
        'damage':0,
        'armor':5
    },
    'EmptyArmor':{
        'cost':0,
        'damage':0,
        'armor':0
    }
}

Rings = {
    'Damage +1':{
        'cost':25,
        'damage':1,
        'armor':0
    },
    'Damage +2':{
        'cost':50,
        'damage':2,
        'armor':0
    },
    'Damage +3':{
        'cost':100,
        'damage':3,
        'armor':0
    },
    'Defense +1':{
        'cost':20,
        'damage':0,
        'armor':1
    },
    'Defense +2':{
        'cost':40,
        'damage':0,
        'armor':2
    },
    'Defense +3':{
        'cost':80,
        'damage':0,
        'armor':3
    },
    'EmptyRing':{
        'cost':0,
        'damage':0,
        'armor':0
    }
}

#print fight(me,boss)

weaponskeys = Weapons.keys()
armorskeys = Armors.keys()

ringskeys = []

allVariants = []

accessories = {}

accessories.update(Weapons)
accessories.update(Armors)
accessories.update(Rings)

for l in range(1,3):
    for i in (r for r in (itertools.combinations(Rings.keys(), l))):
        ringskeys.append(list(i))

for i in (z for z in product(weaponskeys, armorskeys, ringskeys)):
    temp = []
    iarray = list(i)
    temp.append(iarray[0])
    temp.append(iarray[1])
    temp.extend(iarray[2])
    allVariants.append(temp[:])

#print allVariants
#print accessories


#print sumAttribute(accessories,['Defense +2', 'EmptyRing'],'cost')

me =  returnMe(accessories,['Defense +2', 'EmptyRing'])
boss = {'hit':109,'damage':8, 'armor':2}

imwin = filter(lambda x: fight(returnMe(accessories,x),boss)==False, allVariants)

#imwin = filter(lambda x: sumAttribute(accessories,x,'cost') < 100, imwin)
#print imwin

print sorted(map (lambda x: sumAttribute(accessories,x,'cost'), imwin))

#print fight(returnMe(accessories,['Longsword', 'Leather', 'Damage +1', 'Damage +2']),boss) 

#print sumAttribute(accessories,['Longsword', 'Leather', 'Damage +1', 'Damage +2'],'cost')

