import sys
import re
from calculs import ftAbs, reducedForm, degree

def isEquat(equat):
    regex = "(\+?\-?[0-9.]+\*[Xx]\^[0-9]+)+=(\+?\-?[0-9.]+\*[Xx]\^[0-9]+)+"
    match = re.search(regex, equat)
    if match is None or match.group(0) != equat:
        print('\033[91mError: Syntaxe error\033[0m')
        sys.exit()

def addint(equat, index, sign, content):
    nbr = ''
    while index < len(equat) and (equat[index].isdigit() or equat[index] == '.' or equat[index] == ','):
        nbr += equat[index]
        index += 1
    content.append(float(nbr) if sign == 1 else -float(nbr))
    return len(nbr)

def parser(equat):
    sign = 1
    index = 0
    content = []
    while index < len(equat):
        if equat[index] == '=':
            content.append('=')
            sign = 1
        if equat[index] == '+' or equat[index] == '-':
            sign = 1 if equat[index] == '+' else 0
        if equat[index].isdigit():
            index += addint(equat, index, sign, content)
        else:
            index += 1
    return content

def contentToTab(content):
    eqTab = {0: 0, 1: 0, 2: 0}
    index = 0
    while index < len(content) and content[index] != '=':
        eqTab[ftAbs(content[index + 1])] = content[index]
        index += 2
    index += 1
    while index < len(content):
        eqTab[ftAbs(content[index + 1])] -= content[index]
        index += 2
    return eqTab


if len(sys.argv) >= 2:
    equat = sys.argv[1]
else:
    equat = input('Enter a polynomial : ')

equat = equat.replace(' ', '')

isEquat(equat)

content = parser(equat)
eqTab = contentToTab(content)

for key, value in eqTab.items():
    if key != 0 and key != 1 and key != 2:
        print("\033[94mPolynomial degree:", round(key), "\033[0m")
        print("\033[91mError : The polynomial degree is stricly greater than 2, I can't solve.\033[0m")
        sys.exit()

eqTab = reducedForm(eqTab)
rForm = "\033[95mReduced form: "
if eqTab[0] != 0:
    rForm += "- " if eqTab[0] < 0 else ""
    rForm += str(round(ftAbs(eqTab[0])) if ftAbs(eqTab[0]) % 1 == 0 else ftAbs(eqTab[0]))
    rForm += " * X^0 "
if eqTab[1] != 0:
    rForm += "+ " if eqTab[1] > 0 else "- "
    rForm += str(round(ftAbs(eqTab[1])) if ftAbs(eqTab[1]) % 1 == 0 else ftAbs(eqTab[1]))
    rForm += " * X^1 "
if eqTab[2] != 0:
    rForm += "+ " if eqTab[2] > 0 else "- "
    rForm += str(round(ftAbs(eqTab[2])) if ftAbs(eqTab[2]) % 1 == 0 else ftAbs(eqTab[2]))
    rForm += " * X^2 "
rForm += "= 0\033[0m"

print(rForm)
degree(eqTab)

