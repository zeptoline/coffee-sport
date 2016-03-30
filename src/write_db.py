import mysql.connector

# fonction qui crée les tables si elles n'existent pas déjà
def create_table(db) :
    print("création des tables")
    db.cursor().execute(
                "CREATE TABLE IF NOT EXISTS `Activite_db` ("
                    "  `code_insee` int(11),"
                    "  `nom_commune` varchar(255),"
                    "  `num_fich_equipmt` int(11),"
                    "  `nb_equipmt_ident` int(11),"
                    "  `activite_code` int(11),"
                    "  `activite_libelle` varchar(255)"
                ")")

    db.cursor().execute(
                "CREATE TABLE IF NOT EXISTS `Equipement_db` ("
                    "  `code_insee` int(11),"
                    "  `nom_commune` varchar(255),"
                    "  `num_install` int(11),"
                    "  `nom_usuel_install` varchar(255),"
                    "  `num_fich_equipmt` int(11),"
                    "  `nom_equipmt` varchar(255)"
                ")")

    db.cursor().execute(
                "CREATE TABLE IF NOT EXISTS `Installation_db` ("
                    "  `nom_usuel_install` varchar(255),"
                    "  `num_install` int(11),"
                    "  `nom_commune` varchar(255),"
                    "  `code_insee` int(11),"
                    "  `code_postal` int(11),"
                    "  `location` varchar(255)"
                ")")
    print("tables crées")

# fonction qui ajoute une ligne à une table
def add_to_table(db, table, values) :
    add_activite = ("INSERT INTO Activite_db "
               "(code_insee, nom_commune, num_fich_equipmt, nb_equipmt_ident, activite_code, activite_libelle) "
               "VALUES (%s, %s, %s, %s, %s, %s)")

    add_equipement = ("INSERT INTO Equipement_db "
               "(code_insee, nom_commune, num_install, nom_usuel_install, num_fich_equipmt, nom_equipmt) "
               "VALUES (%s, %s, %s, %s, %s, %s)")

    add_installation = ("INSERT INTO Installation_db "
               "(nom_usuel_install, num_install, nom_commune, code_insee, code_postal, location) "
               "VALUES (%s, %s, %s, %s, %s, %s)")

    data = (values[0],values[1],values[2],values[3],values[4],values[5])

    if(table == "Activite_db"):
        db.cursor().execute(add_activite, data)
    elif(table == "Equipement_db"):
        db.cursor().execute(add_equipement, data)
    elif(table == "Installation_db"):
        db.cursor().execute(add_installation, data)
    db.commit()

def select_from_table(db, table, nom_commune=None, data2=None, data3=None) :
    cursor = db.cursor()

    condition = ""
    if((nom_commune != "null") or (data2 != "null") or (data3 != "null")):
        condition = "WHERE "

        if(nom_commune != "null"):
            condition += "nom_commune = '"+nom_commune+"' "

        if(table == "Activite_db"):
            if(data2 != "null"):
                condition += "and activite_libelle = '"+data2+"' "
        elif(table == "Equipement_db"):
            if(data2 != "null"):
                condition += "and nom_usuel_install = '"+data2+"' "
            if(data3 != "null"):
                condition += "and nom_equipmt = '"+data3+"' "
        elif(table == "Installation_db"):
            if(data2 != "null"):
                condition += "and nom_usuel_install = '"+data2+"' "



    select_activite = ("SELECT * FROM Activite_db "+condition)

    select_equipement = ("SELECT * FROM Equipement_db "+condition)

    select_installation = ("SELECT * FROM Installation_db "+condition)

    print(select_activite)
    if(table == "Activite_db"):
        cursor.execute(select_activite)
    elif(table == "Equipement_db"):
        cursor.execute(select_equipement)
    elif(table == "Installation_db"):
        cursor.execute(select_installation)

    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]

    print(field_names)

    rows = cursor.fetchall()

    result = [field_names]
    result.append(rows)
    return result


def select_commune_from_table(db, table, commune=None) :
    cursor = db.cursor()

    select = ("SELECT DISTINCT nom_commune FROM "+table)
    if(commune!=None):
        select+= " WHERE nom_commune LIKE '"+commune+"%'"


    cursor.execute(select)
    rows = cursor.fetchall()
    tab = []
    for row in rows :
        tab.append(row[0])

    return tab
