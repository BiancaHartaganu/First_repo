note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
metoda = slice(None, None, -1)
print(note_muzicale[metoda])
note_muzicale = note_muzicale[metoda]
note_muzicale.reverse()
print(note_muzicale)

print(f'nota DO se repeta de {note_muzicale.count("do")} ori')

lista_1 = [3, 1, 0, 2]
lista_2 = [6, 5, 4]
lista_3 = lista_1 + lista_2
print(lista_3)
lista_1.extend(lista_2)
print(lista_1)

lista_1 = [3, 1, 0, 2, 6, 5, 4]
lista_1.sort()
print(lista_1)
lista_1.remove(0)
print(lista_1)

lista_1 = [3, 1, 0, 2, 6, 5, 4]
lista_goala = []
if lista_1 == lista_goala:
    print('lista este goala')
else:
    print('lista nu este goala')

del lista_1[0: len(lista_1)]
print(lista_1)

if lista_1 == lista_goala:
    print('lista este goala')
else:
    print('lista nu este goala')

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

print(f'Ana a luat nota {dict1["Ana"]}')
print(f'Gigel a luat nota {dict1["Gigel"]}')
print(f'Dorel a luat nota {dict1["Dorel"]}')

dict1 ['Dorel'] = 6
print(f'Dorel a luat nota {dict1["Dorel"]}')

dict1.pop('Gigel')
dict1 ['Ionica'] = 9
print(dict1)


