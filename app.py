from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/menu')
def menu():

    comidas = ['Pizza', 'Hamburguer', 'Batata']

    return render_template('menu.html', comidas=comidas)

@app.route('/contato')
def contato():
    return render_template('contato.html')

app.run(debug=True)