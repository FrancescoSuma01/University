#!/bin/bash

# Commento: [Cognome, Nome, Numero di matricola]
# Controlla se è stata passata una directory come argomento
if [ -z "$1" ]; then
    echo "Uso: $0 <directory>"
    exit 1
fi

# Funzione per convertire i nomi dei file in minuscolo ricorsivamente
rename_files() {
    for file in "$1"/*; do
        if [ -d "$file" ]; then
            # Se è una directory, chiama la funzione ricorsivamente
            rename_files "$file"
        elif [ -f "$file" ]; then
            # Se è un file, converte il nome in minuscolo
            dir=$(dirname "$file")
            base=$(basename "$file")
            lower_base=$(echo "$base" | tr 'A-Z' 'a-z')
            if [ "$base" != "$lower_base" ]; then
                mv "$file" "$dir/$lower_base"
            fi
        fi
    done
}

# Chiamata alla funzione passando la directory specificata
rename_files "$1"
