#pip install flask
import os
from flask import Flask

app = Flask(__name__) #instanciation de la classe flask

@app.route("/") #définir l'endpoint "/" 
def hello():
    return "Hello ANAS !"

# Ensuite, définissez la variable d'environnement FLASK_APP 
# en donnant le nom de votre fichier python :

## export FLASK_APP=first_app.py 
 
# Lancez la commande suivante :

## flask run --host=0.0.0.0

# Sur un navigateur web allez à l'adresse adresse_ip_vm:5000 
# (localhost:5000 si vous utilisez votre machine personnelle), 
# vous devrez apercevoir un Hello World !

#  Vous n'avez pas à définir la variable d'environnement FLASK_APP 
# si vous appelez votre fichier python app.py ou wsgy.py,
#  vous pouvez lancer directement flask run
#  Le port 5000 est utilisé par défaut sur Flask, 
# vous pouvez changer le port via le flag --port lorsque vous utilisez flask run

# Définissez la route "/daniel" qui affiche "Hello Daniel !"

@app.route("/daniel")
def daniel():
    return "Hello Daniel !"

@app.route("/html")
def hello_html():
    return "<h1>Hello World !</h1>"

@app.route("/json")
def hello_json():
    return {"sequence": "Hello World"}


@app.route("/hello_get/<name>")
def hello_get(name):
  return "Hello {}".format(name)
# Do not consider this line </name>    
from flask import request
@app.route("/hello_post", methods=["POST"])
def hello_post():
  data = request.get_json()
  return "Hello {} \n".format(data["name"])

# Envoyez le dictionnaire {"name":"Daniel"} 
# au endpoint /hello_post par curl et POST

#réponse 
#curl localhost:5000/hello_post -d '{"name":"Daniel"}' -H 'Content-Type: application/json' -X POST 
@app.route("/hello",methods=["GET","POST"])
def post_get():
    if request.method == "POST":
        data=request.get_json()
        return "hello {} /n".format(data["name"])
    return "hello world!"

@app.route("/age/<int:year>")
def hello_man(year):
    return "Hello {} years old /n".format(year)

"""Chaines de requetes"""
from flask import Flask
from pydantic import BaseModel
from flask_pydantic import validate

class Query(BaseModel):
    name:str
    age:int

app = Flask(__name__)

@app.route("/intro")
@validate()
def intro(query:Query):
    return "Hello, my name is {} and I am {} years old".format(query.name,query.age)

#localhost:5000/intro?name=Daniel&age=33

# Créez une route affichant, sous le format JSON, 
# que Damian Lillard est un meneur de jeu de Portland, 
# né en 1990 à l'aide d'une chaîne de requête

from flask import Flask
from pydantic import BaseModel
from flask_pydantic import validate

class Player(BaseModel):
    name:str
    position:str
    team:str
    birth_year:int

app = Flask(__name__)

@app.route("/info")
@validate()
def info(query:Player):
    return query.dict()

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)