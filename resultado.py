from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('index.html')

@app.route('/inscrever', methods=['POST'])
def inscrever():

    nickname = request.form['nickname']
    jogo = request.form['jogo']
    email = request.form['email']

    if nickname == '' or jogo == '' or email == '':
        mensagem = 'Preencha todos os campos obrigatórios.'

    elif len(nickname) < 4:
        mensagem = 'Preencha todos os campos obrigatórios.'

    else:
        mensagem = 'Inscrição realizada com sucesso!'

    return render_template('resultado.html', mensagem=mensagem)

app.run(debug=True)