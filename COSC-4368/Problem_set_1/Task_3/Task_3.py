import sys
import csv

from func import *

global nva
nva = 0

# View H11 in doc: This function returns the required sum for B+C given E and F
def sumBC(E, F):
    return (((E+F+21)**2-417)/E**2-(E+F))  

def bV4():
    print('using bV4...\n')
    global nva
    maxE = 8
    solutionsForA = 0
    solutionsForB = 0
    firstGuess = 0
    solutions = 0
    firstNVA = 0

    for e in range(maxE, 0, -1):                # rule H9
        nva += 1
            # same constraints H13 and H11 from probA 
            # combined with H24 to limit assignments of F
        if (sumBC(e, 20)%1==0 and sumBC(e, 20)<=(49-e-20)):
            # Check that the required sum of (B+C) for 20 is valid before assigning
            # note that this is not hardcoded due to constraint H24 
            if not (checkConstraintsA2(sumBC(e, 20), (e + 20 + 21), e, 20)): continue
            f = 20  
            c = 2  #from rule H24
            nva += 2
        elif (sumBC(e, 7)%1==0 and sumBC(e, 7)<=(49-e-7)):
            # Check that the required sum of (B+C) for 20 is valid before assigning
            # note that this is not hardcoded due to constraint H24 
            if not (checkConstraintsA2(sumBC(e, 7), (e + 7 + 21), e, 7)): continue
            f = 7   
            c = 3  # from rule H24
            nva += 2
        elif (sumBC(e, 3)%1==0 and sumBC(e, 3)<=(49-e-3)):
            # Check that the required sum of (B+C) for 20 is valid before assigning
            # note that this is not hardcoded due to constraint H24 
            if not (checkConstraintsA2(sumBC(e, 3), (e + 3 + 21), e, 3)): continue
            f = 3  
            c = 4 # from rule H24
            nva += 2
        else: continue # if a solution for these values of f are impossible, go to next e

        
        b = int(sumBC(e, f))-c    # From rule H1
        nva += 1 
        
        # printAll(b, c, e + f + 21, e, f)
        if (checkConstraintsA(b, c, (e + f + 21), e, f)): solutionsForA += 1
            
        for h in range(1, 51):
            nva += 1

            i = int( (f-h)**(1/3) + 11 ) # from rule H24
            nva += 1

            # g = 11
            # j = 40
            # d = e+f+21
            if checkConstraintsB(b, c, e+f+21, e, f, 11, h, i, 40): 
                if (solutionsForB < 1): print('First solution found nva =', nva)
                printAllB(b, c, e+f+21, e, f, 11, h, i, 40)
                solutionsForB += 1
                # solutions += 1

    # print('\n\nFirst solution found on guess #' + str(firstGuess), 'and with nva =', firstNVA)
    print(solutionsForA, 'Solutions satisfied C1-C4')
    print(solutionsForB, 'Solutions satisfied C5-C9')
    # print(solutions, 'Solutions found')
    print('Total nva:', nva)

    
def problemA():
    print('Starting Problem a...')
    aV5()
    return

def problemB():
    print('Starting Problem b...')
    bV4()

def runTest():

    #val from johnny
    # print(checkConstraintsB(1,2,49,8,20,11,12,13,40))

    print(checkConstraintsB(1, 2, 49, 8, 20, 11, 12, 13, 40))


print('\n'*50)
if len(sys.argv) > 1:
    print('Starting test...')
    if sys.argv[1] == 'aV4': aV4()
    elif sys.argv[1] == 'aV5': aV5()
    elif sys.argv[1] == 'aV6': aV6()
    elif sys.argv[1] == 'bV1': bV1()
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