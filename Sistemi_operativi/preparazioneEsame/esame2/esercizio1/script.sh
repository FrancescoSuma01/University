#!/bin/bash

echo "Attualmente nel sistema sono attivi $(who | cut -d " " -f 1 | sort | uniq | wc -l) \$ utenti"
