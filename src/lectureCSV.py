import csv
import os
import mysql.connector
from installation import Installation
from activite import Activite
from equipement import Equipement

db = mysql.connector.connect(   host="infoweb",     # your host, usually localhost
                                user="E145617E",    # your username
                                passwd="E145617E",  # your password
                                db="E145617E")      # name of the data base

cursor = db.cursor()

type_objet={
    'installations.csv' : Installation,
    'activites.csv' : Activite,
    'equipements.csv' : Equipement
    }

list = []

def lireCSV(nomFichier):
    fname = os.path.dirname(os.path.abspath(__file__))+"/../data/"+nomFichier
    with open(fname, 'r') as file:
        reader = csv.reader(file)
        for row in reader:

            list.append(type_objet[nomFichier](row[0],row[1],row[2],row[3],row[4],row[5]))


def afficherList():
    for elt in list:
        elt.afficher()

lireCSV('activites.csv')
db.close()
