p1 = [0, 0]
p2 = [0, 0]

p1[0] = int(input("Inserisci le coordinate del parametro x del punto 1: "))
p1[1] = int(input("Inserisci le coordinate del parametro y del punto 1: "))

p2[0] = int(input("Inserisci le coordinate del parametro x del punto 1: "))
p2[1] = int(input("Inserisci le coordinate del parametro y del punto 1: "))

pMedio = [0, 0]

pMedio[0] = (p2[0] + p1[0]) / 2
pMedio[1] = (p2[1] + p1[1]) / 2

print(f"Le coordinate del punto medio sono ({pMedio[0]}, {pMedio[1]})")