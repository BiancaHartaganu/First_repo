# def suma_numerelor(x, y):
#     return (f'Suma celor doua numere este: {x + y}')
#
# print(suma_numerelor(3, 4))

# def par_impar(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
# print(par_impar(7))

# def numar_caractere(nume, prenume, nume_mijlociu):
#     nume = len(nume)
#     prenume = len(prenume)
#     nume_mijlociu = len(nume_mijlociu)
#     print(f'Suma caracterelor este: {nume + prenume + nume_mijlociu}')
#
# numar_caractere('Hartaganu', 'Bianca', 'Claudia')

# def aria_dreptunghiului(x, y):
#     return (f'Aria dreptunghiului este: {x * y}')
#
# print(aria_dreptunghiului(2, 10))

# def aria_cercului(r):
#     aria = 3.14 * r * r
#     print(f'Aria cercului este: {aria}')
#
# aria_cercului(8)

# def caracter_in_string(x, y):
#     if x in y:
#         return True
#     else:
#         return False
#
# print(caracter_in_string('z', 'zebra'))

# def string_litere_lower_upper(string):
#     lower_case = 0
#     upper_case = 0
#     for char in string:
#         if char.islower():
#             lower_case = lower_case + 1
#         elif char.isupper():
#             upper_case = upper_case + 1
#     print(f'Numarul de caractere lower case este: {lower_case}')
#     print(f'Numarul de caractere upper case este: {upper_case}')
#
# string_litere_lower_upper('BuEnOs')

# def lista_numere(lista):
#     lista_numere_pozitive = []
#     for numar in lista:
#         if numar > 0:
#             lista_numere_pozitive.append(numar)
#     return print(lista_numere_pozitive)
#
# lista_numere([-7, 0, 5, -3, -4, 9])

# def comparari(x, y):
#     if x > y:
#         print(f'Primul numar {x} este mai mare decat al doilea numar {y}')
#     elif y > x:
#         print(f'Al doilea numar {y} este mai mare decat primul numar {x}')
#     else:
#         print('Numerele sunt egale')
#
# comparari(2, 2)

def add_number_to_set(number, number_set):
    if number in number_set:
        print(f'Nu am adaugat numărul {number} în set. Acesta există deja')
        return False
    else:
        number_set.add(number)
        print(f'Am adaugat numărul {number} în set')
        return True

print(add_number_to_set(5, {9, 3, 4}))

