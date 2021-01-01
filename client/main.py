import json
import os
import time
import fileOpt

from flask import Flask, render_template,send_from_directory




app = Flask(__name__)
@app.route("/")
def Index():#首页
    return render_template("index.html")

@app.route("/files")
def Files():
    list = fileOpt.allFiles(os.getcwd())
    files = list["files"]
    dirs = list["dirs"]
    return render_template("files.html",files = files,dirs=dirs)

@app.route("/mods")
def Mods():
    return render_template("index.html")

@app.route("/downloads")
def Downloads():
    return render_template("index.html")

@app.route("/settings")
def Settings():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)

