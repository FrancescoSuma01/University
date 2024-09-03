#!/bin/bash

# Commento: [Cognome, Nome, Numero di matricola]
# File di log
log_file="process_log.txt"

# Cancella il file di log se già esiste
> "$log_file"

# Salva l'elenco iniziale dei processi (PID) in un array
initial_pids=$(ps -e -o pid --no-headers)

# Funzione per registrare i nuovi processi e il loro parent
log_new_processes() {
    # Ottieni la lista corrente dei processi con PID e PPID
    current_processes=$(ps -e -o pid,ppid,comm --no-headers)

    # Confronta i processi correnti con quelli iniziali
    echo "$current_processes" | while read -r pid ppid comm; do
        # Verifica se il processo è nuovo (non era presente all'avvio dello script)
        if ! echo "$initial_pids" | grep -qw "$pid"; then
            # Se il processo è nuovo, lo registra nel file di log
            echo "Il processo $ppid ha lanciato il nuovo processo $pid ($comm)" >> "$log_file"
        fi
    done
}

# In loop per continuare a registrare nuovi processi
while true; do
    log_new_processes
    sleep 2  # Intervallo di controllo (può essere regolato a piacimento)
done
