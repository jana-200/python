def convertir(unit1: str, unit2: str, facteur: float):
    valeur_str = input(f"Conversion {unit1} -> {unit2}. Donnez la valeur à convertir (ou 'q' pour quitter) : ")
    if valeur_str.lower() == 'q':
        return False
    try:
        valeur_float = float(valeur_str)
    except ValueError:
        print("Vous avez entré une valeur non numérique")
        print("(utilisez des points au lieu des virgules)")
        return convertir(unit1, unit2, facteur)
    valeur_convertie = round(valeur_float * facteur, 2)
    print(f"Resultat de la conversion : {valeur_float} {unit2} = {valeur_convertie} {unit2}")
    return True


while True:
    print("Ce programme vous permet de convertir des unités  : ")
    print("1 - Pouces vers cm")
    print("2 - cm vers pouces")
    choix = input("Votre choix (1 ou 2): ")
    if choix == "1" or choix == "2":
        break
    print("ERROR: vous devez choisir 1 ou 2")

while True:
    if choix == "1":
        if not convertir("pouces", "cm", 2.54):
            break
    elif choix == "2":
        if not convertir("cm", "pouces", 1/2.54):
            break


print("bye bye !")
