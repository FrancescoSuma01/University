def ordina (vec):
    for i in range(len(vec)):
        for j in range(i+1, len(vec)):
            if vec[i] > vec[j]:
                t = vec[i]
                vec[i] = vec[j]
                vec[j] = t

    return vec


lista = [ 20, 50, 10, 70, 90, 30, 20, 0]

print(f"La lista non ordinata è: \n\n  {lista} \n\nmentre la lista ordinata è: \n\n  {ordina(lista)}")