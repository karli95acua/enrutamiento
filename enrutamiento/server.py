from flask import Flask

app = Flask(__name__)

#haz que diga "¡Hola Mundo!"
@app.route( "/", methods = ['GET'] )
def mensaje_holamundo():
    return "¡Hola Mundo!"


#haz que diga "¡Dojo!"
@app.route( "/dojo", methods = ['GET'] )
def mensaje_dojo():
    return "¡Dojo!"


#haz que diga "¡Hola, Flask!
@app.route( "/say/flask", methods = ['GET'] )
def say_flask():
    flask = "¡Hola, Flask!"
    return f"{flask}"


#haz que diga "¡Hola, Michael!"
@app.route( "/say/Michael", methods = ['GET'] )
def say_michael():
    michael = "¡Hola, Michael!"
    return f"{michael}"


#haz que diga "¡Hola, John!"
@app.route( "/say/john", methods = ['GET'] )
def say_john():
    john = "¡Hola, John!"
    return f"{john}"

#haz que diga "hola" 35 veces
#haz que diga "adiós" 80 veces
#haz que diga "perros" 99 veces
@app.route( "/repeat/<int:num1>/<string:var1>" , methods = ['GET'])
def repeat_var1( num1, var1 ):
    resultado = "  ".join([var1] * num1)
    return f"{resultado}"

#BONUS SENSEI: pruebalo por ejemplo con: http://127.0.0.1:5002/cachorro
@app.route('/<path:unmatched_path>', methods = ['GET'])
def handle_unmatched_path(unmatched_path):
    return f"¡Lo siento {unmatched_path}! No hay respuesta. Inténtalo otra vez."


if __name__ == "__main__": #esto permite que solo se ejecute cuando estoy dentro de este proyecto
    app.run( debug = True , port = 5002 )