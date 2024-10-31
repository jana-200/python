import sqlite3

def initialiser_bd():
    co = sqlite3.connect('taches.db')
    cursor = co.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS taches(id INTEGER PRIMARY KEY,tache TEXT NOT NULL,etat BOOLEAN NOT NULL DEFAULT 0)')
    co.commit()
    co.close()

def ajouter_tache(tache):
    co = sqlite3.connect('taches.db')
    cursor = co.cursor()
    cursor.execute('INSERT INTO taches (tache) VALUES (?)', (tache,))
    co.commit()
    co.close()

def supprimer_tache(id):
    co = sqlite3.connect('taches.db')
    cursor = co.cursor()
    cursor.execute('DELETE FROM taches WHERE id = ?', (id,))
    co.commit()
    co.close()

def completer_tache(id):
    co = sqlite3.connect('taches.db')
    cursor = co.cursor()
    cursor.execute('UPDATE taches SET etat = 1 WHERE id = ?', (id,))
    co.commit()
    co.close()

def afficher_taches():
    co = sqlite3.connect('taches.db')
    cursor = co.cursor()
    cursor.execute('SELECT * FROM taches ORDER BY etat')
    taches = cursor.fetchall()
    cursor.close()

    for tache in taches:
        etat = "done" if tache[2] else "not yet"
        print(f"tache numéro {tache[0]}: {tache[1]} (etat : {etat})")


initialiser_bd()

while True:
    print("\nGestionnaire de tâches")
    print("1. Ajouter une tâche")
    print("2. Supprimer une tâche")
    print("3. Marquer une tâche comme terminée")
    print("4. Afficher les tâches")
    print("5. Quitter")

    choix = input("Choisissez une option: ")
    if choix == '1':
        tache = input("tâche à ajouter: ")
        ajouter_tache(tache)
    elif choix == '2':
        id = int(input("numéro de la tâche à supprimer: "))
        supprimer_tache(id)
    elif choix == '3':
        id = int(input("numéro de la tâche terminée: "))
        completer_tache(id)
    elif choix == '4':
        afficher_taches()
    elif choix == '5':
        break
    else:
        print("veuillez entrer un nombre entre 1 et 5")