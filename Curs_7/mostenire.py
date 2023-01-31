'''
Mostenire: Capacitatea unei clase de a imparrtasi atat metode cat si atribute din alta clasa
Clasa copil  mosteneste clasa parinte, astfel clasa copil preia metodele si atributele din clasa parinte
Clasa copil poate avea oricate metode sau atribute in plus faata de clasa parinte.
Clasa parinte nu mosteneste nimic de la Clasa/clasele Copil!!!!!
!! In python. O clasa copil poate mosteni mai multe clase parintte . ex: class Copil(Parinte1, Parinte2, Parinte3...)
In clasa copil putem apela clasa parinte folosind super()
'''


class Person: #clasa parinte
    def __init__(self, nume, varsta, adresa):
        self.nume = nume
        self.varsta = varsta
        self.adresa = adresa

    def anul_nasterii(self):
        return 2023 - self.varsta

    def descriere(self):
        print(self.nume, self.varsta, self.adresa)

class Student(Person): #clasa copil
    def __init__(self, nume, varsta, adresa, facultate, an_studiu):
        #super() reprez un keyword care apeleaza sau reprezinta clasa parinte(Person)
        # cu super() apelam constructorul clasei Parinte
        super().__init__(nume, varsta, adresa)
        self.facultate = facultate
        self.an_studiu = an_studiu

    def descriere(self): #fac suprascriere la metoda "descriere" din clasa parintelui
        super().descriere()
        print(self.facultate, self.an_studiu)

class Angajat(Person):
    def __init__(self, nume, varsta, adresa, companie, salariu):
        super().__init__(nume, varsta, adresa)
        self.companie = companie
        self.salariu = salariu

    def descriere(self):
        super().descriere()
        print(self.companie, self.salariu)

    def salariu_anual(self):
        return self.salariu * 12

class Profesor(Angajat):
    def __init__(self, nume, varsta, adresa, companie, salariu,curs, nr_ore):
        super().__init__(nume, varsta, adresa, companie, salariu)
        self.curs = curs
        self.nr_ore = nr_ore


# student = Student("Vlad", 22, "adresa 1", "UTCN", 5)
# # print(student.nume)
# # print(student.facultate)
# print(student.descriere())

profesor = Profesor("Vlad", 33, "Adresa1", "It Factory", 1000, 160, "Testare Automata")
profesor.descriere()
print((profesor.salariu_anual() * "euro"))
