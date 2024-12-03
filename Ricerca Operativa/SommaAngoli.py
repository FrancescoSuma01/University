# Input delle misure dei tre angoli in secondi
angolo1 = int(input("Inserisci il primo angolo in secondi: "))
angolo2 = int(input("Inserisci il secondo angolo in secondi: "))
angolo3 = int(input("Inserisci il terzo angolo in secondi: "))

# Somma degli angoli in secondi
somma_secondi = angolo1 + angolo2 + angolo3

# Conversione in gradi, primi e secondi
gradi = somma_secondi // 3600  # Ogni 3600 secondi è un grado
resto_secondi = somma_secondi % 3600
primi = resto_secondi // 60  # Ogni 60 secondi è un primo
secondi = resto_secondi % 60

# Output
print(f"L'angolo risultante è: {gradi}°, {primi}', {secondi}''")
