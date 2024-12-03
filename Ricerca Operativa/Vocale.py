lettera = input("Inserisci una lettera: ")

lettera = lettera.lower()

if (lettera == 'a' or lettera == 'e' or lettera == 'i' or lettera == 'o' or lettera == 'u'):
    print(f"La lettera inserita è {lettera} ed è una vocale")
else:
    print(f"La lettera inserita è {lettera} e non è una vocale")