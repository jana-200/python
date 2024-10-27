employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}

somme = 0
for i in employes.values():
    somme += i

print(somme)

# ou : somme = sum(employes.values()) 