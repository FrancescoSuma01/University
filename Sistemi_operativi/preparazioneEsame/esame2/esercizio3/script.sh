#!/bin/bash

# Commento: [Cognome, Nome, Numero di matricola]

# Controlla se è stata passata una directory come argomento
if [ -z "$1" ]; then
    echo "Uso: $0 <directory>"
    exit 1
fi

# Inizializza le variabili per le somme aggregate
total_lines=0
total_words=0
total_bytes=0

# Funzione per contare le righe, parole e byte nei file
count_wc() {
    local file="$1"
    # Usa wc per ottenere il conteggio di righe, parole e byte
    local counts
    counts=$(wc "$file")
    
    # Estrae i singoli valori
    local lines=$(echo "$counts" | awk '{print $1}')
    local words=$(echo "$counts" | awk '{print $2}')
    local bytes=$(echo "$counts" | awk '{print $3}')
    
    # Aggiunge i valori alle variabili aggregate
    total_lines=$((total_lines + lines))
    total_words=$((total_words + words))
    total_bytes=$((total_bytes + bytes))
}

# Ricorsione attraverso la directory
process_directory() {
    for item in "$1"/*; do
        if [ -d "$item" ]; then
            # Se è una directory, chiama la funzione ricorsivamente
            process_directory "$item"
        elif [ -f "$item" ]; then
            # Se è un file, conta le righe, parole e byte
            count_wc "$item"
        fi
    done
}

# Avvia la ricorsione dalla directory specificata
process_directory "$1"

# Stampa i risultati aggregati
echo "Totale:"
echo "Righe: $total_lines"
echo "Parole: $total_words"
echo "Byte: $total_bytes"


