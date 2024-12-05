def input_matrice():
    """
    Permette di inserire una matrice da input accettando solo numeri interi (positivi e negativi).
    """
    while True:
        try:
            righe = int(input("Inserisci il numero di righe della matrice: "))
            colonne = int(input("Inserisci il numero di colonne della matrice: "))
            
            matrice = []
            
            print("Inserisci gli elementi della matrice riga per riga (separati da spazi):")
            for i in range(righe):
                while True:
                    riga = input(f"Riga {i + 1}: ").split()
                    
                    # Verifica che ogni elemento della riga sia un numero intero (positivo o negativo)
                    if len(riga) != colonne:
                        print(f"Errore: hai inserito {len(riga)} valori, ma ne servono {colonne}. Riprova.")
                    elif all(is_integer(val) for val in riga):  # Controlla che tutti gli elementi siano numeri interi
                        matrice.append([int(val) for val in riga])  # Converte tutti gli elementi in interi
                        break
                    else:
                        print("Errore: tutti gli elementi devono essere numeri interi (positivi o negativi). Riprova.")
            
            return matrice
        
        except ValueError:
            print("Errore: assicurati di inserire un numero valido per righe e colonne. Riprova.")

def is_integer(val):
    """
    Funzione di utilità per verificare se una stringa rappresenta un numero intero (positivo o negativo).
    """
    try:
        int(val)  # Prova a convertire il valore in intero
        return True
    except ValueError:
        return False


def prodotto(matrice1, matrice2):
    """
    Calcola il prodotto di due matrici.
    La funzione restituisce la matrice prodotto risultante.
    """
    # Verifica che il numero di colonne della prima matrice sia uguale al numero di righe della seconda matrice
    if len(matrice1[0]) != len(matrice2):
        raise ValueError("Il numero di colonne della prima matrice deve essere uguale al numero di righe della seconda matrice.")
    
    # Crea una matrice vuota per il risultato del prodotto
    matrice_prodotto = []
    
    # Calcolo del prodotto matrice
    for i in range(len(matrice1)):  # Itera sulle righe della prima matrice
        riga_prodotto = []
        for j in range(len(matrice2[0])):  # Itera sulle colonne della seconda matrice
            somma = 0
            for k in range(len(matrice2)):  # Calcola la somma dei prodotti
                somma += matrice1[i][k] * matrice2[k][j]
            riga_prodotto.append(somma)
        matrice_prodotto.append(riga_prodotto)
    
    return matrice_prodotto


def main():
    print("Inserisci la prima matrice (solo numeri interi):")
    matrice1 = input_matrice()

    print()
    print("----------------------------------------------------------------------")
    print()

    # Verifica che il numero di colonne della prima matrice sia uguale al numero di righe della seconda matrice
    righe2 = int(input("Inserisci il numero di righe della seconda matrice: "))
    colonne2 = int(input("Inserisci il numero di colonne della seconda matrice: "))

    if len(matrice1[0]) != righe2:
        print(f"Errore: il numero di colonne della prima matrice ({len(matrice1[0])}) deve essere uguale al numero di righe della seconda matrice ({righe2}).")
        return

    print("----------------------------------------------------------------------")
    print()

    print("Inserisci gli elementi della seconda matrice (solo numeri interi):")
    matrice2 = []
    for i in range(righe2):
        while True:
            riga = input(f"Riga {i + 1}: ").split()
            
            # Verifica che ogni elemento della riga sia un numero intero (positivo o negativo)
            if len(riga) != colonne2:
                print(f"Errore: hai inserito {len(riga)} valori, ma ne servono {colonne2}. Riprova.")
            elif all(is_integer(val) for val in riga):  # Controlla che tutti gli elementi siano numeri interi
                matrice2.append([int(val) for val in riga])  # Converte tutti gli elementi in interi
                break
            else:
                print("Errore: tutti gli elementi devono essere numeri interi (positivi o negativi). Riprova.")
    
    print()
    print("----------------------------------------------------------------------")
    print()

    if matrice1 and matrice2:
        print("\nPrima matrice originale:")
        for riga in matrice1:
            print(riga)

        print("\nSeconda matrice originale:")
        for riga in matrice2:
            print(riga)

        try:
            # Calcola il prodotto delle matrici
            matriceProdotto = prodotto(matrice1, matrice2)
        
            print("\nMatrice prodotto:")
            for riga in matriceProdotto:
                print(riga)
        except ValueError as e:
            print(f"\nErrore: {e}")
    else:
        print("\nErrore: non è stato possibile creare la matrice.")


if __name__ == "__main__":
    main()
