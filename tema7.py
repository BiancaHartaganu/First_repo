'''
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’
'''
from abc import abstractmethod


class FormaGeometrica:
    def __init__(self):
        self.PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError
    @classmethod
    def descrie(self):
        print('Cel mai probabil am colturi')

forma_geometrica = FormaGeometrica()
forma_geometrica.descrie()


'''
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură
'''

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        super().__init__()
        self.latura = latura

patrat1 = Patrat(8)
print(patrat1.latura)
print(patrat1.PI)

'''
ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)
'''
class Patrat(FormaGeometrica):
    def __init__(self, latura):
        super().__init__()
        self.__latura = latura
    def latura(self):
        return self.__latura
    def get_latura(self):
        print(f'Getter: latura e {self.__latura}')
        return self.__latura
    def set_latura(self, latura):
        self.__latura = latura
        print(f'Setter: latura e {self.__latura}')
    def __delete__(self):
        self.__latura = None
        print(f'Deleter: am sters valoarea laturii.')
    def aria(self):
        return self.__latura * self.__latura

patrat = Patrat(6)
patrat.descrie()
patrat.get_latura()
patrat.set_latura(8)
print(patrat.aria())
patrat.__delete__()

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        super().__init__()
        self.__raza = raza
    @property
    def raza(self):
        return self.__raza
    @raza.getter
    def raza(self):
        print(f'Getter: raza este {self.__raza}')
        return self.___raza
    @raza.setter
    def raza(self, raza_noua):
        print(f'Setter: raza este {raza_noua}')
        self._raza = raza_noua
    @raza.deleter
    def raza(self):
        print(f'Deleter: am sters valoarea razei.')
        self.__raza = None
    def descrie(self):
        print('Eu nu am colturi')
    def aria(self):
        return self.PI * self.__raza ** 2

cerc = Cerc(2)
cerc.descrie()
cerc.__raza = 6
print(cerc.aria())
del cerc.__raza

'''
POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
'''
