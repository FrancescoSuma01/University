def scomposizione(n):
    """
    Scompone un numero in fattori primi.

    Parametri:
    - n (int): Il numero da scomporre.

    Ritorna:
    - list: Una lista di fattori primi, inclusi i duplicati.
    """
    fattori_primi = []
    divisore = 2
    
    while divisore * divisore <= n:  # Fino alla radice quadrata di n
        while n % divisore == 0:  # Se divisibile, aggiungi il divisore alla lista
            fattori_primi.append(divisore)
            n //= divisore
        divisore += 1
    
    # Se il numero è maggiore di 1, aggiungi l'ultimo fattore primo
    if n > 1:
        fattori_primi.append(n)
    
    return fattori_primi

# Funzione per stampare la scomposizione con esponenti
def stampa_scomposizione_con_esponenti(n):
    """
    Stampa la scomposizione di un numero in fattori primi, mostrando i fattori senza duplicati e con gli esponenti.
    """
    # Ottieni la lista dei fattori primi
    fattori_primi = scomposizione(n)
    
    # Usa un dizionario per contare quante volte ogni fattore appare
    fattori_con_esponenti = {}
    for fattore in fattori_primi:
        if fattore in fattori_con_esponenti:
            fattori_con_esponenti[fattore] += 1
        else:
            fattori_con_esponenti[fattore] = 1
    
    # Stampa i fattori con i rispettivi esponenti
    print(f"Scomposizione di {n}:")
    for fattore, esponente in fattori_con_esponenti.items():
        print(f"{fattore}^{esponente}")

# Esempio di utilizzo:
numero = int(input("Inserisci un numero da scomporre: "))
stampa_scomposizione_con_esponenti(numero)
