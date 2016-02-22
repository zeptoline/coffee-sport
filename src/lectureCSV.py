import csv
from installation import Installation
from activite import Activite
from equipement import Equipement

type_objet={
    '/hometu/etudiants/h/e/E146187Z/Cours/semestre4/Prod. logiciel/installations-sportives-pdl-master/data/installations.csv' : Installation,
    '/hometu/etudiants/h/e/E146187Z/Cours/semestre4/Prod. logiciel/installations-sportives-pdl-master/data/activites.csv' : Activite,
    '/hometu/etudiants/h/e/E146187Z/Cours/semestre4/Prod. logiciel/installations-sportives-pdl-master/data/equipements.csv' : Equipement
    }
nomFichier = '/hometu/etudiants/h/e/E146187Z/Cours/semestre4/Prod. logiciel/installations-sportives-pdl-master/data/activites.csv'
list = []

def lireCSV():
    with open(nomFichier, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            list.append(type_objet[nomFichier](row[0],row[1],row[2],row[3],row[4],row[5]))

def afficherList():
    for elt in list:
        elt.afficher()

lireCSV()
afficherList()
