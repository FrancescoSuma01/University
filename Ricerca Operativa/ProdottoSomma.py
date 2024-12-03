n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))

if n1 == 0 or n2 == 0:
    print(f"Il prodotto tra {n1} e {n2} è 0")
else:
    somma = 0

    # Calcolo del prodotto usando solo somme
    for i in range(abs(n2)):  # Itera per il valore assoluto di n2
        somma += n1

    # Gestione del segno del risultato
    if n2 < 0:
        somma = -somma

    print(f"Il prodotto tra {n1} e {n2} è {somma}")