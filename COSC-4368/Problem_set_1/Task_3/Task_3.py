import sys
import csv

from test.test_importlib.data03 import namespace

global nva
nva = 0

def C1(B, C, E, F):
    if ((B + C + E + F) < 51):
        return True
    return False

def C1_v2(sumBC, E, F):
    if ((sumBC + E + F) < 51):
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

def C3_v2(sumBC, D, E, F):
    if (D**2 == (E**2 * (sumBC + E + F) + 417)):
        return True
    return False

def checkConstraintsA(B, C, D, E, F):
    # print('checking with values: ', end='')
    # printAll(B, C, D, E, F)
    if (C1(B, C, E, F) and C2(D, E, F) and C3(B, C, D, E, F)):
        return True
    return False

def checkConstraintsA2(sumBC, D, E, F):
    # print('checking with values: ', end='')
    # printAll(B, C, D, E, F)
    if (C1_v2(sumBC, E, F) and C2(D, E, F) and C3_v2(sumBC, D, E, F)):
        return True
    return False

def printAll(B, C, D, E, F):
    print('A =', (B + C + E + F), ', B =', B, ', C =', C, ', D =', D, ', E =', E, ', F =', F)

# View H11 in doc: This function returns the required sum for B+C given E and F
def sumBC(E, F):
    return (((E+F+21)**2-417)/E**2-(E+F))  

def aV4():
    global nva
    maxE = 8
    guesses = 0
    solutions = 0
    firstNVA = 0


    for e in range(maxE, 0, -1):                # rule H9
        nva += 1 #from assigning value to e
        for f in range(29-e, 0, -1):            # rule H12
            nva += 1 #from assigning value to f

            # Don't don't assign d, b, or c values if rules H13 or H11 are broken
            if (not sumBC(e, f)%1==0 or sumBC(e, f)>(50-e-f)): continue #H11

            d = e + f + 21                      # rule H2
            nva += 1 #from assigning value to d

            for b in range(1, 50-e-f):          # From rule H1 
                nva += 1 #from assigning value to b
                for c in range(1, 50-e-f-b):    # From rule H1
                    nva += 1 #from assigning value to c
                    guesses += 1
                    if (checkConstraintsA(b, c, d, e, f)):
                        print('Solution found on guess #' + str(guesses), 'and nva #' +str(nva))
                        solutions += 1
                        if firstNVA == 0: firstNVA = nva
    print('Fist solution found at nva:', firstNVA)

def aV5():
    print('using aV5...\n')
    global nva
    maxE = 8
    guesses = 0
    firstGuess = 0
    solutions = 0
    firstNVA = 0

    for e in range(maxE, 0, -1):                # rule H9
        nva += 1 #from assigning value to e
        for f in range(29-e, 0, -1):            # rule H12
            nva += 1 #from assigning value to f

            # Don't don't assign d, b, or c values if rules H13 or H11 are broken
            if (not sumBC(e, f)%1==0 or sumBC(e, f)>(49-e-f)): continue

            # Check that the required sum of (B+C) defined by H11  
            if not (checkConstraintsA2(sumBC(e, f), (e + f + 21), e, f)): continue
            for b in range(1, int(sumBC(e, f))):          # From rule H16
                nva += 1 #from assigning value to b
                c = int(sumBC(e, f))-b    # From rule H1
                nva += 1 #from assigning value to c
                guesses += 1
                # printAll(b, c, e + f + 21, e, f)
                if (checkConstraintsA(b, c, (e + f + 21), e, f)):
                    # print('Solution found on guess #' + str(guesses), 'and nva #' +str(nva))
                    if (solutions < 1): 
                        firstNVA = int(nva) 
                        firstGuess = guesses
                    solutions += 1

    print('First solution found on guess #' + str(firstGuess), 'and with nva =', firstNVA)
    print(guesses, 'Combinations checked')
    print(solutions, 'Solutions found')

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

            sumBC = sumBC(d, e, f)   #H11
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


if len(sys.argv) > 1:
    print('\n'*50 + 'Starting test...')
    if sys.argv[1] == 'aV4': aV4()
    elif sys.argv[1] == 'aV5': aV5()
    else: runTest()
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
            # findAllSolutions()
            validInput = True
        else: print('\nInvalid input')

# with open('employee_file.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

# print('Total possible combitnations =', nva)
print('Total NVA =', nva, '\n\n')