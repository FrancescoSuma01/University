#!/bin/bash

# Commento: [Cognome, Nome, Numero di matricola]

# Verifica che siano stati forniti due argomenti
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <file_sorgente> <file_destinazione>"
    exit 1
fi

# Assegna gli argomenti a variabili
file_sorgente=$1
file_destinazione=$2

# Verifica se il file di origine esiste
if [ ! -f "$file_sorgente" ]; then
    echo "Il file di origine $file_sorgente non esiste."
    exit 1
fi

# Copia il file di origine nel file di destinazione
cp "$file_sorgente" "$file_destinazione"

# Verifica se la copia è andata a buon fine
if [ $? -eq 0 ]; then
    # Recupera la data di modifica del file di origine
    data_modifica=$(stat -c %y "$file_sorgente")
    
    # Imposta la data di modifica del file di destinazione
    touch -d "$data_modifica" "$file_destinazione"

    echo "File copiato e data di modifica conservata."
else
    echo "Errore nella copia del file."
fi



