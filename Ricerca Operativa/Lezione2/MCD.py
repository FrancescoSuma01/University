def MCD (a,b):
    while b != 0:
        a, b = b, a % b  # Assegna a b il resto della divisione di a per b
    return a

n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero:"))

mcd = MCD(n1, n2)

print(f"Il risultato del massimo comune divisore tra {n1} e {n2} è pari a {mcd}")