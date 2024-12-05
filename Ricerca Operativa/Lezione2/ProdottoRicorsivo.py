def prodotto(a, b):
    if a == 0 or b == 0:
        return 0  # Caso base: la somma dei numeri da 1 a 0 è 0
    else:
        return a + prodotto(a, b-1)

n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))

print(f"Il risultato della prodotto è: {prodotto(n1, n2)}")