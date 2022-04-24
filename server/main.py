import bottle
import quizfragen
import json



@bottle.route("/")
def index():
    with open("static/index.html") as file:
        return bottle.template(file.read(),kategorien=json.dumps(quizfragen.allekategorien()))

@bottle.route("/init")
@bottle.route("/init/")
def init():
    
    if "kategorie" in bottle.request.query:
        kategorie=bottle.request.query.kategorie
    else:
        kategorie=""
    with open("static/init.html") as file:
        return bottle.template(file.read(),datensatz=json.dumps(quizfragen.fragenvon(kategorie)))


@bottle.route("/frage")
@bottle.route("/frage/")
def frage():
    with open("static/frage.html") as file:
        return file.read()

@bottle.route("/main.css")
@bottle.route("/main.css/")
def frage():
    with open("static/main.css.html") as file:
        return file.read()


@bottle.route("/ergebnis")
@bottle.route("/ergebnis/")
def ergebnis():
    with open("static/ergebnis.html") as file:
        return file.read()


@bottle.route("/ergebnis/<n>")
@bottle.route("/ergebnis/<n>/")
def ergebnis(n="n"):
    with open("static/ergebnis-detail.html") as file:
        return bottle.template(file.read(),n=n)

bottle.run(host="localhost", port=8080, debug=True)