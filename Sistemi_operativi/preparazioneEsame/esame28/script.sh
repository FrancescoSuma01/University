# Salva la lista dei comandi in un file di log
LOGFILE=~/$(date +"%Y%m%d%H%M")-SessioneLavoro.txt
history > "$LOGFILE"
