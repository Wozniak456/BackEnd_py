from flask import Flask
app = Flask(__name__)

from backEnd_1 import views

@app.route('/')
def hello_world():
    return 'Hello, World!'