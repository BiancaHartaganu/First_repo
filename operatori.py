'''
Operatori:
aritmetici: +,-,*,/,%
de comparare: <>,==, !=, >=,<=,
logici: and, or, !(not-inverseaza raspunsul)
'''

a=3
b=5
print(a+b)
print(a==b) # 3 e egal cu 5? False
print(a<b and a<4)
print(a<b or a<2)

# cu mama sau cu tata sau (cu bunicu si bunica)
mama = True
tata = False
bunicu = True
bunica = True
print(mama and tata or (bunicu and bunica))
