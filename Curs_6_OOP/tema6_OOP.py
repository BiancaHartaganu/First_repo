# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()
#
# class Cerc():
#     def __init__(self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descriere_cerc(self):
#         print(f'culoare: {self.culoare} raza: {self.raza}')
#
#     def aria(self):
#         aria = 3.14 * self.raza ** 2
#         return aria
#
#     def diametru(self):
#         diametru = 2 * self.raza
#         return diametru
#
#     def circumferinta(self):
#         circumferinta = 2 * 3.14 * self.raza
#         return circumferinta
#
# cerc_1 = Cerc(6, 'Mov')
# cerc_2 = Cerc(8, 'Visiniu')
#
# cerc_1.descriere_cerc()
# print(cerc_1.aria())
# print(cerc_1.diametru())
# print(cerc_1.circumferinta())
#
# print(22 * '*')
#
# cerc_2.descriere_cerc()
# print(cerc_2.aria())
# print(cerc_2.diametru())
# print(cerc_2.circumferinta())

# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul

# class Dreptunghi():
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descrie(self):
#         print(f'lungime: {self.lungime}, latime: {self.latime}, culoare: {self.culoare}')
#
#     def aria(self):
#         aria = self.lungime * self.latime
#         return aria
#     def perimetrul(self):
#         perimetrul = (self.latime + self.lungime) * 2
#         return perimetrul
#     def schimba_culoarea(self, noua_culoare):
#         self.culoare = noua_culoare
#
# dreptunghi_1 = Dreptunghi(8, 3, 'portocaliu')
# dreptunghi_2 = Dreptunghi(12, 7, 'rosu')
#
# dreptunghi_1.descrie()
# print(dreptunghi_1.aria())
# print(dreptunghi_1.perimetrul())
# dreptunghi_1.schimba_culoarea('roz')
# dreptunghi_1.descrie()
#
# print(22 * '*')
#
# dreptunghi_2.descrie()
# print(dreptunghi_2.aria())
# print(dreptunghi_2.perimetrul())
# dreptunghi_2.schimba_culoarea('verde')
# dreptunghi_2.descrie()
#
# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

# class Angajat():
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descrie(self):
#         print(f'nume: {self.nume}, prenume: {self.prenume}, salariu: {self.salariu}')
#     def nume_complet(self):
#         return self.nume + ' ' + self.prenume
#     def salariu_lunar(self):
#         return self.salariu
#     def salariu_anual(self):
#         return self.salariu_lunar() * 12
#     def marire_salariu(self):
#         procent_marire_salariala = self.salariu_lunar() / 100 * (100 + int(input('Ce procentaj va avea cresterea salariala? - ')))
#         salariul_dupa_marire_salariala = procent_marire_salariala
#         return salariul_dupa_marire_salariala
#
# angajat_1 = Angajat('Pop', 'Crina', 5000)
# angajat_2 = Angajat('Albescu', 'Adelin', 7000)
#
# # angajat_1.descrie()
# # print(angajat_1.nume_complet())
# # print(angajat_1.salariu_lunar())
# # print(angajat_1.salariu_anual())
# # print(angajat_1.marire_salariu())
#
# print(22 * '*')
#
# angajat_2.descrie()
# print(angajat_2.nume_complet())
# print(angajat_2.salariu_lunar())
# print(angajat_2.salariu_anual())
# print(angajat_2.marire_salariu())

# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

class Cont():
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')

    def debitare_cont(self):
        self.sold = self.sold - int(input('Introduceti suma pe care doriti sa o debitati: '))
        print(f'Soldul in urma debitarii este {self.sold}')

    def creditare_sold(self):
        self.sold = self.sold + int(input('Introduceti suma pe care doriti sa o depuneti in cont: '))
        print(f'Soldul in urma depunerii este {self.sold}')

persoana_1 = Cont(2222, 'Grigorescu Alex', 8000)
persoana_2 = Cont(4444, 'Pandora Grecu', 12000)

persoana_1.afisare_sold()
persoana_1.debitare_cont()
persoana_1.creditare_sold()

print(22 * '*')

persoana_2.afisare_sold()
persoana_2.debitare_cont()
persoana_2.creditare_sold()