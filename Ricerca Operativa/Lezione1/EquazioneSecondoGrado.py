import math as m

# Introduzione
print("L'equazione richiesta è della seguente forma:")
print("ax^2 + bx + c = 0")
print("")

# Input dei coefficienti
x2 = float(input("Inserisci il coefficiente di x^2 (a): "))
x = float(input("Inserisci il coefficiente di x (b): "))
termineNoto = float(input("Inserisci il termine noto (c): "))

# Calcolo del discriminante
delta = m.pow(x, 2) - 4 * x2 * termineNoto

# Controllo sul discriminante
if delta > 0:
    # Due soluzioni reali distinte
    y1 = (-x - m.sqrt(delta)) / (2 * x2)
    y2 = (-x + m.sqrt(delta)) / (2 * x2)
    print(f"L'equazione data è: {x2}x^2 + {x:+}x + {termineNoto:+} = 0")
    print("Le soluzioni ottenute sono:")
    print(f"x_1: {y1:.2f}")
    print(f"x_2: {y2:.2f}")
elif delta == 0:
    # Una soluzione reale doppia
    y1 = -x / (2 * x2)
    print(f"L'equazione data è: {x2}x^2 + {x:+}x + {termineNoto:+} = 0")
    print("L'equazione ha una soluzione reale doppia:")
    print(f"x: {y1:.2f}")
else:
    # Nessuna soluzione reale
    print(f"L'equazione data è: {x2}x^2 + {x:+}x + {termineNoto:+} = 0")
    print("Non ci sono soluzioni reali perché il discriminante è negativo.")
