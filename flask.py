from flask import Flask, send_file

app = Flask(__name__)

@app.route('/arearestrita/<int:id>')
def area_restrita(id):
    if id == 1:
        return send_file('cadeado_fechado.png', mimetype='image/png')
    elif id == 2:
        return send_file('cadeado_aberto.png', mimetype='image/png')
    else:
        return "ID inválido"

if __name__ == '__main__':
    app.run(debug=True)