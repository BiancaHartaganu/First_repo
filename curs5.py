# functie simpla(fara parametrii si return)
# definim o functie
def hello_world():
    print('Hello world')
#
# hello_world()
# hello_world()
# #daca nu punem paranteze functia nu va fi executata
# # daca o functie nu e apelata codul din interiorul ei nu va fi executat
#
# x = hello_world() #codul din functie va fi executat si x va lua valoarea de none(functia nu returneaza nimic)
# print(x)
#
# def say_hi_name(name): #name e un parametru
#     print(f'Hi, my name is {name}')
# say_hi_name('Bianca') #Bianca e un argument al parametrului name
#
# lista_nume = ['Iuliana', 'Cosmin', 'Andrei']
# say_hi_name(lista_nume)
# for nume in lista_nume:
#     say_hi_name(nume)

# definim o functie care ne zice daca un nr e par sau impar

# def is_even():
#     numar = int(input('Introduceti un numar: '))
#     if numar %2 == 0:
#         return True
#     else:
#         return False
# is_even()

def is_even_2(numar):
    if numar %2 == 0:
        return True
    else:
        return False
# # argument_numar = int(input('Introduceti un numar: '))
# # y = is_even_2(argument_numar)
# # print(y)
# if is_even_2(10) == True:
#     print('10 este par')

# functie ce returneaza suma tuturor elementelor dintr-o lista
#
def suma_numere(lista_numere):
    suma = 0
    for numar in lista_numere:
        suma += numar
    return suma
# lista_1 = [1,2,3,4]
# print(suma_numere(lista_1))

# creem o functie care ne returneaza val maxima dintr-o lista

# def nr_maxim(lista):
#     maxim = 0
#     for numere in lista:
#         if maxim < numere:
#             maxim = numere
#     return maxim
# lista_2 = [7,10,3,4]
# print(f'Numarul maxim este {nr_maxim(lista_2)}')

def numar_maxim2(*numere):
    maxim = 0
    for numar in numere:
        if numar > maxim:
           maxim = numar
    return maxim, "numar maxim"
# m,string = numar_maxim2(1,2,3,4,5)
# print(numar_maxim2(1,2,3,4,5))
# print(m)
# print(string)
#
# m = numar_maxim2(1,2,3,4,5)
# print(numar_maxim2(1,2,3,4,5))
# print(m)

#variabila globala care e definita inafara functiei care poaate fi folosita in interiorul oricarei functii

var_globala = 30
# print(str(var_globala), 'din afara functiei')

def dummy():
    # var_globala = 60
    # print(str(var_globala), 'din interiorul functiei') # valoarea variabilei globale ramane nemodificata in afara functiei
    # pt a modifica valoarea variabilei globale in intereiorul unei functii folosim key word-ul "global"
    global var_globala
    print(var_globala)
# dummy(),
# print(var_globala)
def say_my_age(age):
    print(age)
    return 'sunt aici'
print(say_my_age(5))
#var 2:
def say_my_age(age=10):
    print(age)
    # return 'sunt aici'
say_my_age()
say_my_age(30)

'''
def- key word care anunta inceputul definirii unei functii
say_my_age - numele functiei, este dat de catre user si poate fi orice nume. in general nuumele functiei trebuie sa fie sugestiv pt actiunea pe care o face
() - reprezentant al zonei in care putem sa specificam parametrii(parametrii sunt optionali)
: - reprez inceputul corpului functiei
avem corpul functiei (asemanator structurilor if while for)
'''


