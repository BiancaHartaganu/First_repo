# avem o lista ce contine dif tipuri de date
lista1 = ['Maria', 32, True, 12.5]
# # print(type(lista1))
# print(lista1)
# #printeaza nr de elem din lista de mai sus
# print(len(lista1))
# #afisam primul elem apoi ultimul elem
# print(lista1[0])
# print(lista1[-1])
#stergem primul elem din lista
# lista1.remove(lista1[0])
# print(lista1)
# lista1.pop(0)
# print(lista1)
#remove doar sterge, pop sterge si returneaza
# first_element = lista1.pop(0)
# print(first_element)
#sau
# first_element = lista1.remove(lista1[0])
# print(first_element)

#adaugam un elemt nou la finalul listei
# lista1 = lista1 + ['Ion']
# print(lista1)
#
# #folosim functia append
# lista1.append(21)
# print(lista1)
#
# #adaugam o alta lista pe langa lista pe care o avem
# lista1.extend([1,2,3,4])
# print(lista1)
#adaugam inca un elem pe pozitia cu indexu 2
# lista1.insert(2,'32')
# print(lista1)
#daca nr 32 apare mai mult de o singura data
# assert lista1.count(32) > 1, 'Nr 32 nu apare mai mult de o singura data'
#var 2 cu if
# if lista1.count(32) > 1:
#     print('Nr 32 apare mai mult de o singura data')
# else:
#     print('Nr 32 nu apare mai mult  de o sg data')

# lista1.reverse()
# print(lista1)

# dictionar
#cream un dictionar care sa contina 2 elemente
#cheile sunt nr intregi, iar valorile sunt zile ale saptamanii

dictionar1 = {'ziua 1':'luni', 'ziua 2':'marti'}
# print(dictionar1)
#
# print(dictionar1.keys())
# print(dictionar1.values())
#adaugam cheia 2 cu valoarea "miercuri"
# dictionar1 = dictionar1 + {2:'Miercuri'} #arunca o eroare
# print(dictionar1.update({2:'Miercuri'})) #nu returneaza nimic
# # dictionar1.update({2:'Miercuri'})
# print(dictionar1)

#eliminam un element(trebuie sa cunoastem cheia pt eliminare)
# dictionar1.pop(0)
# print(dictionar1)
# print(dictionar1.popitem() #returneaza ultimul elem(elimina elementul din dictionarul respectiv)
# print(dictionar1)

# verificam daca cheia "0" se afla in dictionar
# print(dictionar1['ziua 1'])
# if  0 in dictionar1.keys():
#     print(f'Cheia 0 exista si vrem sa afisam valoarea {dictionar1.get(0)} ')
# else:
#     print('Cheia 0  nu exista')

#verificam daca valoarea luni se afla in dictionar
# if 'Luni' in dictionar1.values():
#     print('Valoarea luni exista in dictionar')
# else:
#     print('Valoarea luni nu exista')

#seturi:
# new_set = set() #metoda de a declara un set gol
# new_set2 = {1,2,3}
# atentie = {} #se declara un dictionar
# print(type(new_set))
# print(type(new_set2))
# print(type(atentie))
# # adaugam elemente in primul set
# new_set.update([1,2,3,4,5,6,1])
# print(new_set) #setul nu accepta duplicate, se afiseaza o sg data "1"
# # adaugam un sg elem cu add
# new_set.add(7)
# print(new_set)
# new_set.add(0)
# print(new_set)
# new_set2 = {'Martie', 'Aprilie', 1,2 }
# print(new_set2)
# # new_set.update(new_set2)
# # print(new_set)
# print('new set - new_set2 ' + str(new_set.difference(new_set2)))
# print('new_set2 - new_set ' + str(new_set2.difference(new_set)))
# #difference returneaza un al 3lea set ce contine valorile care sunt in new set2 si nu sunt in new set
#
# #intersectia a doua seturi (elementele comune)
# intersection_set = new_set.intersection(new_set2)
# #returneaza un al 3lea set care returneaza valorile comune celor 2 seturi
# # print(new_set.intersection(new_set2))
# print(new_set)

#verificam daca elem cu valoarera 3 este in new_set
# if 3 in new_set:
#     print('Este')
# else:
#     print('Nu este')

#creare de TUPLE
tupla = tuple()
tupla2 = ()
# print(type(tupla))
# print(type(tupla2))

tupla = (10,20,30,40)
print(tupla)
#de cate ori apare elem 30
print(tupla.count(30))
#accesam elem de pe ultima pozitie
print(tupla.index(40)) #returneaza indexul valorii respective(apelate)
print(tupla[-1])
tupla_nested = (10,20,30,40,(1,2,('ian','feb'),3,4))
print(tupla_nested)
# accesam elementul 3 din tupla
print(tupla_nested[4][2]) #elem din pozitia 4 e o tupla si 2 este pozitia din tupla
print(tupla_nested[4][2][1]) #afisam feb
if 40 in tupla_nested:
    print('40 este')
else:
    print('40 nu este')
if (1,2,('ian','feb'),3,4) in tupla_nested:
    print('yes')









