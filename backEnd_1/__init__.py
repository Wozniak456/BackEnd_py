import os.path

from flask import Flask, Response, render_template
from backEnd_1.db import db_init

app = Flask(__name__)
users, category, currency, record = db_init()
from backEnd_1 import views


@app.route('/')
def hello():  # pragma: no cover
    return render_template('index.html')