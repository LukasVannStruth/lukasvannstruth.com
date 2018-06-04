from flask import Flask, render_template
APP = Flask(__name__)

@APP.route('/')
def hello_world():
    return render_template("home.html")