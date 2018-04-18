
def ftAbs(nbr):
    print(nbr)
    return nbr if nbr >= 0 else -nbr

def reducedForm(eqTab):
    div = ftAbs(min(eqTab, key=eqTab.get))
    while div > 1 and (eqTab[0] % div != 0 or eqTab[1] % div != 0 or eqTab[2] % div != 0):
        div -= 1
    if div > 1:
        eqTab[0] /= div
        eqTab[1] /= div
        eqTab[2] /= div
    return eqTab


