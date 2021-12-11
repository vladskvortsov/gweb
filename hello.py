import os
from flask import Flask
app = Flask(__name__)

color = os.environ.get('APP_COLOR')

@app.route("/")
def main():
print (color)
  return "Привіт"

@app.route("/Слава Україні")
def answer():
  return "Героям Слава!!!"


