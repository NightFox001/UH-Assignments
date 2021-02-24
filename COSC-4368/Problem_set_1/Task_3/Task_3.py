import sys
import csv

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

def printAll(B, C, D, E, F):
    print('A =', (B + C + E + F), ', B =', B, ', C =', C, ', D =', D, ', E =', E, ', F =', F)

def getSumBC(D, E, F):

    return ((D**2-417)/E**2-(E+F))  

def aV4():
    # V3 nva = ...
    # print('V4')
    global nva
    maxE = 8
    numSolutions = 0
    firstNVA = 0

    aMin, aMax = 50, 0
    bMin, bMax = 50, 0
    cMin, cMax = 50, 0
    dMin, dMax = 50, 0
    eMin, eMax = 50, 0
    fMin, fMax = 50, 0
    numSolutions = 0

    for e in range(maxE, 0, -1):        # rule H9
        nva += 1 #from assigning value to e
        for f in range(29-e, 0, -1):        # rule H12
            nva += 1 #from assigning value to f

            d = e + f + 21              # rule H2
            nva += 1 #from assigning value to d


            sumBC = getSumBC(d, e, f)   #H11
            if (not sumBC%1==0 or sumBC>(50-e-f)): continue
            nva += 1 #from assigning value to sumBC
            # print('e =', e, 'f =', f, 'sum =', sumBC)
            for b in range(1, 50-e-f): #
                nva += 1 #from assigning value to b
                for c in range(1, 50-e-f-b):
                    nva += 1 #from assigning value to c

                    if (checkConstraintsA(b, c, d, e, f)):
                        if (numSolutions==0): 
                            firstNVA = nva
                            # printAll(b, c, d, e, f)
                        numSolutions += 1

    print('Fist solution found at nva:', firstNVA)
    print('Solutions found:', numSolutions)


def bV1():
    global nva
    maxE = 8
    numSolutions = 0
    firstNVA = 0

    aMin, aMax = 50, 0
    bMin, bMax = 50, 0
    cMin, cMax = 50, 0
    dMin, dMax = 50, 0
    eMin, eMax = 50, 0
    fMin, fMax = 50, 0
    numSolutions = 0

    for e in range(maxE, 0, -1):        # rule H9
        nva += 1 #from assigning value to e
        for f in range(29-e, 0, -1):        # rule H12
            nva += 1 #from assigning value to f

            d = e + f + 21              # rule H2
            nva += 1 #from assigning value to d


            sumBC = getSumBC(d, e, f)   #H11
            if (not sumBC%1==0 or sumBC>100): continue
            nva += 1 #from assigning value to sumBC
            # print('e =', e, 'f =', f, 'sum =', sumBC)
            for b in range(1, 50-e-f): #
                nva += 1 #from assigning value to b
                for c in range(1, 50-e-f-b):
                    nva += 1 #from assigning value to c
                    printAll(b, c, d, e, f)

                    if (checkConstraintsA(b, c, d, e, f)):
                        if (numSolutions==0): 
                            firstNVA = nva
                        numSolutions += 1

    print('Fist solution found at nva:', firstNVA)
    print('Solutions found:', numSolutions)

def problemA():
    print('Starting Problem a...')
    aV4()
    return


def problemB():
    print('Starting Problem b...')
    bV1()

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
        if (usrInput == 'a'):
            problemA()
            validInput = True
        if usrInput == 'b': 
            validInput = True
        if usrInput == 'c': 
            validInput = True
        if usrInput == 'all': 
            findAllSolutions()
            validInput = True
        else: print('\nInvalid input')

# with open('employee_file.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

print('Total possible combitnations =', nva)