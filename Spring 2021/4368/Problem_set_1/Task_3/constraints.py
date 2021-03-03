
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
    return False
def C6(b, c, d, e, g, f):
    if (b+c+e+f) + d == (f-g)**2 - 1: return True
    return False
def C7(g, j):
    if 4*j==g**2+39: return True
    return False
def C8(f, h, g, i):
    if (i-g)**9==(f-h)**3 : return True
    return False
def C9(c, f, g):
    if (g-c)**2== f*c*c +1 : return True
    return False
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

def checkConstraintsA(B, C, D, E, F):
    if (C1(B, C, E, F) and C2(D, E, F) and C3(B, C, D, E, F)):
        return True
    return False

def checkConstraintsA2(sumBC, D, E, F):
    if (C1_v2(sumBC, E, F) and C2(D, E, F) and C3_v2(sumBC, D, E, F)):
        return True
    return False

def checkConstraintsB(b, c, d, e, f, g, h, i, j):
    if C5(e, g, h, i, j) and C6(b, c, d, e, g, f) and C7(g, j) and C8(f, h, g, i,) and C9(c, f, g): return True
    return False

def checkConstraintsC(b, c, d, e, f, g, h, i, j, k, l, m, n, o):
    if C10(k, m) and C11(f, i, n, o) and C12(m, n) and C13(b, g, h, i, o) and C14(k, m, o) and C15(b, i, k, l): return True
    return False

def printAll(B, C, D, E, F):
    print('A =', (B + C + E + F), ', B =', B, ', C =', C, ', D =', D, ', E =', E, ', F =', F)

def printAllB(b, c, d, e, f, g, h, i, j):
    print('A =', (b + c + e + f), ', B =', b, ', C =', c, ', D =', d, ', E =', e, ', F =', f, ', G =', g, ', H =', h, ', I =', i, ', J =', j)

def printAllC(b, c, d, e, f, g, h, i, j, k, l, n, m, o):
    print('A =', (b + c + e + f), ', B =', b, ', C =', c, ', D =', d, ', E =', e, ', F =', f, ', G =', g, ', H =', h, ', I =', i, ', J =', j, 'K =', k, ', L =', l, ', M =', int(m), ', N =', int(n), ', O =', int(o))
