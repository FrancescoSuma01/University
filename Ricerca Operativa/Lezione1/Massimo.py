n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))
n3 = int(input("Inserisci il terzo numero: "))

# Trova il massimo tra i tre numeri
if n1 >= n2 and n1 >= n3:
    print(f"Il numero massimo tra i tre è: {n1}")
    if n1 == n2 or n1 == n3:
        print("Ci sono numeri uguali al massimo.")
elif n2 >= n1 and n2 >= n3:
    print(f"Il numero massimo tra i tre è: {n2}")
    if n2 == n1 or n2 == n3:
        print("Ci sono numeri uguali al massimo.")
else:  # n3 >= n1 and n3 >= n2
    print(f"Il numero massimo tra i tre è: {n3}")
    if n3 == n1 or n3 == n2:
        print("Ci sono numeri uguali al massimo.")