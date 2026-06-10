 from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/')
def inicio():

    nome = request.cookies.get('nome')
    email = request.cookies.get('email')
    tema = request.cookies.get('tema')

    if tema == None:
        tema = 'claro'

    return render_template('inicio.html',
                           nome=nome,
                           email=email,
                           tema=tema)


@app.route('/salvar', methods=['POST'])
def salvar():

    nome = request.form['nome']
    email = request.form['email']

    resp = make_response(redirect('/'))

    resp.set_cookie('nome', nome)
    resp.set_cookie('email', email)

    return resp


@app.route('/claro')
def claro():

    resp = make_response(redirect('/'))
    resp.set_cookie('tema', 'claro')

    return resp


@app.route('/escuro')
def escuro():

    resp = make_response(redirect('/'))
    resp.set_cookie('tema', 'escuro')

    return resp


app.run(debug=True)