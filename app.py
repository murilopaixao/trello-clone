from flask import Flask

app = Flask(__name__)
app.secret_key = 'my secret'

from views import *