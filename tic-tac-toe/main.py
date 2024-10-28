import numpy as np
taille = 3
matrice = np.full((taille,taille),' * ')

def victoire(joueur):
    # Vérifier les lignes
    for i in range(taille):
        if all(matrice[i][j] == " "+joueur+" " for j in range(taille)):
            return True
    # Vérifier les colonnes
    for j in range(taille):
        if all(matrice[i][j] == " "+joueur+" "  for i in range(taille)):
            return True

    # Vérifier la diagonale principale
    if all(matrice[i][i] == " "+joueur+" "  for i in range(taille)):
        return True

    # Vérifier la diagonale secondaire
    if all(matrice[i][taille-i-1] == " "+joueur+" "  for i in range(taille)):
        return True

    return False

def match_nul():
    for i in range(taille):
        for j in range(taille):
            if matrice[i][j] == ' * ':
                return False
    return True


print("Bienvenu : ")

joueur = 'X'
while True:
    print("voici la grille actuelle : ")

    for i in range(taille):
        print(' '.join(matrice[i]))

    print(f"C'est le tour du joueur {joueur}")
    ligne = int(input(f"choisissez une ligne : "))
    colonne = int(input("et une colonne : "))

    if ligne <= 0 or ligne > taille or colonne <= 0 or colonne > taille:
        print("vous devez choisir un nombre valide entre 1 et 3 ! ")
        continue

    if matrice[ligne - 1][colonne - 1] != ' * ':
        print("Cette case est déjà occupée, choisissez une autre ! ")
        continue

    matrice[ligne-1][colonne-1] = " "+joueur+" "

    if victoire(joueur):
        for i in range(taille):
            print(' '.join(matrice[i]))
        print(f"Bravo ! le joueur {joueur} a gagné !")
        break
    if match_nul():
        for i in range(taille):
            print(' '.join(matrice[i]))
        print("Match nul")
        break

    if joueur == 'X':
        joueur = 'O'
    else:
        joueur = 'X'


