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


def somma(matrice1, matrice2):
    """
    Somma due matrici della stessa dimensione.
    La funzione restituisce la matrice somma risultante.
    """
    # Verifica che le due matrici abbiano le stesse dimensioni
    if len(matrice1) != len(matrice2) or len(matrice1[0]) != len(matrice2[0]):
        raise ValueError("Le matrici devono avere la stessa dimensione.")
    
    # Crea una nuova matrice per il risultato
    matrice_somma = []
    
    # Somma elemento per elemento
    for i in range(len(matrice1)):
        riga_somma = []
        for j in range(len(matrice1[0])):
            riga_somma.append(matrice1[i][j] + matrice2[i][j])
        matrice_somma.append(riga_somma)
    
    return matrice_somma


def main():
    print("Inserisci la prima matrice (solo numeri interi):")
    matrice1 = input_matrice()

    print()
    print("----------------------------------------------------------------------")
    print()

    print("Inserisci la seconda matrice (solo numeri interi):")
    matrice2 = input_matrice()

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

        # Calcola la somma
        matriceSomma = somma(matrice1, matrice2)
        
        print("\nMatrice somma:")
        for riga in matriceSomma:
            print(riga)
    else:
        print("\nErrore: non è stato possibile creare la matrice.")


if __name__ == "__main__":
    main()
