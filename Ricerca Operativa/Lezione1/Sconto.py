"""
Sul prezzo di un prodotto viene praticato lo sconto del:
 - 3% se costa meno di 500 euro
 - 5% per prezzi superiori a 500 euro
Calcolare il prezzo da pagare.
"""

prezzo = float(input("Inserisci il prezzo: "))

if prezzo < 500:
    prezzo = prezzo - (prezzo * 0.03)
else:
    prezzo = prezzo - (prezzo * 0.05)

print(f"Applicando lo sconto il prezzo passa a: {prezzo}")