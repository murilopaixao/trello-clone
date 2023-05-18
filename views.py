from flask import render_template, redirect, url_for
from app import app
import json
import pymongo
from os import getenv

MONGO_SRC = getenv('MONGO_SRC')
MONGO_LOGIN = getenv('MONGO_LOGIN')
MONGO_PASSWORD = getenv('MONGO_PASSWORD')
MONGO_PORT = getenv('MONGO_PORT')

conn_str = (f"mongodb://{MONGO_LOGIN}:{MONGO_PASSWORD}@{MONGO_SRC}:{MONGO_PORT}")

try:
    client = pymongo.MongoClient(conn_str)
except Exception:
    print("Error:" + Exception)

myDB = client["trello"]
myCollectionBoards = myDB["boards"]
myCollectionListas = myDB["listas"]

@app.route('/')
def index():
    lista = myCollectionBoards.find({},{"_id": 0})
    return render_template('index.html', lista=lista)

@app.route('/newboard')
def newboard():
    cod = 2
    board = "Dia-a-dia"
    myDoc = {
        "cod": cod,
        "board": board
    }
    myCollectionBoards.insert_one(myDoc)
    return "Ok"

@app.route('/newlist')
def newlist():
    board = 1
    codLista = 2
    nomeLista = "do"
    posicao = 2
    myDoc = {
        "codLista": codLista,
        "board": board,
        "posicao": posicao,
        "nomeLista": nomeLista
    }
    myCollectionListas.insert_one(myDoc)
    return "Ok"

@app.route('/b/<board>')
def b(board):
    boards = myCollectionBoards.find({},{"_id": 0})
    listas = myCollectionListas.find({},{"_id": 0})
    boardAtual = myCollectionBoards.find({"cod": int(board)},{"_id": 0})
    return render_template('board.html', board=board, boardAtual=boardAtual, listas=listas, boards=boards)
