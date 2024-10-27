liste = [20, 10, 51, 25]
print("original :", liste)

liste.append(10)
# ajoute 10 à la fin

print("append 10 :", liste)

liste.extend([11, 12, 13])
# ajoute +ieurs elements à la fin

print("extends 11,12,13 :", liste)

liste.pop()
# efface le dernier element

print("pop sans parametre: ", liste)

liste.pop(0)
# efface l'élément à l'indice passé en parametre

print("pop avec parametre: ", liste)







