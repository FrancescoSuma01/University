#!/bin/bash

# Commento: [Cognome, Nome, Numero di matrico

# Crea una directory temporanea per memorizzare gli hash dei file
temp_dir=$(mktemp -d)
temp_hashes="$temp_dir/file_hashes.txt"
temp_duplicates="$temp_dir/duplicates.txt"

# Trova tutti i file nelle directory specificate e calcola il loro hash
while IFS= read -r dir; do
    if [ -d "~/Documents/SO2024/preparazioneEsame/esame4" ]; then
        find "~/Documents/SO2024/preparazioneEsame/esame4" -type f -exec sha256sum {} + >> "$temp_hashes"
    else
        echo "La directory $dir non esiste o non è una directory."
    fi
done < "$dir_file"

# Trova i file duplicati basandosi sugli hash
echo "Trovando file duplicati..."
sort "$temp_hashes" | uniq -d -w 64 > "$temp_duplicates"

# Proponi l'eliminazione dei file duplicati all'utente
if [ -s "$temp_duplicates" ]; then
    echo "File duplicati trovati:"
    cat "$temp_duplicates"
    echo "Vuoi eliminare i file duplicati? (y/n)"
    read -r response
    if [ "$response" = "y" ]; then
        awk '{print $2}' "$temp_duplicates" | while read -r file; do
            echo "Eliminando $file"
            rm -f "$file"
        done
        echo "Eliminazione completata."
    else
        echo "Nessun file è stato eliminato."
    fi
else
    echo "Nessun file duplicato trovato."
fi

# Pulizia: rimuove la directory temporanea
rm -r "$temp_dir"



