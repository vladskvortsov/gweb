import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    text = 'yyyyyyyyyyyy'
    return render_template('index.html', txt=text)


@app.route("/Слава_Україні")
def answer():
    return "Героям Слава!!!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
