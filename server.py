from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def hello(name):
    print(name)
    return "Hi " + name

@app.route('/repeat/<int:number>/<string:name>')
def reapeating(number, name):
    responds = ''
    for i in range(0,number):
        responds +=  f"<h1>{name}</h1>"
    return responds

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)