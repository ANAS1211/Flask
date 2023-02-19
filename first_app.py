#pip install flask

from flask import Flask

app = Flask(__name__) #instanciation de la classe flask

@app.route("/") #définir l'endpoint "/" 
def hello():
    return "Hello World !"

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