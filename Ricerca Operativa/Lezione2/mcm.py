def MCD (a,b):
    while b != 0:
        a, b = b, a % b  # Assegna a b il resto della divisione di a per b
    return a

def MCM (a, b):
    mcd = MCD(a, b)
    
    # Calcola e restituisce l'MCM usando la formula
    return abs(a * b) // mcd

n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))

mcm = MCM(n1, n2)

print(f"Il risultato del minimo comune multiplo tra {n1} e {n2} è pari a {mcm}")