from flask import render_template, request, redirect, url_for, flash, send_from_directory, send_file
from app import app
import json
import datetime
from os import getenv
from tinydb import TinyDB, Query


boardDB = TinyDB('./db/board.json')
listasDB = TinyDB('./db/listas.json')
cartoes = TinyDB('./db/cartoes.json')
q = Query()

@app.route('/')
def index():
    listaBoard = boardDB.all()
    return render_template('index.html', listaBoard=listaBoard)

@app.route('/newboard')
def newboard():
    cod = "003"
    board = "Valle"
    myDoc = {
        "cod": cod,
        "board": board
    }
    boardDB.insert(myDoc)
    return "Ok"

@app.route('/b/<board>')
def b(board):
    boards = boardDB.all()
    listas = listasDB.all()
    boardAtual = boardDB.search(q.cod == board)
    return render_template('board.html', board=board, boardAtual=boardAtual, listas=listas, boards=boards)

@app.route('/newlist')
def newlist():
    board = "001"
    codLista = "l003"
    nomeLista = "done"
    posicao = 3
    myDoc = {
        "codLista": codLista,
        "board": board,
        "posicao": posicao,
        "nomeLista": nomeLista
    }
    listasDB.insert(myDoc)
    return "Ok"

