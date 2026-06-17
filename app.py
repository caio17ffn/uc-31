from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "123456"

usuario_correto = "admin"
senha_correta = "123"

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    erro = ""

    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == usuario_correto and senha == senha_correta:
            session["usuario"] = usuario
            return redirect("/dashboard")
        else:
            erro = "Usuario ou senha incorretos"

    return render_template("login.html", erro=erro)


@app.route("/dashboard")
def dashboard():

    if "usuario" not in session:
        return redirect("/login")

    return render_template("dashboard.html", usuario=session["usuario"])


@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect("/login")


app.run(debug=True)