# Este es el respaldo del proyecto VIIIGames

from flask import render_template
from app_flask import app

@app.route("/")
def index():
    return render_template("test_login.html")

@app.route("/crear/cuenta")
def cuenta():
    return render_template("test_creacion.html")

if __name__ == "__main__":
    app.run(debug = True)