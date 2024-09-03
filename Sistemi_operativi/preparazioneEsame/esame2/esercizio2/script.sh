#!/bin/bash

# Ottieni l'ID dell'utente corrente
user_id=$(id -u)

# Inizializza il contatore
total_open_files=0

# Itera su tutti i processi dell'utente corrente
for pid in $(pgrep -u "$user_id"); do
    # Conta il numero di file aperti dal processo
    num_files=$(ls /proc/$pid/fd 2>/dev/null | wc -l)
    
    # Aggiunge al contatore totale
    total_open_files=$((total_open_files + num_files))
done

# Stampa il numero totale di file aperti
echo "Numero totale di file aperti dai processi dell'utente: $total_open_files"
