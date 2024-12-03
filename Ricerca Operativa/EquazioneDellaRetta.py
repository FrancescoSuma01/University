# Input delle coordinate dei due punti
x1 = float(input("Inserisci la coordinata x del primo punto: "))
y1 = float(input("Inserisci la coordinata y del primo punto: "))
x2 = float(input("Inserisci la coordinata x del secondo punto: "))
y2 = float(input("Inserisci la coordinata y del secondo punto: "))

# Controllo se la retta è verticale
if x1 == x2:
    print(f"La retta è verticale e la sua equazione è: x = {x1}")
else:
    # Calcolo del coefficiente angolare m
    m = (y2 - y1) / (x2 - x1)
    # Calcolo dell'intercetta q
    q = y1 - m * x1
    # Stampa dell'equazione della retta
    print(f"L'equazione della retta è: y = {m:.2f}x + {q:.2f}")