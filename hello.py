import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
  return "Привіт"

@app.route("/Слава Україні")
def answer():
  return "Героям Слава!!!"

if __name__ == "__main__"
app.run() 
