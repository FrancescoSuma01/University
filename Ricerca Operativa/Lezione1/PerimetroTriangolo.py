import math as m

cateto1 = int(input("Inserisci le dimensioni del primo cateto: "))
cateto2 = int(input("Inserisci le dimensioni del secondo cateto: "))

ipotenusa = m.sqrt(m.pow(cateto1,2) + m.pow(cateto2,2))

print("Le dimensioni del triangolo sono:")
print(f"Cateto 1: {cateto1:.2f}")
print(f"Cateto 2: {cateto2:.2f}")
print(f"Ipotenusa: {ipotenusa:.2f}")

print("")

perimetro = cateto1 + cateto2 + ipotenusa

print(f"Il perimetro del triangolo è pari a: {perimetro:.2f}")