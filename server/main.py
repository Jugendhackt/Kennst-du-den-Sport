import bottle





@bottle.route("/")
def index():
    with open("static/index.html") as file:
        return file.read()

@bottle.route("/init")
@bottle.route("/init/")
def init():
    
    if "kategorie" in bottle.request.query:
        kategorie=bottle.request.query.kategorie
    else:
        kategorie="allgemein"
    return "Hier ist die /init Seite"+kategorie


@bottle.route("/frage")
@bottle.route("/frage/")
def frage():
    with open("static/frage.html") as file:
        return file.read()


@bottle.route("/ergebnis")
@bottle.route("/ergebnis/")
def ergebnis():
    with open("static/ergebnis.html") as file:
        return file.read()


@bottle.route("/ergebnis/<n>")
@bottle.route("/ergebnis/<n>/")
def ergebnis(n="n"):
    return bottle.template("Hier ist die{{n}} /ergebnis Seite",n=n)

bottle.run(host="localhost", port=8080, debug=True)