from math import sqrt

def guessCloseNbr(nbr):
    guess = round(nbr / 2)
    while guess * guess > nbr:
        guess -= 1
    return guess

def betterApprox(nbr, approx):
    return (approx + nbr/approx)/2

def ftSqrt(nbr):
    approx = guessCloseNbr(nbr)
    for i in range(3):
        approx = betterApprox(nbr, approx)
        i += 1
    return round(approx, 3)
