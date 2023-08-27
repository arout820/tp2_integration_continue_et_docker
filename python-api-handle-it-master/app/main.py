from flask import Flask, jsonify, request

from machine.machine import Machine
from application.application import Application

app = Flask(__name__)
machine = Machine()

@app.route("/")
def hello_world():
    return "Bienvenue sur l'application de gestion"

@app.route('/machines', methods=["GET","POST"])
def liste_machine():
    if request.method == 'GET':
        return jsonify({"machines": machine.liste() })
    elif request.method == "POST":
        data = request.json
        return jsonify({"machine":machine.add(data)})
    else:
        return jsonify({"error": 'La méthode utilisée n\'est pas valide'})

@app.route('/machines/<name>', methods=["GET","PUT","DELETE"])
def get_machine(name):
    if request.method == 'GET':
        return jsonify({"machine":machine.get(name)})
    if request.method == 'PUT':
        data = request.form # a multidict containing POST data
        return jsonify({"machine":machine.edit(name,data)})
    if request.method == 'DELETE':
        return jsonify({"machine":machine.delete(name)})
    else:
        return jsonify({"error": 'La méthode utilisée n\'est pas valide'})
