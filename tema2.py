# 1. if are o conditie (daca nu e alba) urmata de else (atunci e neagra)
# ex2: daca e natural sau nu
x = 40
if x >= 0:
    print(f'{x} este un numar natural')
else:
    print(f'Nu e natural')
# ex3: daca e pozitiv, neg sau neutru
if x >= 0:
    print(f'{x} este pozitiv')
elif x < 0:
    print(f'{x} este negativ')
else:
    print('Numar neutru')
# ex4:
if x > -2 and x < 13:
    print(f'Numarul {40} se afla in intervalul -2 si 13')
else:
    print(f'Nu se afla in intervalul mentionat')
# ex5:
y = 30
print(abs(x) - abs(y))
#ex6
if not (x > 5 and x < 27):
    print(f'{x} nu este in interval')
else:
    print(f'Este in interval')
#ex7
if x == y:
    print(f'{x} este egal cu {y}')
else:
    print(f'{x} nu e egal cu {y}')
#ex8:
z = 20
if x == y and x == z:
    print(f' Triunghi isoscel')
elif x == y == z:
    print(f'Triunghi echilateral')
elif x != y != z:
    print(f'Triunghi oarecare')
else:
    print('Nu e triunghi')
