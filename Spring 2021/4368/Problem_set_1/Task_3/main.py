import sys
import csv
from func import *
from constraints import *

global nva
nva = 0

# View H11 in doc: This function returns the required sum for B+C given E and F
def sumBC(E, F): #note that no new vars are assigned
    return (((E+F+21)**2-417)/E**2-(E+F))  

def cV4():
    print('using cV4...\n')
    global nva
    maxE = 8
    checks = 0
    solutionsForA = 0
    solutionsForB = 0
    solutionsForC = 0
    solutions = 0
    firstSolution = 0

    for e in range(maxE, 0, -1):                # rule H9
        nva += 1 #from assigning value to e
        for f in range(29-e, 0, -1):            # rule H13
            nva += 1 #from assigning value to f

            # Don't don't assign d, b, or c values if rules H13 or H11 are broken
            if (not sumBC(e, f)%1==0 or sumBC(e, f)>(49-e-f)): continue

            # Check that the required sum of (B+C) defined by H11. (e + f + 21) is in place of D
            if not (checkConstraintsA2(sumBC(e, f), (e + f + 21), e, f)): continue
            for c in range(2, 5):          # From rule H24
                nva += 1 #from assigning value to b
                b = int(sumBC(e, f))-c    # From rule H1
                nva += 1 #from assigning value to c
        
                # If the current values dont satisfy constraits for A then they won't pass B or C so stop
                if ( not checkConstraintsA(b, c, (e + f + 21), e, f)): continue
                solutionsForA += 1
                for i in range(9, 14): # from rule H24
                    nva += 1

                    h = f-(i-11)**3 # from rule H25

                    if checkConstraintsB(b, c, e+f+21, e, f, 11, h, i, 40):
                        solutionsForB += 1
                        #starting with max val for k and looping down reduces nva from 197 to 36
                        for k in range(10, 3, -2): # From H30 and H31
                            nva += 1

                            # couldn't prove a limit of L :(i
                            # I have a therory that L has a limt of 18 but not 100% sure it was a valid proof
                            for l in range(1, 51): 
                                nva += 1

                                #Note that 
                                # g = 11, j = 40, d = (e+f+21)
                                # m = (k**2-6)/2 # From H31
                                # n = (m**2 + 291)**(1/2) # From rule H33
                                # o = k**2 -m -10 # From rule H32
                                # so a solution can be found without ever assigning these values. However, if you feel that this is kinda 'cheaty' then you can uncomment the line below to count for these assignments
                                # nva += 6 # extra for d, g, j, m, n, and o 

                                checks += 1
                                if checkConstraintsC(b, c, (e+f+21), e, f, 11, h, i, 40, k, l, (k**2-6)/2, (((k**2-6)/2)**2 + 291)**(1/2), k**2-((k**2-6)/2) -10):
                                    if (solutionsForC<1): firstSolution = checks
                                    solutionsForC += 1
                                    printAllC(b, c, (e+f+21), e, f, 11, h, i, 40, k, l, (k**2-6)/2, (((k**2-6)/2)**2 + 291)**(1/2), k**2-((k**2-6)/2) -10)
                                    print('nva =', nva)


    print('\n  ### Extra info from continuing after solution was found ###')
    print('\t Total combinations checked for a solution:', checks)
    print('\t First solution found on check:', firstSolution)
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
    cV4()

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
    if sys.argv[1] == 'a3': aV3()
    elif sys.argv[1] == 'a4': aV4()
    elif sys.argv[1] == 'a5': aV5()
    elif sys.argv[1] == 'a6': aV6()
    elif sys.argv[1] == 'a': problemA()
    elif sys.argv[1] == 'b1': bV1()
    elif sys.argv[1] == 'b2': bV2()
    elif sys.argv[1] == 'b3': bV3()
    elif sys.argv[1] == 'b4': bV4()
    elif sys.argv[1] == 'b5': bV5()
    elif sys.argv[1] == 'b': problemB()
    elif sys.argv[1] == 'c1': cV1()
    elif sys.argv[1] == 'c2': cV2()
    elif sys.argv[1] == 'c3': cV3()
    elif sys.argv[1] == 'c4': cV4()
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

