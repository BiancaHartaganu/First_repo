#simularea unui bancomat

'''
1. Sa definim un user si parola
2. Sa definim un sold al contului de tipul int
3. Sa introducem de la tastatura username si parola contului
4. Daca username sau parola e gresita, sa se opreasca executarea programului
5. Dorim sa scoatem o suma de bani si dorim sa verificam daca avem fonduri suficiente
'''

user = 'username'
expected_password = '1234'
sold = 100
username = input('username: ')
assert user == username, 'username gresit'
print('username corect')
parola = (input('parola: '))
assert expected_password == parola, 'parola gresita'
print('parola corecta')

suma = int(input('introduceti suma dorinta: '))
assert suma <= sold, 'Fonduri insuficiente'
print(f'Suma dorita de dvs este {suma}')
print('plata efectuata')

