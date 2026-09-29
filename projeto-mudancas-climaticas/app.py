from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/mudancas-climaticas")
def mudancas_climaticas():
    return render_template("mudancas_climaticas.html")


@app.route("/combate")
def combate():
    return render_template("combate.html")


@app.route("/habitos")
def habitos():
    return render_template("habitos.html")


if __name__ == "__main__":
    app.run(debug=True)