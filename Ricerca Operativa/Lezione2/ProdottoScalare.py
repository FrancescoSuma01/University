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

def prodottoScalare(vec1, vec2):
    prodotto = 0

    for i in range(0, len(vec1)):
        prodotto = prodotto + (vec1[i] * vec2[i])

    return prodotto    

vec1 = riempimentoVec()

print()
print("Passaimo ora al secondo vettore: ")
print()

vec2 = riempimentoVec()

prodotto = prodottoScalare(vec1, vec2)

print(f"Il prodotto scalare tra i vettori \n \n  v1 = {vec1} \n \n  v2 = {vec2} \n \nda come risultato: {prodotto}")