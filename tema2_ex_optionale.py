# 1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
# x = int(123588)
# if x < 1000:
#     print('x nu are minim 4 cifre')
# else:
#     print('x are minim 4 cifre')
#
# # 2. Verifica daca x are exact 6 cifre
# if 100000 <= x <= 999999:
#     print('x are fix 6 cifre')
# else:
#     print('x nu are fix 6 cifre')
#
# # 3 Verifica daca x este numar par sau impar
#
# if x % 2 == 0:
#     print('x este numar par')
# else:
#     print('x este numar impar')
#
# # 4. Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre
# # ele
#
# x = 225
# y = 105
# z = 89
#
# if x > y and x > z:
#     print('x este numarul cel mai mare')
# elif y > x and y > z:
#     print('y este numarul cel mai mare')
# else:
#     print('Z este numarul cel mai mare')
#
# # 5.Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca
# # triunghiul este valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de
# # 180 de grade sau daca suma lungimilor a oricare doua laturi este mai mare decat
# # lungimea celei de-a treia laturi)
#
# x = int(70)
# y = int(80)
# z = int(30)
#
# if (x + y + z) == 180:
#     print('triunghiul este valid')
# else:
#     print('triunghiul nu este valid')

# 6. Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de
# la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. ex: dacă
# ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the
# smarte'

# fraza = "Coral is either the stupidest animal or the smartest rock"
# x = int(input('introdu valoarea lui x: '))
# print(fraza[0:(len(fraza)-x)])
#
# # 7. Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format
# # din primele 5 caractere + ultimele 5
#
# fraza_2 = (fraza[0:5]+fraza[len(fraza)-5:len(fraza)])
# print(fraza_2)
#
# # 8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza
# # indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock
# # (hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing,
# # afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest
# # animal or the smartest '
#
# print(fraza.find("rock")) # aflam indexul literei r din cuvantul rock
# # functia slice returneaza sirul pana la indexul specificat
# print(fraza[slice(fraza.find("rock"))])

# # 9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se
# # va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA'
# # e acceptat ca un string in care primul si ultimul caracter este la fel (hint, te poti folosi de o
# # functie pentru a face string-ul case insensitive)
#
# string_1 = input("Inroduceti stringul: ")
# assert string_1[0].casefold() == string_1[-1].casefold(), "Prima si ultima litera nu sunt identice"
# print("Prima si ultima litera sunt identice")

# 10. Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare
# (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)

string_2 = "0123456789"
print(string_2[0:len(string_2)-1:2])
print(string_2[1:len(string_2):2])