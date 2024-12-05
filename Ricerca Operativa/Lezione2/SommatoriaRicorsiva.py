def sommatoria(n):
    if n == 0:
        return 0  # Caso base: la somma dei numeri da 1 a 0 è 0
    else:
        return n + sommatoria(n - 1)


numero = int(input("Inserisci il numero di cui calcolare la somma: "))

print(f"Il risultato della sommatoria è: {sommatoria(numero)}")