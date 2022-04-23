import bottle





@bottle.route("/")
def index():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kennst du den Sport?</title>
   
</head>
<body>
<p id = "x">weitergekommen!</p>

</body>
</html>"""

@bottle.route("/init")
@bottle.route("/init/")
def init():
    return bottle.template("""
    <html>

    <body>

    <script>

    var daten = {{ datenstring }};
window.location.replace("/");
    </script>


    </body>

    </html>
    """, datenstring = "daten")

bottle.run(host="localhost", port=8080, debug=True)