import bottle





@bottle.route("/")
def index():
    return "Hallo ich bin cool"

@bottle.route("/init")
@bottle.route("/init/")
def init():
    return "Hier ist die /init Seite"

@bottle.route("/frage")
@bottle.route("/frage/")
def frage():
    return "Hier ist die /frage Seite"

@bottle.route("/ergebnis")
@bottle.route("/ergebnis/")
def ergebnis():
    return "Hier ist die /ergebnis Seite"

@bottle.route("/ergebnis/<n>")
@bottle.route("/ergebnis/<n>/")
def ergebnis(n="n"):
    return bottle.template("Hier ist die{{n}} /ergebnis Seite",n=n)

bottle.run(host="localhost", port=8080, debug=True)