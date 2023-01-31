'''
Polimorfism = poli (mai multe) morfism(forma/forme) = ceva care poate lua mai multe forme
In cazul OOP, o metoda poate sa aibe acelasi nume in clase diferite dar implementari/logica diferita in interior

Abstractizare este un proces prin care putem sa ascundem o anumita functionalitate specifica fata de utilizator
de asemenea, putem forta un anumit comportament in clasele copil

Utilizatorul stie ce face functionalitatea dar nu si cum
Clasa parinte care este o clasa abstracta, nu putem sa cream obiecte din ea, ci doar sa o folosim ca un template pt clasele copil

In abstractizare avem 2 concepte:
- Interfata -> contine doar metode abstracte(in java exista interfete propriu-zise: Intereface numeInterfata..)
- Clasa abstracta -> care contine atat metode abstracte cat si metode proprii cu logica in interiorul lor (in java exista Abstract class numeClasa)

Clasa Abstracta trebuie sa mosteneasca clasa ABC(Abstract Class Method)
Fiecare metoda a clasei abstracte trebuie sa arunce exceptia NotImplementedError sau pass
Clasa abstracta NU are constructor pt ca nu cream obiecte din ea!!

O metoda abstracta e o metoda care nu are corp(fara logica)

'''

# def add(a,b,c=8):
#     return (a+b+c)
#
# print(add(1,2,3))
# print(add(1,2))

# abstractizare
from abc import ABC, abstractmethod

class Vehicul(ABC):

    @abstractmethod    #decorator ca sa marcam acceasta metoda ca abstracta
    def nr_roti(self):
        raise NotImplementedError

    @abstractmethod
    def nr_locuri(self):
        pass           #metodele abstracte neavand logica si pt a preveni anumite erori, scriem in corpul metodelor pass sau NotImplementedError


    @classmethod
    def metoda_logica_proprie(self):
        print("Aici este o metoda cu logica proprie, nu trebuie implementata in clasa copil")

class Masina(Vehicul):

    def __init__(self, culoare):
        self.culoare = culoare

    def nr_roti(self):
        return 4
    def nr_locuri(self):
        return 5

class Bicicleta(Vehicul):
    def __init__(self, culoare, roti_ajutatoare = False):
        self.culoare = culoare
        self.roti_ajutatoare = roti_ajutatoare

    def nr_roti(self):
        if self.roti_ajutatoare: #self.roti_ajutatoare == true (echivalent)
            return 4
        else:
            return 2

    def nr_locuri(self):
        return 1


masina = Masina("verde")
masina.metoda_logica_proprie()
print(masina.nr_roti())
print(masina.nr_locuri())
masina.metoda_logica_proprie()

bicicleta = Bicicleta("rosu")
print(bicicleta.nr_roti())
print(bicicleta.nr_locuri())
bicicleta.metoda_logica_proprie()

# vehicul = Vehicul() # nu putem crea un obiect de tipul clasei abstracte
