import mysql.connector

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
