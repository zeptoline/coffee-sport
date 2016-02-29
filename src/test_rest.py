from bottle import route, run, template
from importCSV import importCSV
from read_db import read_from_db


@route('/')
def acceuil():
    return '''
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

@route('/import/activites')
def export_to_db():
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

@route('/import/installations')
def export_to_db():
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

@route('/import/equipements')
def export_to_db():
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

@route('/view/activites')
def view_from_db():
    res = read_from_db("activites.csv")
    return '''
        <h1> Resultat de Activite </h1>
        </br>
    '''+res+'''
        </br>
        <a href="./../">Acceuil</a>
    '''

@route('/view/installations')
def view_from_db():
    res = read_from_db("installations.csv")
    return '''
        <h1> Resultat de Installation </h1>
        </br>
    '''+res+'''
        </br>
        <a href="./../">Acceuil</a>
    '''

@route('/view/equipements')
def view_from_db():
    res = read_from_db("equipements.csv")
    return '''
        <h1> Resultat de Equipement </h1>
        </br>
    '''+res+'''
        </br>
        <a href="./../">Acceuil</a>
    '''

run(host='localhost', port=8080, debug=True)
