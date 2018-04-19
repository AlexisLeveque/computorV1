from sqrt import ftSqrt

def ftAbs(nbr):
    return nbr if nbr >= 0 else -nbr

def reducedForm(eqTab):
    div = ftAbs(eqTab[0])
    while div > 1 and (eqTab[0] % div != 0 or eqTab[1] % div != 0 or eqTab[2] % div != 0):
        div -= 1
    if div > 1:
        eqTab[0] /= div
        eqTab[1] /= div
        eqTab[2] /= div
    return eqTab

def second_degree(eqTab):
    print(eqTab)
    delta = eqTab[1] * eqTab[1] - 4 * eqTab[2] * eqTab[0]
    if delta > 0:  #x1 = (-b-√Δ)/(2a) et x2= (-b+√Δ)/(2a)
        r1 = (-eqTab[1] + ftSqrt(delta))/2 * eqTab[2]
        r2 = (-eqTab[1] - ftSqrt(delta))/2 * eqTab[2]
        print("Discriminant is strictly positive, the two solutions are:")
        print("r1 : ", r1)
        print("r2 : ", r2)
    elif delta == 0:  #-b/(2a)
        r = -eqTab[1]/(2 * eqTab[2])
        print("Discriminant is strictly equal to 0 , the solution is:")
        print("r : ", r)
    else:
        r1 = (-eqTab[1] )/2 * eqTab[2]
        r1i = (+ ftSqrt(-delta))/2 * eqTab[2]
        r2 = (-eqTab[1])/2 * eqTab[2]
        r2i = (- ftSqrt(-delta))/2 * eqTab[2]
        print("Discriminant is strictly negative, the two solutions are:")
        print("r1 : ", r1, "+ i *", r1i)
        print("r2 : ", r2, "- i *", r2i)

def first_degree(eqTab):
    if eqTab[0] == 0:
        print("The result is x = 0")
    else:
        print("The result is x = ", round(eqTab[0]/eqTab[1], 4))

def simple(eqTab):
    if eqTab[0] == 0:
        print("Every real are solution")
    else:
        print("No solution")

def degree(eqTab):
    if eqTab[2] == 0 and eqTab[1] == 0:
        simple(eqTab)
    elif eqTab[2] == 0:
        first_degree(eqTab)
    else:
        second_degree(eqTab)
