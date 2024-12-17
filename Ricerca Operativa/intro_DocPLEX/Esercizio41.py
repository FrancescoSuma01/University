'''
prodotti : E1 - E2 - E3 - E4
reparti : 3
operai : 100 (40 reparto 1, 35 reparto 2, 25reparto 3)
ore di lavoro operaio : 8 ore al giorno per 5 giorni a settimana

|                   |   E1  |   E2  |   E3  |   E4  |
|-------------------|-------|-------|-------|-------|
|    Reparto 1      |   1   |  1.5  |  0.5  |  1.6  |
|    Reparto 2      |  1.2  |  1.3  |  0.6  |  1    |
|    Reparto 3      |  0.8  |  1.7  |  0.7  |  1.3  |
|-------------------|-------|-------|-------|-------|
| Prezzo di vendita |  800  | 1200  |  950  | 1100  |

Richiesta : E1 = 1000
            E2 = 600
            E3 = 300
            E4 = 200
            max Z

max Z = 800 (x11 + x12 + x13) + 1200 (x21 + x22 + x23) + 950 (x31 + x32 + x33) + 1100 (x41 + x42 + x43)

s.v. :  + + + Vincoli di capacità + + +
        1 x11 + 1.5 x21 + 0.5 x31 + 1.6 x41 <= 40 (operai rep. 1) * 5(giorni a settimana) * 8 (ore al giorno)
        1.2 x12 + 1.3 * x22 + 0.6 * x32 + x42 <= 35 (operai rep. 2) * 5(giorni a settimana) * 8 (ore al giorno)
        0.8 * x13 + 1.7 * x23 + 0.7 * x33 + 1.3 * x43 <= 25 (operai rep. 3) * 5(giorni a settimana) * 8 (ore al giorno)
        
        + + + Vincoli di domanda + + +
        x11 + x12 + x13 >= 1000
        x21 + x22 + x23 >= 600
        x31 + x32 + x33 >= 300
        x41 + x42 + x43 >= 200
'''

import docplex.mp.model as cplex

# creazione del modello
m = cplex.Model("Esercizio_41")

# definizione delle variabili decisionali
x11 = m.integer_var(name="x11")
x12 = m.integer_var(name="x12")
x13 = m.integer_var(name="x13")
x21 = m.integer_var(name="x21")
x22 = m.integer_var(name="x22")
x23 = m.integer_var(name="x23")
x31 = m.integer_var(name="x31")
x32 = m.integer_var(name="x32")
x33 = m.integer_var(name="x33")
x41 = m.integer_var(name="x41")
x42 = m.integer_var(name="x42")
x43 = m.integer_var(name="x43")

# definizione della funzione obiettivo
m.maximize(800 * (x11 + x12 + x13) + 1200 * (x21 + x22 + x23) + 950 * (x31 + x32 + x33) + 1100 * (x41 + x42 + + x43))

# definizione dei vincoli
m.add_constraint(x11 + 1.5 * x21 + 0.5 * x31 + 1.6 * x41 <= 40 * 40 )
m.add_constraint(1.2 * x12 + 1.3 * x22 + 0.6 * x32 + x42 <= 35 * 40 )
m.add_constraint(0.8 * x13 + 1.7 * x23 + 0.7 * x33 + 1.3 * x43 <= 25 * 40)
m.add_constraint(x11 + x12 + x13 >= 1000)
m.add_constraint(x21 + x22 + x23 >= 600)
m.add_constraint(x31 + x32 + x33 >= 300)
m.add_constraint(x41 + x42 + x43 >= 200)

# risolvo
print(" - - - Stampa delle informazioni del modello - - -")
m.print_information()

print()

s = m.solve(log_output=True)

print()

print("- - - Stampa della soluzione ottima - - -")
print(s)