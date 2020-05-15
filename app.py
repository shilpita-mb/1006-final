# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/bonappetit")
def crossword():
    return render_template('bonappetit.html')

@app.route("/libraryalign")
def library():
    return render_template('libraries.html')

#start the server
if __name__ == "__main__":
    app.run()