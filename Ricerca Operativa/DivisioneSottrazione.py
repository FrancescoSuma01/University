# Input dei numeri
dividendo = int(input("Inserisci il dividendo: "))
divisore = int(input("Inserisci il divisore: "))

# Controllo che il divisore sia positivo
if divisore == 0:
    print("Errore: la divisione per zero non è definita.")
else:
    quoziente = 0
    resto = dividendo

    # Sottrazioni ripetute
    while resto >= divisore:
        resto -= divisore
        quoziente += 1

    # Risultati
    print(f"Il quoziente della divisione intera tra {dividendo} e {divisore} è {quoziente}")
    print(f"Il resto della divisione è {resto}")
