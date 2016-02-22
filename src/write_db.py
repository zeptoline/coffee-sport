import mysql.connector

db = mysql.connector.connect(host="infoweb",    # your host, usually localhost
                     user="E145617E",         # your username
                     passwd="E145617E",  # your password
                     db="E145617E")        # name of the data base



db.close()
