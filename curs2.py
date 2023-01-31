# bancomat
# verificam username si parola
# user-u are 2 incercari de a-si introduce username-ul. la a2a incercare gresita se iese din program
# daca user-u popate sa scoata o suma mai mica sau egala cu soldul curent
# daca introduci o suma prea mare poate sa aleaga daca doreste sa reincerce sau nu
# la a2a incercare daca user-ul introduce o suma prea mare, se iese din program
#
# expected_user_name = 'username'
# expected_password = 'password'
# sold = 5000
# username = input('Indtroduceti username: ')
# if username == expected_user_name:
#     print('Username corect')
# else:
#     print('Username incorect')
#     username = input('Indtroduceti username: ')
#     assert username == expected_user_name, 'Username gresit a doua oara'
# password = input('Introduceti parola: ')
# if len(password) == len(expected_password) and password == expected_password:
#     print('parola corecta')
# else:
#     print('Parola gresita')
#     password = input('Introduceti parola: ')
#     assert password == expected_password, 'Parola gresita a doua oara'
#
# suma_extrasa = int(input('Introduceti suma: '))
# if suma_extrasa <= sold:
#     print('Tranzactie reusita')
# else:
#     print('Suma dorita depaseste soldul curent')
#     reincercare = input('Doriti sa reintroduceti suma? ')
#     if reincercare == 'Da':
#         suma_extrasa = int(input('Introduceti suma: '))
#         assert suma_extrasa <= sold, 'Suma dorita depaseste soldul curent. O zi buna.'
#         print('Tranzactie acceptata')
#     elif reincercare == 'Nu':
#         print('Multumesc, o zi buna!')
import random

# exercitiu 2
# un zar cu 6 fete si simulam o aruncare de zaruri
dice_number = [1,2,3,4,5,6]
dice_roll = random.choice(dice_number)
number = int(input('Introdu un nr de la 1 la 6: '))
if number < dice_roll:
    print(f'Ai pierdut, ai ales un nr mai mic, ai ales numarul {number}, dar a fost {dice_roll} ')
elif number > dice_roll:
    print(f'Ai pierdut, ai ales un nr mai mare, ai ales numarul {number}, dar a fost {dice_roll} ')
else:
    print(f'Ai ghicit! Ai ales {number} si a fost {dice_roll} ')
    