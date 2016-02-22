import csv

class Installation:
    nom_usuel_install = ""
    num_install = 0
    nom_commune = ""
    code_insee = 0
    code_postal = 0
    location = ""

    def __init__(self, v1, v2, v3, v4, v5, v6):
        self.nom_usuel_install = v1
        self.num_install = v2
        self.nom_commune = v3
        self.code_insee = v4
        self.code_postal = v5
        self.location = v6

    def afficher(self):
        print("Nom : ",self.nom_usuel_install," numero : ",self.num_install)


## EXECUTION ##
list = []
def lireCSV():
    with open('/hometu/etudiants/h/e/E146187Z/Cours/semestre4/Prod. logiciel/installations-sportives-pdl-master/data/installations.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            list.append(Installation(row[0],row[1],row[2],row[3],row[4],row[5]))

def afficherList():
    for elt in list:
        elt.afficher()

# lireCSV()
# afficherList()
