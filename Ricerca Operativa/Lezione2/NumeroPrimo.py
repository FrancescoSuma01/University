def primo(numero):
    for divisore in range(2, numero):
        if numero % divisore == 0:
            return False
    return True

numero = int(input("Inserisci il numero da verificare: "))

isPrimo = primo(numero)

if isPrimo:
    print(f"{numero} è un numero primo")
else:
    print(f"{numero} non è un numero primo")