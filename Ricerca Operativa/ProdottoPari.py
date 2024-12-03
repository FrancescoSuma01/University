n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))
n3 = int(input("Inserisci il terzo numero: "))

prodotto = n1 * n2 * n3

if (prodotto%2 == 0):
    print(f"Il prodotto tra {n1}, {n2} e {n3} da come risultato {prodotto} è pari")
else:
    print(f"Il prodotto tra {n1}, {n2} e {n3} da come risultato {prodotto} è dispari")