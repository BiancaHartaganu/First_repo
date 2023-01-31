'''
Structuri repetitive
= modalitati in care putem executa un cod in mod repetat pana cand o anumita conditie nu mai e indeplinita
Exista 4 tipuri de structuri repetitive:
1. while
2. do while (nu e scopul cursului)
3. for
4. for each
Modalitati de control al structurilor repetitive
1. Break (opreste executarea structurii repetitive)
2. Continue (face skip la o iteratie)
'''

'''
While - este o structura repetitiva in care executam o serie de instructiuni, atata timp cat conditia e adevarata
De regula, elementul sau variabila de control a while'ului se declara inafara acestuia
'''
# ex1 - printeaza pe ecran toate nr de la 1 la 10

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# debugging = proces prin care analizam codul pt a vedea cum circula datele
# de fiecare data cand vrem sa facem debugging putem sa punem breakpoint (bulina rosie)

# ex2  - Suma nr de la 1 la 500
# suma = 0
# i = 1
# while i <= 500:
#     suma += i
#     i += 1
# print(suma)

# ex3 lista cu lunile anului si sa o parcurgem, apoi sa printam fiecare valoare din lista
list1 = ['Ianuarie', 'Februarie', 'Martie','Aprilie','Mai','Iunie','Iulie']
index = 0
# while index <len(list1):
#     print(list1[index])
#     index += 1
#parcurgem lista fara a afisa luna Martie si luna Mai
# while index <len(list1):
#     if list1[index] == "Martie" or list1[index] == "Mai":
#        index += 1
#         continue
#     print(list1[index])
#     index += 1

# parcurgem lista pana ajungem la luna aprilie
# while index <len(list1):
#     if list1[index] == "Aprilie":
#         break
#     print(list1[index])
#     index += 1

# inlocuim luna Mai cu luna Noiembrie
# while index < len(list1):
#     if list1[index] == "Mai":
#       list1[index] = "Noiembrie"
#       break
#     index += 1
# print(f'Lista finala este : {list1}')

'''
For - o structura repetitiva care e utilizata atunci cand vrem sa parcurgem o structura de date cu scopul de a prelucra datele din acea structura de date
De asemenea poate fi folosit sa executam un set de instructiuni de un nr definit de ori (range)
Structura unui for:
- inceputul structurii repetitive "for"
- variabila de iteratie
- inceputul range'ului de parcurs (default e 0, optional)
- sfarsitul range'ului de parcurs (obligatoriu) - capatul superior nu e luat in considerare
- pasul range'ului (care din cand cand by default e 1)
'''

# # ex4 - sa parcurgem toate nr de la 0 la 10 si sa printam separat nr pare de nr impare
# # for i in range(11):
# #     if i%2 == 0:
# #         print(f'Nr {i} este par')
# #     else:
# #         print(f'Nr {i} este impar')
#
# # nested list sau embedded list sau lista impricata sau matrice
#
# matrice = [
#     [1, 'test1'],
#     [2, 'test2',3],
#     [5, 6, 7]
# ]
# for i in range(len(matrice)):
#     for j in range(len(matrice[i])):
#         print(f'Valoarea de pe pozitia [{i}][{j}] este {matrice[i][j]}')

# luni = ['Ianuarie', 'Februarie', 'Martie','Aprilie','Mai','Iunie','Iulie']
# # for i in range(len(list1)):
# #     print(list1[i])
# for luna in luni: #for each
#     print(luna)

# ex6
# lista_culori_disponibile = ["rosu", "galben", "albastru", "fuchsia", "magenta", "roz", "violet", "maro", "negru",
#                             "orange", "verde", "indigo"]
# liste_culori_de_exclus = ["rosu", "galben", "roz"]
#
# lista_culori_neexcluse = []
#
# for culoare in lista_culori_disponibile:
#     if culoare in liste_culori_de_exclus:
#         continue
#     lista_culori_neexcluse.append(culoare)
# print(lista_culori_neexcluse)

#ex7 - sortam o lista de numere(algoritmi de sortare!)

lista_nesortata = [1, 5, 10, 2, 50, 11, 20, 12]
# lista_nesortata.sort() # suprascrie lista initiala, nu returneaza nimic
# print(lista_nesortata)

#acum le sortam manual
for i in range(len(lista_nesortata)-1):
    for j in range(len(lista_nesortata)-1):
        if lista_nesortata[j] > lista_nesortata[j+1]:
            lista_nesortata[j],lista_nesortata[j+1] = lista_nesortata[j+1], lista_nesortata[j]
print(lista_nesortata)


'''
Recapitulare
tupla - o structura de date care se defineste intre 2 paranteze: (2,5)
      - Are indexi, sunt imutabile
dictionar - structura de date cu cheie si valoare: {cheie: valoare}
        - sunt mutabile,
        - cheile sunt unice
        - dictionarele sunt ordonate
Set - structura de date care au elemente unice
    - nu sunt ordonate sau indexate
    - nu putem schimba locatia elementelor
    - se pot adauga sau sterge elemente
Liste - structura de date care pastreaza mai multe valori intr-o singura variabila
      - pastreaza diferite tipuri de date (doar in Python)
      - fiecare elem are index si este mutabil
'''


