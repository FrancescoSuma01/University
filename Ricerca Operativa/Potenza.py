base = int(input("Inserisci la base: "))
esponente = int(input("Inserisci l'esponente: "))

if base == 0 and esponente == 0:
    print("Il risultato della potenza inserita è undefined.")
elif esponente == 0:
    print("Poiché l'esponente è pari a 0, il risultato è 1.")
else:
    potenza = 1  # Inizializzazione a 1, poiché è l'elemento neutro della moltiplicazione
    for i in range(esponente):
        potenza *= base  # Moltiplica successivamente la base
    print(f"Il risultato di {base} elevato a {esponente} è {potenza}")
