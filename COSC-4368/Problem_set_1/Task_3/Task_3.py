import sys
from test.test_importlib.data03 import namespace

global nva
nva = 0

def C1(B, C, E, F):
    if ((B + C + E + F) < 51):
        return True
    return False

def C2(D, E, F):
    if (D == (E + F + 21)):
        return True
    return False

def C3(B, C, D, E, F):
    if (D**2 == (E**2 * (B + C + E + F) + 417)):
        return True
    return False



def checkConstraintsA(B, C, D, E, F):
    if (C1(B, C, E, F) and C2(D, E, F) and C3(B, C, D, E, F)):
        return True
    return False

def findAllSolutions():
    global nva
    numSolutions = 0
    maxE = 50

    aMin = 50
    bMin = 50
    cMin = 50
    dMin = 50
    eMin = 50
    fMin = 50
    aMax = 0
    bMax = 0
    cMax = 0
    dMax = 0
    eMax = 0
    fMax = 0

    for b in range(1, 51):
        nva += 1 #from assigning value to b
        for c in range(1, 51):
            nva += 1 #from assigning value to c
            for e in range(1, maxE+1):
                nva += 1 #from assigning value to e
                for f in range(1, 51):
                    nva += 1 #from assigning value to f
                    d = e + f + 21
                    nva += 1 #from assigning value to d
                    a = (b + c + e + f)
                    nva += 1 #from assigning value to a
                    if (checkConstraintsA(b, c, d, e, f)):
                        numSolutions += 1
                        if (a < aMin): aMin = a
                        if (a > aMax): aMax = a
                        if (b < bMin): bMin = b
                        if (b > bMax): bMax = b
                        if (c < cMin): cMin = c
                        if (c > cMax): cMax = c
                        if (d < dMin): dMin = d
                        if (d > dMax): dMax = d
                        if (e < eMin): eMin = e
                        if (e > eMax): eMax = e
                        if (f < fMin): fMin = f
                        if (f > fMax): fMax = f


    print('Solutions found:', numSolutions)
    print(aMin, '< a <', aMax)
    print(bMin, '< b <', bMax)
    print(cMin, '< c <', cMax)
    print(dMin, '< d <', dMax)
    print(eMin, '< e <', eMax)
    print(fMin, '< f <', fMax)
    

def aV1():
    # V1 73,000
    minA = 4
    maxA = 50 # 
    maxE = 8
    for f in range(1, 29):
        nva += 1 #from assigning value to f
        for e in range(1, maxE+1):
            nva += 1 #from assigning value to e
            d = e + f + 21
            nva += 1 #from assigning value to d
            for b in range(1, 50-(e+f)):
                nva += 1 #from assigning value to b
                for c in range(1, 50-(e+f)-b):
                    nva += 1 #from assigning value to c
                    a = (b + c + e + f)
                    nva += 1 #from assigning value to a
                    # print(nva)
                    printAll(a, b, c, d, e, f)
                    if (checkConstraintsA(a, b, c, d, e, f)):
                        print('Found solution!')
                        return

def aV2():
    # V2 nva = 452
    # make b and c min possible values
    global nva
    maxE = 8
    b = 1
    nva += 1 #from assigning value to b
    c = 1
    nva += 1 #from assigning value to c
    for f in range(1, 29):
        nva += 1 #from assigning value to f
        for e in range(1, maxE+1):
            nva += 1 #from assigning value to e
            d = e + f + 21
            nva += 1 #from assigning value to d
            a = (b + c + e + f)
            nva += 1 #from assigning value to f
            # print(nva)
            printAll(b, c, d, e, f)
            if (checkConstraintsA(b, c, d, e, f)):
                return

def aV3():
    # V3 nva = 452
    print('V3')
    global nva
    maxE = 8
    aMin, aMax = 50, 0
    bMin, bMax = 50, 0
    cMin, cMax = 50, 0
    dMin, dMax = 50, 0
    eMin, eMax = 50, 0
    fMin, fMax = 50, 0
    numSolutions = 0
    firstNVA = 0

    for e in range(maxE, 0, -1):
        nva += 1 #from assigning value to e
        for f in range(1, 30-e):
            nva += 1 #from assigning value to f
            d = e + f + 21
            nva += 1 #from assigning value to d
            for b in range(1, 50):
                nva += 1 #from assigning value to b
                for c in range(1, 50):
                    nva += 1 #from assigning value to c
                    a = (b + c + e + f)
                    nva += 1 #from assigning value to f
                    # printAll(b, c, d, e, f)

                    if (checkConstraintsA(b, c, d, e, f)):
                        printAll(b, c, d, e, f)
                        if numSolutions==0: firstNVA = nva
                        numSolutions += 1
                        if (a < aMin): aMin = a
                        if (a > aMax): aMax = a
                        if (b < bMin): bMin = b
                        if (b > bMax): bMax = b
                        if (c < cMin): cMin = c
                        if (c > cMax): cMax = c
                        if (d < dMin): dMin = d
                        if (d > dMax): dMax = d
                        if (e < eMin): eMin = e
                        if (e > eMax): eMax = e
                        if (f < fMin): fMin = f
                        if (f > fMax): fMax = f

    print('Solutions found:', numSolutions)
    print('Fist solution found at nva:', firstNVA)
    print(aMin, '< a <', aMax)
    print(bMin, '< b <', bMax)
    print(cMin, '< c <', cMax)
    print(dMin, '< d <', dMax)
    print(eMin, '< e <', eMax)
    print(fMin, '< f <', fMax)


def printAll(B, C, D, E, F):
    print('A =', (B + C + E + F), ', B =', B, ', C =', C, ', D =', D, ', E =', E, ', F =', F)
    

def problemA():
    print('Problem a')
    global nva
    maxB = 29
    maxE = 8
    aV3()
    return

def runTest():
    problemA()
    global nva


if len(sys.argv) > 1 and sys.argv[1] == 'test':
    print('\n\nStarting test...')
    runTest()
else:
    validInput = False
    while(not validInput):
        usrInput = input("Enter problem to solve ('a', 'b', 'c'):\n")
        if (usrInput == 'a' or usrInput == 'b' or usrInput == 'c'): validInput = True
        else: print('\nInvalid input')

print('nva =', nva)