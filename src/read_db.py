import csv
import os
import mysql.connector
from installation import Installation
from activite import Activite
from equipement import Equipement
from write_db import select_from_table

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
    return db

def deconnection(db):
    db.close()

# fonction qui permet l'importation d'un fichier csv dans la base de donnée
def read_from_db(nomFichier):
    db = connection()
    tname = type_objet[nomFichier]+"_db";

    # select sur la base de données
    result = select_from_table(db, tname)

    res = '<table border=1px style="border-collapse: collapse;">'

    # nom des colonnes de la tables
    res += '''
        <tr>
            <td style="font-weight: bold;text-align: center;padding: 5px;">'''+str(result[0][0]).replace("_", " ")+'''</td>
            <td style="font-weight: bold;text-align: center;padding: 5px;">'''+str(result[0][1]).replace("_", " ")+'''</td>
            <td style="font-weight: bold;text-align: center;padding: 5px;">'''+str(result[0][2]).replace("_", " ")+'''</td>
            <td style="font-weight: bold;text-align: center;padding: 5px;">'''+str(result[0][3]).replace("_", " ")+'''</td>
            <td style="font-weight: bold;text-align: center;padding: 5px;">'''+str(result[0][4]).replace("_", " ")+'''</td>
            <td style="font-weight: bold;text-align: center;padding: 5px;">'''+str(result[0][5]).replace("_", " ")+'''</td>
        </tr>
    '''

    # données de la table
    for row in result[1]:
        res += '''
            <tr>
                <td>'''+str(row[0])+'''</td>
                <td>'''+str(row[1])+'''</td>
                <td>'''+str(row[2])+'''</td>
                <td>'''+str(row[3])+'''</td>
                <td>'''+str(row[4])+'''</td>
                <td>'''+str(row[5])+'''</td>
            </tr>
        '''
    res += '</table>'
    deconnection(db)
    return res

def read_from_db_json(nomFichier):
    db = connection()
    tname = type_objet[nomFichier]+"_db";

    # select sur la base de données
    result = select_from_table(db, tname)
    # nom des colonnes de la tables
    res = {}

    id1 = str(result[0][0]).replace("_", " ")
    id2 = str(result[0][1]).replace("_", " ")
    id3 = str(result[0][2]).replace("_", " ")
    id4 = str(result[0][3]).replace("_", " ")
    id5 = str(result[0][4]).replace("_", " ")
    id6 = str(result[0][5]).replace("_", " ")

    # données de la table
    for row in result[1]:
        dict = {id1:row[0],
                id2:row[1],
                id3:row[2],
                id4:row[3],
                id5:row[4],
                id6:row[5]}
        res[len(res)] = dict
    deconnection(db)
    return res
