class Persoana():
#atribute
    nume = ''
    prenume = ''
    varsta = 0

    def __init__(self,nume, prenume,varsta ):
        self.nume = nume #self.nume este atributul obiectului instantiat
                        # iar nume este parametrul functiei __init__
                        #prin acest parametru atribuim o valoare atributului self.nume
        self.prenume = prenume
        self.varsta = varsta

    def __str__(self):
        return f"Numele meu este {self.nume}. Prenume: {self.prenume}. Varsta: {self.varsta}"

    def varsta_peste_10_ani(self):
        return self.varsta + 10

bianca = Persoana("Hartaganu","Bianca", 27)
print(bianca.nume, bianca.prenume, bianca.varsta)
bianca.nume = 'Hartaganu_modificat'
print(bianca.nume, bianca.prenume, bianca.varsta)
# florica = Persoana("Vladimir", "Florica", 55)
# print(florica.nume, florica.prenume, florica.varsta)
#
# print(bianca)
#
# print(bianca.varsta_peste_10_ani())
