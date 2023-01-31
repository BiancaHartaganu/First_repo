# flow control - if else
# evalueaza conditii si bifurca codul in functie de rezultat
#daca pun false la "if" afiseaza doar "pornim radio" si "oprim radio", anuleaza toata functia if
piesa_faina = True

print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

# if else
# daca nr este par, printam acest lucru, altfel printam impar
# % - modulo afiseaza restul impartirii
nr = 4
if nr % 2 == 0:
    print('nr par')
else:
    print('impar')

# if, else if, else
# cum ne saluta robotelul in functie de ora
# luam date de la tastatura
# ne asiguram ca sunt transformate din string in int
ora = int(input('Introdu ora'))
print(ora == -17)
if ora < 0:
    print('ora negativa')
elif ora <= 11:
    print('buna dimineata')
elif ora <= 18:
    print('buna ziua')
elif ora <= 21:
    print('buna seara')
elif ora <= 24:
    print('noapte buna')
else:
    print('ora mai mare decat 24')
# "ctrl + /" sa anulezi codul si sa devina #

# robotel telefonic
optiunea = int(input('alege o optiune'))
if optiunea == 0:
    print('meniu anterior')
elif optiunea == 1:
    print('ati ales romana')
elif optiunea == 2:
    print('ati ales engleza')
else:
    print('nu am identificat opt, mai incearca')
