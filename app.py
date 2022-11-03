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
    app.run(debug=True, host='0.0.0.0')


#    port = int(os.environ.get('PORT', 5000))
#    app.run(debug=True, host='0.0.0.0', port=port)

