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
    delta = eqTab[1] * eqTab[1] - 4 * eqTab[2] * eqTab[0]
    print("\033[94mPolynomial degree: 2\033[0m")
    print("\033[94mdelta =", delta, "\033[0m")
    if delta > 0:  #x1 = (-b-√Δ)/(2a) et x2= (-b+√Δ)/(2a)
        r1 = (-eqTab[1] + ftSqrt(delta))/(2 * eqTab[2])
        r2 = (-eqTab[1] - ftSqrt(delta))/(2 * eqTab[2])
        print("\033[92mDiscriminant is strictly positive, the two solutions are:\033[0m")
        print("\033[93mr1 : ", r1, "\033[0m")
        print("\033[93mr2 : ", r2, "\033[0m")
    elif delta == 0:  #-b/(2a)
        r = -eqTab[1]/(2 * eqTab[2])
        print("\033[92mDiscriminant is strictly equal to 0 , the solution is:\033[0m")
        print("\033[93mr : ", r, "\033[0m")
    else: #x1 = (-b-i√Δ)/(2a) et x2= (-b+i√Δ)/(2a)
        r1 = (-eqTab[1] )/(2 * eqTab[2])
        r1i = (+ ftSqrt(-delta))/(2 * eqTab[2])
        r2 = (-eqTab[1])/(2 * eqTab[2])
        r2i = (- ftSqrt(-delta))/(2 * eqTab[2])
        print("\033[92mDiscriminant is strictly negative, the two solutions are:\033[0m")
        print("\033[93mr1 : ", r1, "+ i *", r1i, "\033[0m")
        print("\033[93mr2 : ", r2, "- i *", r2i, "\033[0m")

def first_degree(eqTab):
    print("\033[94mPolynomial degree: 1\033[0m")
    if eqTab[0] == 0:
        print("\033[92mThe solution is \033[93mx = 0\033[0m")
    else:
        print("\033[92mThe solution is\033[93m x = ", -eqTab[0]/eqTab[1], "\033[0m")

def simple(eqTab):
    print("\033[94mPolynomial degree: 0\033[0m")
    if eqTab[0] == 0:
        print("\033[92mEvery real are solution\033[0m")
    else:
        print("\033[92mNo solution\033[0m")

def degree(eqTab):
    if eqTab[2] == 0 and eqTab[1] == 0:
        simple(eqTab)
    elif eqTab[2] == 0:
        first_degree(eqTab)
    else:
        second_degree(eqTab)
