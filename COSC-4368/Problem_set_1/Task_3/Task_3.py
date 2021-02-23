import sys
from test.test_importlib.data03 import namespace


if len(sys.argv) > 1 and sys.argv[1] == 'test':
    print('Starting test...\n\n')

global nva
nva = 0

def C1(A, B, C, E, F):
    # if (A['value'] == (B['value']+C['value']+E['value']+F['value'])):
    if (A == (B + C + E + F)):
        return True
    return False

def C2(D, E, F):
    # if ( D['value'] == E['value'] + F['value'] + 21):
    if (D == (E + F + 21)):
        return True
    return False

def C3(B, C, D, E, F):
    if (D**2 == (E**2 * (B + C + E + F) + 417)):
        return True
    return False

def incVal(var):
    global nva
    nva += 1
    var['count'] += 1
    var['value'] = var['value'] + 1
    output(var)

def checkConstraintsA(B, C, D, E, F):
    if (C2(D, E, F) and C3(B, C, D, E, F)):
        return True
    return False

def setVal(var, newVal):
    global nva
    nva += 1
    var['count'] += 1
    var['value'] = newVal
    output(var)

def output(var):
    print(var['name'], '=', var['value'], '\tcount =', var['count'])

def printAll(B, C, D, E, F):
    print('A =', (B + C + E + F), ', B =', B, ', C =', C, ', D =', D, ', E =', E, ', F =', F)
    

def problemA():
    global nva
    minA = 4
    maxA = 50 # 
    maxE = 8

    # incVal(varList['A'])

    #loop over possibilities
    # for f in range(1, 29):
    #     nva += 1 #increase f
    #     for e in range(1, maxE+1):
    #         nva += 1 #increase e
    #         d = e + f + 21
    #         nva += 1 #increase d
    #         for b in range(1, 50-(e+f)):
    #             nva += 1 #increase b
    #             for c in range(1, 50-(e+f)-b):
    #                 nva += 1 #increase c
    #                 a = (b + c + e + f)
    #                 nva += 1 #increase a
    #                 # print(nva)
    #                 printAll(a, b, c, d, e, f)
    #                 if (checkConstraintsA(a, b, c, d, e, f)):
    #                     print('Found solution!')
    #                     return

    for f in range(1, 29):
        nva += 1 #increase f
        for e in range(1, maxE+1):
            nva += 1 #increase e
            d = e + f + 21
            nva += 1 #increase d
            for b in range(1, 50-(e+f)):
                nva += 1 #increase b
                for c in range(1, 50-(e+f)-b):
                    nva += 1 #increase c
                    a = (b + c + e + f)
                    nva += 1 #increase f
                    # print(nva)
                    printAll(b, c, d, e, f)
                    if (checkConstraintsA(b, c, d, e, f)):
                        print('Found solution!')
                        return
    # checkConstraintsA(    
    return

def runTest():
    problemA()
    global nva


runTest()
print('nva =', nva)