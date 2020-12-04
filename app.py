from flask import Flask, render_template

#Nom de l'application (obligatoire)
app = Flask(__name__)

#Données utilisées par l'application. Syntaxe permettant de rendre la variable 'data' accessible partout avec Jinja (sinon on a un 'data not defined')
stock_database = [
    {
        "diplome": "bac ES",
        "annee": "2014",
        "lieu": "Antony",
    },
    {
        "diplome": "licence histoire",
        "annee": "2017",
        "lieu": "Sorbonne Université",
    },
    {
        "diplome": "licence anglais",
        "annee": "2017",
        "lieu": "Sorbonne Université",
    },
    {
        "diplome": "master histoire",
        "annee": "2019",
        "lieu": "Sorbonne Université",
    },
    {
        "diplome": "master TNAH",
        "annee": "2021",
        "lieu": "ENC",
    },
    {
        "emploi": "stage archiviste",
        "annee": "2020",
        "lieu": "Groupe Crédit Agricole",
    },
    {
        "emploi": "employé de banque",
        "annee": "2019",
        "lieu": "BNP",
    },
{
        "emploi": "employé de restauration",
        "annee": "2016",
        "lieu": "Centre sportif de Bougival",
    },
]

#Instanciation des différents chemins URL disponibles dans l'app.

#Chemin vers la page d'accueil (démarrage et retour au menu)
@app.route("/")
def index():
    return render_template("index.html", data=stock_database)

#Chemin vers la page 'variable' qui change selon les boutons cliqués. Le chemin sera sous la forme variable/nombre (place_id).
#La valeur de place_id est définie selon le bouton cliqué.
@app.route("/variable/<int:place_id>")
def variable(place_id):
    return render_template("variable.html", place_id=place_id, data=stock_database)

if __name__ == "__main__":
#Permet d'utiliser le débugger Jinja
    app.run(debug=True)
