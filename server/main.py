import bottle





@bottle.route("/")
def hello():
    return "Hallo ich bin cool"

bottle.run(host="localhost", port=8080, debug=True)