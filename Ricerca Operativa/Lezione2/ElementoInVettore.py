def ricerca(vec, elem):
    """
    Cerca un elemento in un vettore e restituisce la sua posizione (indice).
    Restituisce -1 se l'elemento non è presente.
    """
    for i in range(len(vec)):
        # Prova a interpretare l'input come numero, se possibile
        if elem.isdigit():
            elem = int(elem)  # Converte in intero
        elif elem.replace('.', '', 1).isdigit():
            elem = float(elem)  # Converte in float

        if elem == vec[i]:
            return i
    return -1  # Restituisci -1 se l'elemento non è trovato

# Lista di esempio
lista = ['1', 2, 3, 4, "cinque", 6, 7, 8, 9, "dieci"]

# Input dell'utente
elemento = input("Inserisci l'elemento da ricercare nella lista: ")

# Cerca l'elemento nella lista
presente = ricerca(lista, elemento)

# Stampa il risultato
if presente != -1:
    print(f"L'elemento è presente nella lista alla posizione: {presente}")
else:
    print("L'elemento non è presente nella lista.")
