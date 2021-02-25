import sys
import csv

from func import *

global nva
nva = 0

def C10(k, m):
    if (2*m == k**2 -6): return True
    return False
def C11(f, i, n, o):
    if ((n-o)**3 +7 == (f-i)*n): return True
    return False
def C12(m, n):
    if (n**2 == m**2 +291): return True
    return False
def C13(b, g, h, i, o):
    if (o**2 == g*h*i*b + 133): return True
    return False
def C14(k, m, o):
    if (m + o == k**2 -10): return True
    return False
def C15(b, i, k, l):
    if (l**3 + i == (l+b)*k): return True
    return False    

def checkConstraintsC(b, c, d, e, f, g, h, i, j, k, l, m, n, o):
    # print('\nTesting C5-C9 with values:\nA =', (b + c + e + f), ', B =', b, ', C =', c, ', D =', d, ', E =', e, ', F =', f, ', G =', g, ', H =', h, ', I =', i, ', J =', j, ', M =', m, ', N =', n, '\n')
    if C10(k, m) and C11(f, i, n, o) and C12(m, n) and C13(b, g, h, i, o) and C14(k, m, o) and C15(b, i, k, l): return True
    return False

# View H11 in doc: This function returns the required sum for B+C given E and F
def sumBC(E, F):
    return (((E+F+21)**2-417)/E**2-(E+F))  

def cV3():
    print('using cV3...\n')
    global nva
    maxE = 8
    checks = 0
    solutionsForA = 0
    solutionsForB = 0
    solutionsForC = 0
    solutions = 0

    for e in range(maxE, 0, -1):                # rule H9
        nva += 1 #from assigning value to e
        for f in range(29-e, 0, -1):            # rule H13
            nva += 1 #from assigning value to f

            # Don't don't assign d, b, or c orvalues if rules H13 or H11 are broken
            if (not sumBC(e, f)%1==0 or sumBC(e, f)>(49-e-f)): continue

            # Check that the required sum of (B+C) defined by H11  
            if not (checkConstraintsA2(sumBC(e, f), (e + f + 21), e, f)): continue
            for c in range(2, 5):          # From rule H16
                nva += 1 #from assigning value to b
                b = int(sumBC(e, f))-c    # From rule H1
                nva += 1 #from assigning value to c
        
                # printAll(b, c, e + f + 21, e, f)
                if (checkConstraintsA(b, c, (e + f + 21), e, f)): solutionsForA += 1
                    
                for h in range(1, f):# from rule H23
                    nva += 1
                    i = int( (f-h)**(1/3) + 11 ) # from rule H23
                    nva += 1
                    if checkConstraintsB(b, c, e+f+21, e, f, 11, h, i, 40):
                        solutionsForB += 1
                        for k in range(4, 11, 2): # From H30 and H31
                            nva += 1
                            m = (k**2-6)/2 # From H31
                            nva += 1
                            o = k**2 -m -10 
                            nva += 1
                            n = (m**2 + 291)**(1/2)
                            nva += 1
                            for l in range(1, 51): 
                                nva += 1
                                checks += 1
                                if checkConstraintsC(b, c, (e+f+21), e, f, 11, h, i, 40, k, l, m, n, o):
                                    solutionsForC += 1
                                    printAllC(b, c, e+f+21, e, f, 11, h, i, 40, k, l, n, m, o)
                                    print('nva =', nva)


    # print('\n\nFirst solution found on guess #' + str(firstGuess), 'and with nva =', firstNVA)
    print('\n  ### Extra info from continuing after solution was found ###')
    print('\t Total combinations checked for a solution:', checks)
    print('\t',solutionsForA, 'Solutions satisfied C1-C4')
    print('\t',solutionsForB, 'Solutions satisfied C1-C9')
    print('\t',solutionsForC, 'Solutions satisfied C1-C15')
    print('\t Total nva:', nva,'\n')

    
def problemA():
    print('Starting Problem a...')
    aV6()
    return

def problemB():
    print('Starting Problem b...')
    bV4()

def problemC():
    print('Starting Problem c...')
    cV3()

def runTest():
    # print(checkConstraintsB(1, 2, 49, 8, 20, 11, 12, 13, 40))
    for m in range(1, 51):
        for n in range(1, 51):
            if C12(m, n): 
                print(m, n)
                return


print('\n'*50)
if len(sys.argv) > 1:
    print('Starting test...')
    if sys.argv[1] == 'aV4': aV4()
    elif sys.argv[1] == 'aV5': aV5()
    elif sys.argv[1] == 'aV6': aV6()
    elif sys.argv[1] == 'a': problemA()
    elif sys.argv[1] == 'bV1': bV1()
    elif sys.argv[1] == 'bV2': bV2()
    elif sys.argv[1] == 'bV3': bV3()
    elif sys.argv[1] == 'bV4': bV4()
    elif sys.argv[1] == 'bV5': bV5()
    elif sys.argv[1] == 'b': problemB()
    elif sys.argv[1] == 'c1': cV1()
    elif sys.argv[1] == 'c': problemC()
    else: runTest()
else:
    validInput = False
    while(not validInput):
        usrInput = input("Enter problem to solve ('a', 'b', 'c'):\n")
        if (usrInput == 'a'):
            validInput = True
            problemA()
        elif usrInput == 'b': 
            validInput = True
            problemB()
        elif usrInput == 'c': 
            validInput = True
            problemC()
        elif usrInput == 'test': 
            runTest()
            validInput = True
        else: print('\nInvalid input')

# with open('employee_file.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

# print('Total possible combitnations =', nva)
# print('Total NVA =', nva, '\n\n')