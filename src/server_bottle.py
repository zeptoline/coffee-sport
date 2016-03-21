import bottle
from bottle import route, run, template, static_file, post, get, response
from importCSV import importCSV
from read_db import read_from_db
from read_db import read_from_db_json
import json
#### pour recup l'ip ####
import socket
ip = socket.gethostbyname(socket.gethostname())
print("ip : ",ip)
#########################

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

@app.route('/view/activites', method=['OPTIONS', 'GET'])
def view_from_db():
    response.headers['Content-type'] = 'application/json'
    res = json.dumps(read_from_db_json("activites.csv"))
    return res

@app.route('/view/installations', method=['OPTIONS', 'GET'])
def view_from_db():
    response.headers['Content-type'] = 'application/json'
    res = json.dumps(read_from_db_json("installations.csv"))
    return res

@app.route('/view/equipements', method=['OPTIONS', 'GET'])
def view_from_db():
    response.headers['Content-type'] = 'application/json'
    res = json.dumps(read_from_db_json("equipements.csv"))
    return res

app.install(EnableCors())

app.run(host=ip, port=8080, debug=True)
