def ordina(vec):
    """
    Ordina un vettore in ordine crescente.
    """
    for i in range(len(vec)):
        for j in range(i + 1, len(vec)):
            if vec[i] > vec[j]:
                # Scambia i valori
                vec[i], vec[j] = vec[j], vec[i]
    return vec


def unisci(vec1, vec2):
    """
    Unisce due liste in una sola lista.
    """
    vec3 = []  # Crea una lista vuota

    # Aggiungi tutti gli elementi della prima lista
    for i in range(len(vec1)):
        vec3.append(vec1[i])

    # Aggiungi tutti gli elementi della seconda lista
    for i in range(len(vec2)):
        vec3.append(vec2[i])

    return vec3


# Liste di esempio
lista1 = [0, 10, 50, 90]
lista2 = [20, 30, 40, 60, 70, 80]

# Ordina entrambe le liste
lista1_ordinata = ordina(lista1)
lista2_ordinata = ordina(lista2)

# Unisci le liste ordinate
unione = unisci(lista1_ordinata, lista2_ordinata)

# Ordina l'unione
unione_ordinata = ordina(unione)

# Stampa i risultati
print(f"Le due liste sono:\n\n  {lista1} \n\n  {lista2}")
print(f"\nOrdinate diventano:\n\n  {lista1_ordinata} \n\n  {lista2_ordinata}")
print(f"\nLa loro unione ordinata dà:\n\n  {unione_ordinata}")
