mot_secret = "chaaton"
nbr_lettres = len(mot_secret)
aAfficher = ["_"] * nbr_lettres
print(" ".join(aAfficher))

tryNbr = 0
lettres_trouvees = set()
lettres_correctes = set()

while tryNbr < 6 and len(lettres_correctes) < len(set(mot_secret)):  # Unique letters in mot_secret
    while True:
        lettre = input("Proposez une lettre : ").lower()
        if len(lettre) == 1 and lettre.isalpha():
            break
        else:
            print("Vous devez entrer UNE lettre valide.")

    if lettre in lettres_trouvees:
        print("Attention, vous avez déjà proposé cette lettre.")
        continue  # Skip the rest of the loop and prompt for a new letter
    lettres_trouvees.add(lettre)

    count = 0
    for i in range(nbr_lettres):
        if mot_secret[i] == lettre and aAfficher[i] == "_":
            lettres_correctes.add(lettre)
            aAfficher[i] = lettre
            count += 1

    if count == 0:
        tryNbr += 1
        print(f"FAUX, il vous reste encore {6 - tryNbr} essais.")
    else:
        print(f"Vous avez trouvé {count} lettre(s).")

    print(" ".join(aAfficher))

# Final messages after game ends
if tryNbr >= 6:
    print(f"Le mot secret était '{mot_secret}'\n. Vous avez utilisé tous vos essais... vous avez perdu.\n")
else:
    print("BRAVO, vous avez trouvé le mot !!")
