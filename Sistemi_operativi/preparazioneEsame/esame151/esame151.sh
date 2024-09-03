#!/bin/bash

# Commento: [Cognome, Nome, Numero di matricola]

# Pacchetto codificato in base64
encoded_packet="RQAAVJ3/AABAAQAAwKiyNwgICAgIAE01klYAAGEusTkABhsDCAkKCwwNDg8QERITFBUWFxgZGhscHR4fICEiIyQlJicoKSorLC0uLzAxMjM0NTY3"

# Decodifica del pacchetto
decoded_packet=$(echo "$encoded_packet" | base64 -d)

# Estrazione dell'indirizzo IP del mittente (byte 13-16)
src_ip=$(echo "$decoded_packet" | dd bs=1 skip=12 count=4 2>/dev/null | od -An -t u1 | tr -s ' ' '.' | sed 's/^\.//')

# Estrazione dell'indirizzo IP del destinatario (byte 17-20)
dest_ip=$(echo "$decoded_packet" | dd bs=1 skip=16 count=4 2>/dev/null | od -An -t u1 | tr -s ' ' '.' | sed 's/^\.//')

# Stampa degli indirizzi IP in notazione decimale quadripuntata
echo "Indirizzo IP del mittente: $src_ip"
echo "Indirizzo IP del destinatario: $dest_ip"
