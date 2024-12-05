def trasposta(matrice):
    """
    Calcola la trasposta di una matrice.
    La trasposta scambia righe e colonne.
    """
    righe = len(matrice)
    colonne = len(matrice[0])
    
    # Crea una matrice vuota per la trasposta
    matrice_trasposta = [[None for _ in range(righe)] for _ in range(colonne)]
    
    # Scambia righe e colonne
    for i in range(righe):
        for j in range(colonne):
            matrice_trasposta[j][i] = matrice[i][j]
    
    return matrice_trasposta


def input_matrice():
    """
    Permette di inserire una matrice da input.
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
                    if len(riga) != colonne:
                        print(f"Errore: hai inserito {len(riga)} valori, ma ne servono {colonne}. Riprova.")
                    else:
                        matrice.append(riga)  # Accetta stringhe direttamente
                        break
            
            return matrice
        
        except ValueError:
            print("Errore: assicurati di inserire un numero valido per righe e colonne. Riprova.")


# Input della matrice
print("Inserisci una matrice (può contenere numeri o stringhe):")
matrice = input_matrice()

if matrice:
    print("\nMatrice originale:")
    for riga in matrice:
        print(riga)

    # Calcola la trasposta
    matrice_trasposta = trasposta(matrice)
    
    print("\nMatrice trasposta:")
    for riga in matrice_trasposta:
        print(riga)
else:
    print("\nErrore: non è stato possibile creare la matrice.")
