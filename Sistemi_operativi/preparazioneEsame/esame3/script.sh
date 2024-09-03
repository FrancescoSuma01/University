#!/bin/bash

# Commento: [Cognome, Nome, Numero di matricola]

# Verifica del numero di parametri
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <PID> <intervallo_campionamento_in_secondi>"
    exit 1
fi

# Parametri
PID=$1
INTERVAL=$2
OUTPUT_FILE="cpu_usage.dat"
PLOT_FILE="cpu_usage.png"

# Inizializza il file di output
echo "# Tempo (s)  CPU (%)" > "$OUTPUT_FILE"

# Acquisizione dati CPU
SECONDS=0
while kill -0 $PID 2>/dev/null; do
    # Ottiene l'uso della CPU del processo specifico
    CPU=$(ps -p $PID -o %cpu --no-headers)
    
    # Aggiungi i dati al file
    echo "$SECONDS $CPU" >> "$OUTPUT_FILE"
    
    # Incrementa il tempo e attende l'intervallo specificato
    sleep $INTERVAL
    SECONDS=$((SECONDS + INTERVAL))
done

# Generazione del grafico con gnuplot
gnuplot -persist <<-EOFMarker
    set title "CPU Usage over Time for PID $PID"
    set xlabel "Time (s)"
    set ylabel "CPU Usage (%)"
    set grid
    set term png
    set output "$PLOT_FILE"
    plot "$OUTPUT_FILE" using 1:2 with lines title "CPU (%)"
EOFMarker

echo "Grafico salvato in $PLOT_FILE"
