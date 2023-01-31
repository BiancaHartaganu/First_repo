import math

tip_cafea = 'Jacobs'
gramaj = 300
pret = 30.5
ambalaj_atragator = True
#
print(type(tip_cafea))
print(type(gramaj))
print(type(pret))
print(type(ambalaj_atragator))
#
print(round(pret))
pret = 30
print(pret)
print(type(pret))
#
print('Cafeaua mea preterata este ' +  tip_cafea)
print(f'Gramajul cumparat este de + {gramaj}')
print(f'Pretul cafelei este {pret} lei')
print(f'Este {ambalaj_atragator} ca se cumpara mult din cauza ambalajului')
# pret = float(pret)
# print(type(pret) adaugate

numele = 'Hartaganu'
prenumele = 'Bianca'
numele = input('Introduceti numele: ')
prenumele = input('Introduceti prenumele: ')
nr_litere_nume = len(numele)
nr_litere_prenume = len(prenumele)
print(f'Numele complet are {nr_litere_nume + nr_litere_prenume} caractere')

lungime = 10
latime = 6
aria = lungime * latime
lungime = int(input('lungime: '))
latime = int(input('latime: '))
print(f'Aria dreptunghiului este {aria}')

coral = 'Coral is either the stupidest animal or the smartest rock'
repetari = int(coral.count('the'))
print(f'Cuvantul "the" se repeta de {repetari} ori.')
assert type(repetari) == int
print('All good')
#sau varianta assert string.isdigit(), 'Stringul nu contine doar numere.'
#isdigit e o functie care verifica daca e numerica.

name = 'Not a morning person yet'
print('The original string is: ' + name)
res = []
for ele in name.split():
    if len(ele) % 2 :
        res.append(ele)
print('The odd length strings are : ' + str(res))
def middle_char(txt):
  return txt[(len(txt)-1)//2:(len(txt)+2)//2]
print('Middle character(s) of the said string: ', middle_char(name))

name = 'apa'
name = input('name: ')
if(name == name[::-1]):
    print('String is a palindrome')
else:
    print('String is not a palindrome')
#sau assert name == x[::-1],

#eex 1 de la optionale
x = input()
assert len(x)%2 != 0, 'Lungimea stringului este para'
middle_caracter = math.floor(len(x)/2)




