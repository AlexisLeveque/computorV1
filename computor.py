import sys
from calculs import ftAbs, reducedForm, degree



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
# else:
#     equat = input('Enter a polynomial : ')

equat = "2 * X^2 + 4 * X^1 - 10 * X^0 = 0 * X^0" #only for test purpose

equat = equat.replace(' ', '')

content = parser(equat)
print(content)
eqTab = contentToTab(content)

print(eqTab)

for key, value in eqTab.items():
    if key != 0 and key != 1 and key != 2:
        print("The polynomial degree is not between 0 and 2, I can't solve.")

eqTab = reducedForm(eqTab)
print(eqTab)
degree(eqTab)



