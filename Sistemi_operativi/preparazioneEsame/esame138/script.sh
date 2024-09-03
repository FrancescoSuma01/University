#!/bin/bash

# Commento: [Cognome, Nome, Numero di matricola]

# Verifica che sia stato passato un argomento
if [ "$#" -ne 1 ]; then
    echo "Uso: $0 <stringa_base64>"
    exit 1
fi

# Stringa Base64 da decodificare
base64_string=$1

# Tabella di codifica Base64
base64_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# Converti la stringa Base64 in una sequenza binaria
binary_string=""
for (( i=0; i<${#base64_string}; i++ )); do
    char=${base64_string:$i:1}
    if [[ "$char" == "=" ]]; then
        # Trattiamo i caratteri "=" come padding e li ignoriamo nella decodifica
        continue
    fi
    index=$(expr index "$base64_chars" "$char")
    index=$((index - 1)) # Gli indici in base64_chars partono da 1, quindi sottraiamo 1
    binary_string+=$(printf "%06d" "$(echo "obase=2; $index" | bc)")
done

# Rimuovi gli zeri finali del padding
binary_string=${binary_string%0*}

# Converti la stringa binaria in una stringa ASCII
ascii_string=""
for (( i=0; i<${#binary_string}; i+=8 )); do
    byte=${binary_string:$i:8}
    ascii_string+=$(printf "\\x$(printf "%x" "$((2#$byte))")")
done

# Mostra la stringa decodificata
echo -e "$ascii_string"
