import cmath
import random
import string

def getZ(z):
    return random.uniform(-z, z)


def getScore(x, y):
    return (1+ pow(x + y +1,2)*(19-(14*x)+(3*pow(x,2))-(14*y)+(6*x*y)+(3*pow(y,2))))*(30+(pow((2*x)-(3*y),2))*(18-(32*x)+(12*pow(x,2))+(4*y)-(36*x*y)+(27*pow(y,2))))


def RHC(sp, p, z, seed):
    solutionChecked = 0
    random.seed(seed)
    bestSolution = {
        "x": sp[0],
        "y": sp[1],
        "score": getScore(sp[0], sp[1])
    }
    newBestFound = True
    print('First solution:', bestSolution)
    while newBestFound:
        newBestFound = False
        neighborhood = []
        for _ in range(p):
            z1 = getZ(z)
            z2 = getZ(z)
            x = bestSolution["x"]+z1
            y = bestSolution["y"]+z2
            ns =  getScore(x, y)

            newSolution = {
                "x": round(x, r)%2, # %2 to make sure the random num is always in range(-2,2)
                "y": round(y, r)%2,
                "score": round(ns, r)
            }
            neighborhood.append(newSolution)

        for solution in neighborhood:
            solutionChecked += 1
            if (solution["score"] < bestSolution["score"]):
                bestSolution = solution
                newBestFound = True
    bestSolution["count"] = solutionChecked
    return bestSolution


# p how many solutions to generate / loop?
# lower value is better when looking for solution.
# terminate if no solutions generated have a better (lower) solution then current best

# f take params x and y with values between -2 and 2
# new sol = (x+z1, y+z2)
#  z1/2 are randonly generated numbers [-0.5, 0.5] that you add to curr
# solution to get a new 'p' to add to neighborhood (of size p so do this p many times)
# then find best solution generated and see if it is better than curr solution
# if none are, return solution


    ###         main        ###
r = 5 # for rounding results
seed = 62

sp = [1, 1]
# sp = [-0.5, 0.3] 
# sp = [1, -2] 
# sp = [0,0]

p = 500
z = 1

answer = RHC(sp, p, z, seed)
print('Result:', answer)

