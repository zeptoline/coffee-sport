import csv

class Activite:
    code_insee = 0
    nom_commune = ""
    num_fich_equipmt = 0
    nb_equipmt_ident = 0
    activite_code = 0
    activite_libelle = ""

    def __init__(self, v1, v2, v3, v4, v5, v6):
        self.code_insee = v1
        self.nom_commune = v2
        self.num_fich_equipmt = v3
        self.nb_equipmt_ident = v4
        self.activite_code = v5
        self.activite_libelle = v6

    def afficher(self):
        print("Nom commune : ",self.nom_commune," code insee : ",self.code_insee)

## EXECUTION ##
list = []
def lireCSV():
    with open('/hometu/etudiants/h/e/E146187Z/Cours/semestre4/Prod. logiciel/installations-sportives-pdl-master/data/activites.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            list.append(Activite(row[0],row[1],row[2],row[3],row[4],row[5]))

def afficherList():
    for elt in list:
        elt.afficher()

# lireCSV()
# afficherList()
