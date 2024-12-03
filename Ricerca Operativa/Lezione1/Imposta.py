"""
Su una somma di denaro si vuole applicare un'imposta progressiva secondo lo schema seguente:
 - da 0 a 5000 euro: imposta del 10%
 - dopo i 5000 e fino a 15000 euro: imposta del 20%
 - oltre i 15000 euro: imposta del 30%.
"""

denaro = float(input("Inserire la somma di denaro: "))
imposta = 0.0

if (denaro > 0 and denaro < 5000):
    imposta = denaro * 0.1
elif (denaro >= 5000 and denaro < 15000):
    imposta = denaro * 0.2
elif (denaro >= 15000):
    imposta = denaro * 0.3

print(f"L'imposta da applicare su {denaro} è pari a {imposta}, per un totale di {denaro + imposta}")