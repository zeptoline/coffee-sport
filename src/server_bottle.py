import bottle
from bottle import route, run, template, static_file, post, get, response, request
from importCSV import importCSV
from read_db import read_from_db
from read_db import read_from_db_json
from read_db import get_commune_json
import json


#### pour recup l'ip ####
import socket
ip = socket.gethostbyname(socket.gethostname())
print("ip : ",ip)
#########################

# autorisation cors
class EnableCors(object):
    name = 'enable_cors'
    api = 2

    def apply(self, fn, context):
        def _enable_cors(*args, **kwargs):
            # set CORS headers
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

            if bottle.request.method != 'OPTIONS':
                # actual request; reply with the actual response
                return fn(*args, **kwargs)
        return _enable_cors


app = bottle.app()


@app.route('/')
def acceuil():
    return
    '''
        <h1>Export vers la BDD</h1>
        </br>
        <a href="./import/activites">activites from csv</a>
        </br>
        <a href="./import/installations">installations from csv</a>
        </br>
        <a href="./import/equipements">equipements from csv</a>

        </br></br>

        <h1>Afficher donnée la BDD</h1>
        </br>
        <a href="./view/activites">activites</a>
        </br>
        <a href="./view/installations">installations</a>
        </br>
        <a href="./view/equipements">equipements</a>
    '''

# redirection pour l'importation des activités
@app.route('/import/activites', method=['OPTIONS', 'GET'])
def export_to_db():
    response.headers['Content-type'] = 'application/json'
    importCSV("activites.csv")
    return '''
        Exportation réussi
        </br>
        Redirection dans 3 secondes sinon appuyer sur Accueil
        </br>
        <a href="./../">Acceuil</a>
        <script>
            function go_to_accueil(){
                document.location.href = "./../";
            }
            window.setTimeout(go_to_accueil, 3000);
        </script>
    '''
# redirection pour l'importation des installaitons
@app.route('/import/installations', method=['OPTIONS', 'GET'])
def export_to_db():
    response.headers['Content-type'] = 'application/json'
    importCSV("installations.csv")
    return '''
        Exportation réussi
        </br>
        Redirection dans 3 secondes sinon appuyer sur Accueil
        </br>
        <a href="./../">Acceuil</a>
        <script>
            function go_to_accueil(){
                document.location.href = "./../";
            }
            window.setTimeout(go_to_accueil, 3000);
        </script>
    '''
# redirection pour l'importation des equipements
@app.route('/import/equipements', method=['OPTIONS', 'GET'])
def export_to_db():
    response.headers['Content-type'] = 'application/json'
    importCSV("equipements.csv")
    return '''
        Exportation réussi
        </br>
        Redirection dans 3 secondes sinon appuyer sur Accueil
        </br>
        <a href="./../">Acceuil</a>
        <script>
            function go_to_accueil(){
                document.location.href = "./../";
            }
            window.setTimeout(go_to_accueil, 3000);
        </script>
    '''

# redirection pour récupérer la table Activité en fonction des critères "nom_commune" et "activite_libelle"
# autre ici ne sert pas
@app.route('/view/activites/<nom_commune>/<activite_libelle>/<autre>', method=['OPTIONS', 'GET'])
def view_from_db(nom_commune, activite_libelle, autre):
    response.headers['Content-type'] = 'application/json'
    res = json.dumps(read_from_db_json("activites.csv", nom_commune, activite_libelle, autre))
    return res

# redirection pour récupérer la table Installation en fonction des critères "nom_commune" et "nom_usuel_install"
# autre ici ne sert pas
@app.route('/view/installations/<nom_commune>/<nom_usuel_install>/<autre>', method=['OPTIONS', 'GET'])
def view_from_db(nom_commune, nom_usuel_install, autre):
    response.headers['Content-type'] = 'application/json'
    res = json.dumps(read_from_db_json("installations.csv", nom_commune, nom_usuel_install, autre))
    return res

# redirection pour récupérer la table Installation en fonction des critères "nom_commune" et "nom_usuel_install" et "nom_equipmt"
@app.route('/view/equipements/<nom_commune>/<nom_usuel_install>/<nom_equipmt>', method=['OPTIONS', 'GET'])
def view_from_db(nom_commune, nom_usuel_install, nom_equipmt):
    response.headers['Content-type'] = 'application/json'
    res = json.dumps(read_from_db_json("equipements.csv", nom_commune, nom_usuel_install, nom_equipmt))
    return res


# redirection pour écupérer les communes pour l'autocomplétion
@app.route('/view/commune', method=['OPTIONS', 'GET'])
def view_from_db():
    response.headers['Content-type'] = 'application/json'
    commune = request.GET.get('commune', '').strip()
    table = request.GET.get('table', '').strip()
    res = json.dumps(get_commune_json(table, commune))
    return res

# autorisation cors
app.install(EnableCors())

# on lance le serveur sur l'ip local et sur le port 8080
app.run(host=ip, port=8080, debug=True)
