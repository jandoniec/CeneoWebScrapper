from app import app
from flask import render_template


'''

@app.route('/name/',defaults={'name':'Anonim'})
@app.route('/name/<name>')
def name(name):
    return f"Hello, {name}!"
'''
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/author")
def author():
    return render_template('author.html')

@app.route("/ekstrakcja")
def extraction():
    return render_template('extraction.html')

@app.route("/productlist")
def productList():
    return render_template('productlist.html')

@app.route("/product")
def product():
    return render_template('product.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=8081)