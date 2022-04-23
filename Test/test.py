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
<p id = "x"> Hallo</p>
   <script> const Http = new XMLHttpRequest();
   const url= "127.0.0.1:8080/init";
Http.open("GET", url);
Http.send()
Http.onreadystatechange=function(){
    if(this.readyState==4 && this.status==200){
 document.querySelector('#x').element.innerHTML = Http.responseText;
    }
}
</script>
</body>
</html>"""

@bottle.route("/init")
@bottle.route("/init/")
def init():
    return "Hier ist die /init Seite"
bottle.run(host="localhost", port=8080, debug=True)