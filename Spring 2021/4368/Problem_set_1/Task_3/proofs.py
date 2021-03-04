
def square_root(num):
  	return num**0.5

def h20():
    maxJ = 50
    minJ = 1 # See H20
    #find max G
    for j in range(minJ, maxJ+1):
        # root = square_root(4*j-39)
        # print(root)
        if (4*j-39) < 0: print('J =', j, 'would make G an imaginary number')
        elif (square_root(4*j-39)%1==0): # G values that are a decimel
            print('J =', j, 'makes','G =', int(square_root(4*j-39)))
        else: print('J =', j, 'makes','G =', square_root(4*j-39))
        

print('\n\n')

def h21():
    #from C7
    # Get all possible values for J and G
    maxG = 12 # G < 13 from H20
    for g in range(1, maxG+1):
        j = (g**2+39)/4
        # print('G =', g, 'if', 'J =', int(j))
        if (j%1==0): # if J is a whole number
            print('G =', g, 'if', 'J =', int(j))

def h22():
    for c in range(1,50):
        f = (c**2 - 22*c + 120)/(c**2)
        if (f>1): print('c =', c, 'f =', f)

def h33():
    maxM = 51

## main ##

# h20()
# h21()
# h22()





