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

def C5(e, g, h, i, j):
    if h*j + e*12 == (g+i)**2: return True
    # print('C5 failed')
    return False

def C6(b, c, d, e, g, f):
    if (b+c+e+f) + d == (f-g)**2 - 1: return True
    # print('C6 failed')
    return False

def C7(g, j):
    if 4*j==g**2+39: return True
    # print('C7 failed')
    return False

def C8(f, h, g, i):
    if (i-g)**9==(f-h)**3 : return True
    # print('C8 failed...  if (i-g)**9==(f-h)**3 : return True')
    # print('('+str(i)+'-'+str(g)+')**9 =', (i-g)**8, 'and ('+str(f)+'-'+str(h)+')**3 =', (f-h)**3)
    return False

def C9(c, f, g):
    if (g-c)**2== f*c*c +1 : return True
    # print('C9 failed... (g-c)**2 =', (g-c)**2, 'and f*c*c +1 =', f*c*c +1)
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

def checkConstraintsB(b, c, d, e, f, g, h, i, j):
    # print('\nTesting C5-C9 with values:\nA =', (b + c + e + f), ', B =', b, ', C =', c, ', D =', d, ', E =', e, ', F =', f, ', G =', g, ', H =', h, ', I =', i, ', J =', j, '\n')
    if C5(e, g, h, i, j) and C6(b, c, d, e, g, f) and C7(g, j) and C8(f, h, g, i,) and C9(c, f, g): return True
    return False

def printAll(B, C, D, E, F):
    print('A =', (B + C + E + F), ', B =', B, ', C =', C, ', D =', D, ', E =', E, ', F =', F)

def printAllB(b, c, d, e, f, g, h, i, j):
    print('A =', (b + c + e + f), ', B =', b, ', C =', c, ', D =', d, ', E =', e, ', F =', f, ', G =', g, ', H =', h, ', I =', i, ', J =', j, '\n')

# View H11 in doc: This function returns the required sum for B+C given E and F
def sumBC(E, F):
    return (((E+F+21)**2-417)/E**2-(E+F))  


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
    # V3 nva = 82,507
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
                    a = (b + c + e + f) # a ranged(4, 128)... not good
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

def aV4():
    # V3 nva = ...
    print('V4')
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

    for e in range(maxE, 0, -1): # 
        nva += 1 #from assigning value to e
        for f in range(29-e, 0, -1):
            nva += 1 #from assigning value to f
            d = e + f + 21
            nva += 1 #from assigning value to d
            for b in range(1, 50-e-f):
                nva += 1 #from assigning value to b
                for c in range(1, 50-e-f-b):
                    nva += 1 #from assigning value to c

                    if (checkConstraintsA(b, c, d, e, f)):
                        if (numSolutions==0): firstNVA = nva
                        # printAll(b, c, d, e, f)
                        numSolutions += 1

                        if ((b + c + e + f) < aMin): aMin = (b + c + e + f)
                        if ((b + c + e + f) > aMax): aMax = (b + c + e + f)
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
                        return

    print('Solutions found:', numSolutions)
    print('Fist solution found at nva:', firstNVA)
    print(aMin, '< a <', aMax)
    print(bMin, '< b <', bMax)
    print(cMin, '< c <', cMax)
    print(dMin, '< d <', dMax)
    print(eMin, '< e <', eMax)
    print(fMin, '< f <', fMax)

def aV4():
    print('using aV4...\n')
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
                        if solutions < 1 : 
                            print('first solution found on guess #' + str(guesses), 'and nva #' +str(nva))
                            firstNVA = nva
                        # printAll(b, c, d, e, f)
                        solutions += 1
    
    print('\nTotal solutions found:', solutions)
    print('Total nva:', nva)


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
                if (checkConstraintsA(b, c, (e + f + 21), e, f)):
                    # print('Solution found on guess #' + str(guesses), 'and nva #' +str(nva))
                    if (solutions < 1): 
                        print('First solution found!')
                        printAll(b, c, e + f + 21, e, f)
                        print('nva =', nva)
                        firstNVA = int(nva) 
                        firstGuess = guesses
                    solutions += 1
    print('\n\nFirst solution found on guess #' + str(firstGuess), 'and with nva =', firstNVA)
    print(guesses, 'Combinations checked')
    print('\nTotal solutions found:', solutions)
    print('Total nva:', nva)


def aV6():
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
                guesses += 1
                # Use int(sumBC(e, f))-b inplace of C From rule H1
                if (checkConstraintsA(b, int(sumBC(e, f))-b, (e + f + 21), e, f)):
                    # print('Solution found on guess #' + str(guesses), 'and nva #' +str(nva))
                    if (solutions < 1): 
                        print('First solution found!')
                        printAll(b, int(sumBC(e, f))-b, e + f + 21, e, f)
                        print('nva =', nva)
                        firstNVA = int(nva) 
                        firstGuess = guesses
                    solutions += 1

    print('\nTotal solutions found:', solutions)
    print('Total nva:', nva)


def bV1():
    print('using bV1...\n')
    global nva
    maxE = 8
    solutionsForA = 0
    solutionsForB = 0
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

                        if checkConstraintsB(b, c, e+f+21, e, f, 11, h, i, 40): 
                            # print('found b')
                            printAllB(b, c, e+f+21, e, f, 11, h, i, 40)
                            solutionsForB += 1
                            # solutions += 1


    # print('\n\nFirst solution found on guess #' + str(firstGuess), 'and with nva =', firstNVA)
    print(solutionsForA, 'Solutions satisfied C1-C4')
    print(solutionsForB, 'Solutions satisfied C5-C9')
    # print(solutions, 'Solutions found')
    print('Total nva:', nva)

def bV2():
    print('using bV2...\n')
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
                    if checkConstraintsB(b, c, e+f+21, e, f, 11, h, i, 40): 
                        # print('found b')
                        printAllB(b, c, e+f+21, e, f, 11, h, i, 40)
                        solutionsForB += 1
                        # solutions += 1

    # print('\n\nFirst solution found on guess #' + str(firstGuess), 'and with nva =', firstNVA)
    print(solutionsForA, 'Solutions satisfied C1-C4')
    print(solutionsForB, 'Solutions satisfied C5-C9')
    # print(solutions, 'Solutions found')
    print('Total nva:', nva)


def bV3():
    print('using bV3...\n')
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
        if (checkConstraintsA(b, c, (e + f + 21), e, f)): solutionsForA += 1
        for h in range(1, 51):
            nva += 1
            for i in range(1, 51):
                nva += 1
                # g = 11
                # j = 40
                # d = e+f+21
                if checkConstraintsB(b, c, e+f+21, e, f, 11, h, i, 40): 
                    if (solutionsForB < 1): print('First solution found nva =', nva)
                    printAllB(b, c, e+f+21, e, f, 11, h, i, 40)
                    solutionsForB += 1
    # print('\n\nFirst solution found on guess #' + str(firstGuess), 'and with nva =', firstNVA)
    print(solutionsForA, 'Solutions satisfied C1-C4')
    print(solutionsForB, 'Solutions satisfied C5-C9')
    # print(solutions, 'Solutions found')
    print('Total nva:', nva)


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
