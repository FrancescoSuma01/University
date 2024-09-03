#!/bin/bash

# Commento: [Cognome, Nome, Numero di matricola]

# Verifica che siano stati forniti esattamente due argomenti
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <stringa_hex1> <stringa_hex2>"
    exit 1
fi

# Assegna gli argomenti a variabili
hex1=$1
hex2=$2

# Funzione per convertire una stringa esadecimale in un numero decimale
hex_to_dec() {
    local hex_value=$1
    echo "$((16#$hex_value))"
}

# Funzione per convertire un numero decimale in una stringa esadecimale
dec_to_hex() {
    local dec_value=$1
    printf "%X\n" "$dec_value"
}

# Trova la lunghezza delle stringhe esadecimali
len1=${#hex1}
len2=${#hex2}

# Trova la lunghezza massima tra le due stringhe
max_len=$((len1 > len2 ? len1 : len2))

# Aggiungi zeri iniziali per fare in modo che le due stringhe abbiano la stessa lunghezza
hex1=$(printf "%0${max_len}X" "$((16#$hex1))")
hex2=$(printf "%0${max_len}X" "$((16#$hex2))")

# Calcola l'XOR bit a bit
xor_result=""
for (( i=0; i<max_len; i+=2 )); do
    byte1="${hex1:$i:2}"
    byte2="${hex2:$i:2}"
    byte1_dec=$(hex_to_dec "$byte1")
    byte2_dec=$(hex_to_dec "$byte2")
    xor_byte_dec=$((byte1_dec ^ byte2_dec))
    xor_result+=$(printf "%02X" "$xor_byte_dec")
done

# Mostra il risultato
echo "$xor_result"
