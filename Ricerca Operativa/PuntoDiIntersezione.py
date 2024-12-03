# Input dei parametri delle due rette
m1 = float(input("Inserisci il coefficiente angolare della prima retta (m1): "))
q1 = float(input("Inserisci l'intercetta della prima retta (q1): "))
m2 = float(input("Inserisci il coefficiente angolare della seconda retta (m2): "))
q2 = float(input("Inserisci l'intercetta della seconda retta (q2): "))

# Controllo del tipo di rette
if m1 == m2:
    if q1 == q2:
        print("Le rette sono coincidenti e hanno infiniti punti di intersezione.")
    else:
        print("Le rette sono parallele e non hanno punti di intersezione.")
else:
    # Calcolo del punto di intersezione
    x = (q2 - q1) / (m1 - m2)
    y = m1 * x + q1
    print(f"Il punto di intersezione delle due rette è: ({x:.2f}, {y:.2f})")