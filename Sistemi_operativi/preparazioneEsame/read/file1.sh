#!/bin/bash

echo "+ + + Digita il tuo nome + + +"
read nome

echo ""
echo "Ti chiami" $nome

echo ""
echo "- - - - - - - - - - - - - - - - - - - - - - - - -"

echo ""
echo "+ + + Digita il tuo cognome + + +"
read -n4 cognome

echo ""
echo "Il tuo cognome e" $cognome

echo ""
echo "- - - - - - - - - - - - - - - - - - - - - - - - -"

echo ""
echo "+ + + Digita la tua eta + + +"
read -t5 eta

echo ""
echo "Hai" $eta "anni"

echo ""
echo "- - - - - - - - - - - - - - - - - - - - - - - - -"

echo ""
echo "+ + + Digita una parola segreta + + +"
read -s secret

echo ""
echo "La tua parola segrate e: " $secret

echo ""
echo ""
echo "bye"
