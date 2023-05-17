from flask import render_template, request, redirect, url_for, flash, send_from_directory, send_file
from app import app
import json
import datetime
from os import getenv

@app.route('/')
def index():
    return "Trello Clone"