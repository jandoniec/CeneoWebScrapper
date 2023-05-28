from app import app
from flask import Flask, render_template

@app.route('/')
@app.route('/index')
def index():
    return "Hello, Jan Doniec"

@app.route('/name/',defaults={'name':'Anonim'})
@app.route('/name/<name>')
def name(name):
    return f"Hello, {name}!"

@app.route("/")
def index():
    return render_template('mainpage.html')

@app.route("/aboutauthor")
def author():
    return render_template('author.html')

@app.route("/ekstrakcja")
def extraction():
    return render_template('extraction.html')

@app.route("/productlist")
def productList():
    return render_template('productlist.html')