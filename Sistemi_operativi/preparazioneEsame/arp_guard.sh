#!/bin/bash

# Commento: [Cognome, Nome, Numero di matricola]

# Funzione per mostrare l'uso dello script
usage() {
    echo "Uso: $0 [-b] [-t SEC]"
    echo "  -b        Riproduce un suono ogni volta che viene rilevato un cambiamento."
    echo "  -t SEC    Intervallo in secondi tra le verifiche (default: 60)."
    exit 1
}

# Impostazioni predefinite
beep=false
interval=60

# Parsing delle opzioni
while getopts ":bt:" opt; do
    case ${opt} in
        b )
            beep=true
            ;;
        t )
            interval=$OPTARG
            ;;
        \? )
            usage
            ;;
        : )
            echo "Errore: L'opzione -$OPTARG richiede un argomento."
            usage
            ;;
    esac
done
shift $((OPTIND -1))

# Verifica della validità dell'intervallo
if ! [[ "$interval" =~ ^[0-9]+$ ]] || [ "$interval" -le 0 ]; then
    echo "Errore: L'intervallo deve essere un numero intero positivo."
    usage
fi

# Funzione per ottenere la cache ARP
get_arp_cache() {
    ip neighbor
}

# Memorizza la cache ARP iniziale
previous_cache=$(get_arp_cache)

while true; do
    # Attende l'intervallo specificato
    sleep "$interval"

    # Ottiene la cache ARP corrente
    current_cache=$(get_arp_cache)

    # Confronta la cache ARP corrente con quella precedente
    if [ "$previous_cache" != "$current_cache" ]; then
        echo "Cambiamento nella cache ARP rilevato:"
        echo "$current_cache"

        # Riproduce un suono se l'opzione -b è abilitata
        if $beep; then
            while true; do
                # Emette un suono
                echo -e "\a"
                # Attende la pressione di un tasto per fermare il suono
                read -t 1 -n 1 key
                if [ $? -eq 0 ]; then
                    break
                fi
            done
        fi

        # Aggiorna la cache precedente
        previous_cache="$current_cache"
    fi
done



