#!/bin/bash

# Commento: [Cognome, Nome, Numero di matricola]

# Verifica del numero di parametri
if [ "$#" -ne 3 ]; then
    echo "Uso: $0 <file1> <file2> <bytes_da_ignorare>"
    exit 1
fi

# Parametri
file1=$1
file2=$2
skip_bytes=$3

# Verifica che i file esistano
if [ ! -f "$file1" ] || [ ! -f "$file2" ]; then
    echo "Uno o entrambi i file non esistono."
    exit 1
fi

# Crea versioni temporanee dei file senza l'intestazione
tail -c +$(($skip_bytes + 1)) "$file1" > /tmp/file1_trimmed
tail -c +$(($skip_bytes + 1)) "$file2" > /tmp/file2_trimmed

# Confronta i file senza l'intestazione
if cmp -s /tmp/file1_trimmed /tmp/file2_trimmed; then
    echo "I file hanno lo stesso contenuto indipendentemente dall'intestazione."
else
    echo "I file sono diversi anche dopo aver ignorato l'intestazione."
fi

# Pulizia: rimuove i file temporanei
rm /tmp/file1_trimmed /tmp/file2_trimmed



