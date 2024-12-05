import os

def occorrenza(file_content, lettera):
    """
    Calcola la percentuale di presenza di una lettera nel contenuto del file.
    """
    cont = file_content.count(lettera)  # Conta le occorrenze della lettera
    percentuale = (cont / len(file_content)) * 100 if len(file_content) > 0 else 0  # Calcola la percentuale
    return percentuale

def main():
    nomeFile = input("Inserisci il nome del file su cui effettuare il conteggio: ")

    if os.path.exists(nomeFile):  # Verifica che il file esista
        with open(nomeFile, 'r') as file:
            file_content = file.read().lower()  # Legge il file e converte tutto in minuscolo

        percentuali = {}

        # Calcola la percentuale per ogni lettera dell'alfabeto
        for lettera in range(ord('a'), ord('z') + 1):
            lettera_corrente = chr(lettera)
            percentuali[lettera_corrente] = occorrenza(file_content, lettera_corrente)

        print("\nLa frequenza relativa percentuale delle lettere dell'alfabeto è:")
        for lettera, perc in percentuali.items():
            print(f"{lettera}: {perc:.2f}%")

    else:
        print("Errore: il file specificato non esiste.")

if __name__ == "__main__":
    main()
