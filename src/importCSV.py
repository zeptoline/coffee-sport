import csv
import os
import mysql.connector
from installation import Installation
from activite import Activite
from equipement import Equipement
from write_db import create_table
from write_db import add_to_table

# list qui associe les nom de fichier au nom de classes et de tables
type_objet={
    'installations.csv' : "Installation",
    'activites.csv' : "Activite",
    'equipements.csv' : "Equipement"
    }

# connection à la base de donnée
def connection():
    db = mysql.connector.connect(   host="infoweb",     # your host, usually localhost
                                    user="E145617E",    # your username
                                    passwd="E145617E",  # your password
                                    db="E145617E")      # name of the data base
    # creation des tables
    create_table(db)
    return db

def deconnection(db):
    db.close()

# fonction qui permet l'importation d'un fichier csv dans la base de donnée
def importCSV(nomFichier):
    db = connection()

    fname = os.path.dirname(os.path.abspath(__file__))+"/../data/"+nomFichier
    tname = type_objet[nomFichier]+"_db";
    db.cursor().execute("TRUNCATE TABLE "+tname) #On vide la table
    with open(fname, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            add_to_table(db, tname, row)
    deconnection(db)

# importCSV('activites.csv')
# importCSV('installations.csv')
# importCSV('equipements.csv')
