import csv

class Equipement:
    code_insee = 0
    nom_commune = ""
    num_install = 0
    nom_usuel_install = ""
    num_fich_equipmt = 0
    nom_equipmt = ""

    def __init__(self, v1, v2, v3, v4, v5, v6):
        self.code_insee = v1
        self.nom_commune = v2
        self.num_install = v3
        self.nom_usuel_install = v4
        self.num_fich_equipmt = v5
        self.nom_equipmt = v6

    def afficher(self):
        print("Nom : ",self.nom_equipmt," numero : ",self.num_fich_equipmt)


## EXECUTION ##
list = []
def lireCSV():
    with open('/hometu/etudiants/h/e/E146187Z/Cours/semestre4/Prod. logiciel/installations-sportives-pdl-master/data/equipements.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            list.append(Equipement(row[0],row[1],row[2],row[3],row[4],row[5]))

def afficherList():
    for elt in list:
        elt.afficher()

# lireCSV()
# afficherList()
