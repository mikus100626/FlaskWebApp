from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/galeria')
def getGalery():
    return render_template('galeria.html')
@app.route('/alexa')
def alexa():
    return render_template('alexa.html')
#debug true nie chcem na produkcji 

