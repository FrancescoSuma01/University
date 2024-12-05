import math as m

def riempimentoVec():
    """
    Riempie un vettore con numeri forniti dall'utente.
    Ritorna una lista di numeri.
    """
    vec = []
    cont = 1
    while True:
        numero = input(f"Inserisci il {cont}° valore del vettore (lascia vuoto per terminare): ")
        if numero == "":  # Condizione per uscire dal ciclo
            break
        if numero.lstrip('-').replace('.', '', 1).isdigit():  # Controlla se è un numero valido
            vec.append(float(numero))  # Aggiunge il numero come float
            cont += 1
        else:
            print("Inserisci un numero valido.")
    return vec

def pNorma(vec, p):
    """
    Calcola la p-norma di un vettore.
    """
    newVec = [m.pow(abs(x), p) for x in vec]  # Usa una list comprehension per calcolare la potenza
    somma = sum(newVec)  # Somma i valori elevati
    return m.pow(somma, 1 / p)  # Eleva alla potenza 1/p

# Input del vettore
vec = riempimentoVec()

# Input del valore di p
while True:
    try:
        p = float(input("Inserisci il valore della p: "))
        if p > 0:
            break
        else:
            print("Il valore di p deve essere positivo.")
    except ValueError:
        print("Inserisci un numero valido per p.")

# Calcolo della p-norma
risultato = pNorma(vec, p)

# Output del risultato
print(f"La p-norma (p = {p}) è pari a {risultato:.2f}")
