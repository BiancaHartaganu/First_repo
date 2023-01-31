masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for masina in range(len(masini)):
#     print(f'Masina mea preferata este {masini[masina]}')
#     masina += 1

# for masina in masini:
#     print(f'Masina mea preferata este {masina}')

# i = 0
# while i < len(masini):
#     print(f'Masina mea preferata este {masini[i]}')
#     i += 1

# for masina in range(len(masini)):
#   if masina in range(1,len(masini)-1):
#     masini[masina] = masini[masina].upper()
# else:
#   print(masini)

# for masina in masini:
#     print(f'Am gasit masina {masina}')
#     if masina == "Mercedes":
#         print('Am gasit masina aleasa de DVS')
#         break
# print(f'Am gasit masina {masina}, mai cautam')

# masini_lux = []
# for masina in masini:
#     if masina == "Trabant" or masina == "Lăstun":
#         continue
#     masini_lux.append(masina)
# for masina_lux in masini_lux:
#     print(f'S-ar putea sa va placa masina {masina_lux}')

# masini_vechi = []
#
# for masina in masini:
#     if masina == 'Lăstun':
#         masini_vechi.append('Lăstun')
#         masini[masini.index('Lăstun')] = 'Tesla'
#     if masina == 'Trabant':
#         masini_vechi.append('Trabant')
#         masini[masini.index('Trabant')] = 'Tesla'
# print(f'Masini vechi = {masini_vechi}')
# print(f'Masini noi = {masini}')

# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
#
# buget = 15000
#
# for masina, pret in pret_masini.items():
#   if pret <= buget:
#     print(f"Pentru un buget de sub {buget} euro puteți alege mașina {masina} la pretul de {pret} euro")

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

# numaratoare = 0
# for numar in numere:
#   if numar == 3:
#     numaratoare += 1
# print(f"Numărul 3 apare de {numaratoare} ori în listă.")

# suma = 0
# for numar in numere:
#   suma += numar
#
# print(f"Suma elementelor din listă este: {suma}")

# nr_mare = numere[0]
# for numar in numere:
#   if numar > nr_mare:
#     nr_mare = numar
# print(f"Cel mai mare număr din listă este: {nr_mare}")

for i, numar in enumerate(numere):
  if numar > 0:
    numere[i] = -numar
print(f"Noua listă este: {numere}")