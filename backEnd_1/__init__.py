import os.path

from flask import Flask, Response, render_template

app = Flask(__name__)

from backEnd_1 import views


@app.route('/')
def hello():  # pragma: no cover
    return render_template('index.html')