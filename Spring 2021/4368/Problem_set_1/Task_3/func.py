from constraints import *

global nva
nva = 0

# View H11 in doc: This function returns the required sum for B+C given E and F
def sumBC(E, F):
    return (((E+F+21)**2-417)/E**2-(E+F))  

 
def aV1():
    # V1 73,000
    minA = 4
    maxA = 50 # 
    maxE = 8 #view rule H9
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
    # V3 nva = 82,507
    print('V3')
    global nva
    maxE = 8
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
                    a = (b + c + e + f) # a ranged(4, 128)... not good
                    nva += 1 #from assigning value to f
                    # printAll(b, c, d, e, f)

                    if (checkConstraintsA(b, c, d, e, f)):
                        printAll(b, c, d, e, f)
                        if numSolutions==0: firstNVA = nva
                        numSolutions += 1


    print('Solutions found:', numSolutions)
    print('Fist solution found at nva:', firstNVA)





def aV4():
    print('using aV4...\n')
    global nva
    maxE = 8
    checks = 0
    firstSolution = 0
    solutions = 0
    

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

                    checks += 1
                    if (checkConstraintsA(b, int(sumBC(e, f))-b, (e + f + 21), e, f)):
                        # print('Solution found on guess #' + str(checks), 'and nva #' +str(nva))
                        if (solutions < 1):
                            firstSolution += 1 
                            print('Solution found!')
                            printAll(b, int(sumBC(e, f))-b, e + f + 21, e, f)
                            print('nva =', nva)
                        solutions += 1
    
    print('\n  ### Extra info from continuing after solution was found ###')
    print('\t Total combinations checked for a solution:', checks)
    print('\t First solution found on check:', firstSolution)
    print('\t Total solutions found:', solutions)
    print('\t Total nva:', nva,'\n')


def aV5():
    print('using aV5...\n')
    global nva
    maxE = 8
    checks = 0
    firstSolution = 0
    solutions = 0
    
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

                checks += 1
                if (checkConstraintsA(b, int(sumBC(e, f))-b, (e + f + 21), e, f)):
                    # print('Solution found on guess #' + str(checks), 'and nva #' +str(nva))
                    if (solutions < 1):
                        firstSolution += 1 
                        print('Solution found!')
                        printAll(b, int(sumBC(e, f))-b, e + f + 21, e, f)
                        print('nva =', nva)
                    solutions += 1

    print('\n  ### Extra info from continuing after solution was found ###')
    print('\t Total combinations checked for a solution:', checks)
    print('\t First solution found on check:', firstSolution)
    print('\t Total solutions found:', solutions)
    print('\t Total nva:', nva,'\n')


def aV6():
    print('using aV6...\n')
    global nva
    maxE = 8
    checks = 0
    firstSolution = 0
    solutions = 0
    

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

                checks += 1
                if (checkConstraintsA(b, int(sumBC(e, f))-b, (e + f + 21), e, f)):
                    if (solutions < 1):
                        firstSolution += 1 
                        print('Solution found!')
                        printAll(b, int(sumBC(e, f))-b, e + f + 21, e, f)
                        print('nva =', nva)
                    solutions += 1

    print('\n  ### Extra info from continuing after solution was found ###')
    print('\t Total combinations checked for a solution:', checks)
    print('\t First solution found on check:', firstSolution)
    print('\t Total solutions found:', solutions)
    print('\t Total nva:', nva,'\n')





def bV1():
    print('using bV1...\n')
    global nva
    maxE = 8
    solutionsForA = 0
    solutionsForB = 0
    checks = 0
    firstSolution = 0

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
                solutionsForA += 1
                # printAll(b, c, e + f + 21, e, f)
                if (checkConstraintsA(b, c, (e + f + 21), e, f)):
                    # print('\nSolution found for 3a constriants')
                    # printAll(b, c, e + f + 21, e, f)
                    solutionsForA += 1
                    
                    for h in range(1, 51):
                        nva += 1
                        for i in range(1, 51):
                            checks += 1
                            if checkConstraintsB(b, c, e+f+21, e, f, 11, h, i, 40): 
                                print('Solution found!')
                                printAllB(b, c, e+f+21, e, f, 11, h, i, 40)
                                print('nva =', nva)
                                if(solutionsForB<1):firstSolution = checks
                                solutionsForB += 1
                                


    print('\n  ### Extra info from continuing after solution was found ###')
    print('\t Total combinations checked for a solution:', checks)
    print('\t First solution found on check:', firstSolution)
    print('\t',solutionsForA, 'Solutions satisfied C1-C4')
    print('\t',solutionsForB, 'Solutions satisfied C1-C9')
    print('\t Total nva:', nva,'\n')





def bV2():
    print('using bV2...\n')
    global nva
    maxE = 8
    solutionsForA = 0
    solutionsForB = 0
    checks = 0
    firstSolution = 0

    for e in range(maxE, 0, -1):                # rule H9
        nva += 1
            # same constraints H13 and H11 from probA 
            # combined with H24 to limit assignments of F
        if (sumBC(e, 20)%1==0 and sumBC(e, 20)<=(49-e-20)):
            f = 20 # c = 2
            nva += 1
        elif (sumBC(e, 7)%1==0 and sumBC(e, 7)<=(49-e-7)):
            f = 7 # c = 3
            nva += 1
        elif (sumBC(e, 3)%1==0 and sumBC(e, 3)<=(49-e-3)):
            f = 3 # c = 4
            nva += 1
        else: # if a solution for these values of f are impossible, go to next e
            continue 

        # Check that the required sum of (B+C) defined by H11  
        if not (checkConstraintsA2(sumBC(e, f), (e + f + 21), e, f)): continue
        for b in range(1, int(sumBC(e, f))):          # From rule H16
            nva += 1 
            c = int(sumBC(e, f))-b    # From rule H1
            nva += 1 
            solutionsForA += 1
            # printAll(b, c, e + f + 21, e, f)
            if (checkConstraintsA(b, c, (e + f + 21), e, f)):
                # print('\nSolution found for 3a constriants')
                # printAll(b, c, e + f + 21, e, f)
                solutionsForA += 1
                
                for h in range(1, 51):
                    nva += 1
                    for i in range(1, 51):
                        nva += 1
                        # g = 11
                        # j = 40
                        # d = e+f+21
                        # printAllB(b, c, e+f+21, e, f, 11, h, i, 40)
                        checks += 1
                        if checkConstraintsB(b, c, e+f+21, e, f, 11, h, i, 40): 
                            if (solutionsForB < 1): 
                                print('Solution found!')
                                printAllB(b, c, e+f+21, e, f, 11, h, i, 40)
                                print('nva =', nva)
                                if(solutionsForB<1):firstSolution = checks
                                solutionsForB += 1

    print('\n  ### Extra info from continuing after solution was found ###')
    print('\t Total combinations checked for a solution:', checks)
    print('\t First solution found on check:', firstSolution)
    print('\t',solutionsForA, 'Solutions satisfied C1-C4')
    print('\t',solutionsForB, 'Solutions satisfied C1-C9')
    print('\t Total nva:', nva,'\n')





def bV3():
    print('using bV3...\n')
    global nva
    maxE = 8
    solutionsForA = 0
    solutionsForB = 0
    checks = 0
    firstSolution = 0

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
        if (checkConstraintsA(b, c, (e + f + 21), e, f)): solutionsForA += 1
        for h in range(1, 51):
            nva += 1
            for i in range(1, 51):
                nva += 1
                # g = 11
                # j = 40
                # d = e+f+21
                checks += 1
                if checkConstraintsB(b, c, e+f+21, e, f, 11, h, i, 40): 
                    if (solutionsForB < 1): 
                        print('Solution found!')
                        printAllB(b, c, e+f+21, e, f, 11, h, i, 40)
                        print('nva =', nva)
                        firstSolution = checks
                    solutionsForB += 1

    print('\n  ### Extra info from continuing after solution was found ###')
    print('\t Total combinations checked for a solution:', checks)
    print('\t First solution found on check:', firstSolution)
    print('\t',solutionsForA, 'Solutions satisfied C1-C4')
    print('\t',solutionsForB, 'Solutions satisfied C1-C9')
    print('\t Total nva:', nva,'\n')





def bV4():
    print('using bV4...\n')
    global nva
    maxE = 8
    solutionsForA = 0
    solutionsForB = 0
    checks = 0
    firstSolution = 0

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
            
        for h in range(1, f): # From rule H23
            nva += 1
            i = int( (f-h)**(1/3) + 11 ) # from rule H23
            nva += 1
            checks += 1
            if checkConstraintsB(b, c, e+f+21, e, f, 11, h, i, 40): 
                if (solutionsForB < 1): 
                    print('Solution found!')
                    printAllB(b, c, e+f+21, e, f, 11, h, i, 40)
                    print('nva =', nva)
                    firstSolution = checks
                solutionsForB += 1

    print('\n  ### Extra info from continuing after solution was found ###')
    print('\t Total combinations checked for a solution:', checks)
    print('\t First solution found on check:', firstSolution)
    print('\t',solutionsForA, 'Solutions satisfied C1-C4')
    print('\t',solutionsForB, 'Solutions satisfied C1-C9')
    print('\t Total nva:', nva,'\n')





def bV5():
    print('using bV5...\n')
    global nva
    maxE = 8
    solutionsForA = 0
    solutionsForB = 0
    checks = 0
    firstSolution = 0

    for e in range(maxE, 0, -1):                # rule H9
        nva += 1 #from assigning value to e
        for f in range(29-e, 0, -1):            # rule H12
            nva += 1 #from assigning value to f

            # Don't don't assign d, b, or c orvalues if rules H13 or H11 are broken
            if (not sumBC(e, f)%1==0 or sumBC(e, f)>(49-e-f)): continue

            # Check that the required sum of (B+C) defined by H11  
            if not (checkConstraintsA2(sumBC(e, f), (e + f + 21), e, f)): continue
            for c in range(2, 5):          # From rule H16
                nva += 1 #from assigning value to b
                b = int(sumBC(e, f))-c    # From rule H1
                nva += 1 #from assigning value to c
        
                
                if (checkConstraintsA(b, c, (e + f + 21), e, f)): solutionsForA += 1
                    
                for h in range(1, f): # From rule H23
                    nva += 1
                    i = int( (f-h)**(1/3) + 11 ) # from rule H23
                    nva += 1
                    checks += 1
                    if checkConstraintsB(b, c, e+f+21, e, f, 11, h, i, 40): 
                        if (solutionsForB < 1): 
                            print('Solution found!')
                            printAllB(b, c, e+f+21, e, f, 11, h, i, 40)
                            print('nva =', nva)
                            firstSolution = checks
                        solutionsForB += 1


    print('\n  ### Extra info from continuing after solution was found ###')
    print('\t Total combinations checked for a solution:', checks)
    print('\t First solution found on check:', firstSolution)
    print('\t',solutionsForA, 'Solutions satisfied C1-C4')
    print('\t',solutionsForB, 'Solutions satisfied C1-C9')
    print('\t Total nva:', nva,'\n')





def cV1():
    print('using cV1...\n')
    global nva
    maxE = 8
    solutionsForA = 0
    solutionsForB = 0
    solutionsForC = 0
    firstSolution = 0
    checks = 0
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
            
        for h in range(1, f):
            nva += 1
            i = int( (f-h)**(1/3) + 11 ) # from rule H24
            nva += 1
            if checkConstraintsB(b, c, e+f+21, e, f, 11, h, i, 40):
                solutionsForB += 1
                for k in range(4, 11, 2): # From H30 and H31
                    nva += 1
                    for l in range(1, 51): 
                        nva += 1
                        for m in range(1, 51): # From H31
                            nva += 1
                            for n in range(1, 52):
                                nva += 1
                                for o in range(1, 51): 
                                    nva += 1
                                    checks += 1
                                    if checkConstraintsC(b, c, (e+f+21), e, f, 11, h, i, 40, k, l, m, n, o):
                                        print('found c solution:', solutionsForC)
                                        if(solutionsForC<1):firstSolution = checks
                                        solutionsForC += 1


    # print('\n\nFirst solution found on guess #' + str(firstGuess), 'and with nva =', firstNVA)
    print('\n### Extra info from continuing after solution was found ###')
    print(solutionsForA, 'Solutions satisfied C1-C4')
    print(solutionsForB, 'Solutions satisfied C1-C9')
    print(solutionsForC, 'Solutions satisfied C1-C15')
    # print('Total solutions found:', solutionsForC)
    print('Total nva:', nva)





def cV2():
    print('using cV2...\n')
    global nva
    maxE = 8
    checks = 0
    firstSolution = 0
    solutionsForA = 0
    solutionsForB = 0
    solutionsForC = 0
    solutions = 0
    

    for e in range(maxE, 0, -1):                # rule H9
        nva += 1 #from assigning value to e
        for f in range(29-e, 0, -1):            # rule H12
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
                    
                for h in range(1, f):
                    nva += 1
                    i = int( (f-h)**(1/3) + 11 ) # from rule H24
                    nva += 1
                    if checkConstraintsB(b, c, e+f+21, e, f, 11, h, i, 40):
                        solutionsForB += 1
                        for k in range(4, 11, 2): # From H30 and H31
                            nva += 1
                            m = (k**2-6)/2 # From H31
                            nva += 1
                            o = k**2 -m -10 # From H32
                            nva += 1
                            for l in range(1, 51): 
                                nva += 1
                                for n in range(1, 52):
                                    nva += 1
                                    checks += 1
                                    if checkConstraintsC(b, c, (e+f+21), e, f, 11, h, i, 40, k, l, m, n, o):
                                        if (solutionsForC<1): firstSolution = checks
                                        solutionsForC += 1
                                        printAllC(b, c, e+f+21, e, f, 11, h, i, 40, k, l, n, m, o)
                                        print('nva =', nva)






def cV3():
    print('using cV3...\n')
    global nva
    maxE = 8
    checks = 0
    firstSolution = 0
    solutionsForA = 0
    solutionsForB = 0
    solutionsForC = 0
    solutions = 0
    

    for e in range(maxE, 0, -1):                # rule H9
        nva += 1
            # same constraints H13 and H11 from probA but combined with H24
            # only assign a value to F and C if it possible a solution to exist with that value
            # note: Ik this looks hardcoded but its not due to constraint H24 
        if (sumBC(e, 20)%1==0 and sumBC(e, 20)<=(49-e-20)):
            # Check that the required sum of (B+C) for 20 is valid before assigning
            if not (checkConstraintsA2(sumBC(e, 20), (e + 20 + 21), e, 20)): continue
            f = 20  
            c = 2  #from rule H24
            nva += 2
        elif (sumBC(e, 7)%1==0 and sumBC(e, 7)<=(49-e-7)):
            if not (checkConstraintsA2(sumBC(e, 7), (e + 7 + 21), e, 7)): continue
            f = 7   
            c = 3  # from rule H24
            nva += 2
        elif (sumBC(e, 3)%1==0 and sumBC(e, 3)<=(49-e-3)):
            if not (checkConstraintsA2(sumBC(e, 3), (e + 3 + 21), e, 3)): continue
            f = 3  
            c = 4 # from rule H24
            nva += 2
        else: continue # if a solution for these values of f are impossible, go to next e

        
        b = int(sumBC(e, f))-c    # From rule H1
        nva += 1 
        
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
                            if (solutionsForC<1): firstSolution = checks
                            solutionsForC += 1
                            printAllC(b, c, e+f+21, e, f, 11, h, i, 40, k, l, n, m, o)
                            print('nva =', nva)


    # print('\n\nFirst solution found on guess #' + str(firstGuess), 'and with nva =', firstNVA)
    print('\n  ### Extra info from continuing after solution was found ###')
    print('\t Total combinations checked for a solution:', checks)
    print('\t First solution found on check:', firstSolution)
    print('\t',solutionsForA, 'Solutions satisfied C1-C4')
    print('\t',solutionsForB, 'Solutions satisfied C1-C9')
    print('\t',solutionsForC, 'Solutions satisfied C1-C15')
    print('\t Total nva:', nva,'\n')