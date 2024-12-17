'''
P1 - P2 - P3 - P4 - P5  ==> Prodotti
M1 - M2  ==> Macchine

P1 = 250
P2 = 300
P3 = 500
P4 = 450
P5 = 180

___________________________________________
|      |  P1  |  P2  |  P3  |  P4  |  P5  |
|------|------|------|------|------|------|
|  M1  |  10  |  15  |   7  |  18  |   -  |
|------|------|------|------|------|------|
|  M2  |   9  |  13  |  20  |  -   |  20  |
-------------------------------------------

Per l'assemblagio di un singolo prodotto occorrono 18 ore di un operaio
4 x M1 + 3 M2 -> 5 Giorni a settimana per 16 ore al giorno
10 operai per l'assemblagio 5 giorni a settimana per 8 ore al giorno ciascuno

max  ->  250x1 + 300x2 + 500x3 + 450x4 + 180x5
s.t. ->  10x1 + 15x2 + 7x3 + 18x4 <= 320 (4M1 * 5giorni * 2turni * 8hturno)
         9x1 + 13x2 + 20x3 + 20x5 <= 240 (3M1 * 5giorni * 2turni * 8hturno)
         18(x1 + x2 + x3 + x4 + x5) <= 400 (10operai * 5giorni * 8hturno)

'''

import docplex.mp.model as cplex

m = cplex.Model("Esercizio_40")

# definizione delle variabili decisionali
x1 = m.continuous_var(name='x1')
x2 = m.continuous_var(name='x2')
x3 = m.continuous_var(name='x3')
x4 = m.continuous_var(name='x4')
x5 = m.continuous_var(name='x5')

# definizione della funzione obiettivo
m.maximize(250 * x1 + 300 * x2 + 500 * x3 + 450 * x4 + 180 * x5)

# dichiarazione dei vincoli
m.add_constraint(10 * x1 + 15 * x2 + 7 * x3 + 18 * x4 <= 320)
m.add_constraint(9 * x1 + 13 * x2 + 20 * x3 + 20 * x5 <= 240)
m.add_constraint(18 * (x1 + x2 + x3 + x4 + x5) <= 400)

# risolvo
print(" - - - Stampa delle informazioni del modello - - -")
m.print_information()

print()

s = m.solve(log_output=True)

print()

print("- - - Stampa della soluzione ottima - - -")
print(s)