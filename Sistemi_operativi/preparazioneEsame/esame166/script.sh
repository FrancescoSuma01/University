#!/bin/bash

# Commento: [Cognome, Nome, Numero di matricola]

# Funzione per mostrare l'uso dello script
usage() {
    echo "Uso: $0 [-d] <SEQUENZA> <FILE> ..."
    exit 1
}

# Gestione degli argomenti
decimal_output=false

# Controlla se il primo argomento è l'opzione -d
if [ "$1" == "-d" ]; then
    decimal_output=true
    shift
fi

# Verifica che siano forniti almeno due argomenti (sequenza e almeno un file)
if [ "$#" -lt 2 ]; then
    usage
fi

# La sequenza da cercare
sequence=$1
shift

# Converti la sequenza esadecimale in un formato binario
sequence_bin=$(echo "$sequence" | xxd -r -p)

# Cerca la sequenza in ogni file
for file in "$@"; do
    if [ ! -f "$file" ]; then
        echo "Il file $file non esiste."
        continue
    fi

    # Trova la sequenza nel file
    offset=0
    while read -r -d '' -n 1 char; do
        if [[ "$char" == "$(printf '%b' "$sequence_bin")" ]]; then
            echo "$file: $(printf '%x' "$offset")"
            if $decimal_output; then
                echo "$file: $offset"
            fi
        fi
        offset=$((offset + 1))
    done < <(dd if="$file" bs=1 2>/dev/null)
done



