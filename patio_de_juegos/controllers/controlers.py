from patio_de_juegos import app
from flask import render_template


@app.route('/play')
def play():
    return render_template("play.html")


@app.route('/play/<int:numero>')
def play_num(numero):
    return render_template("play_num.html", numero=numero)


@app.route('/play/<int:numero>/<color>')
def repetir(numero,color):
    return render_template("play_num_color.html", numero=numero,color=color)