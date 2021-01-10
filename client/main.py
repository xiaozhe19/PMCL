import json
import os
import time
import fileOpt
import luncher
import autoUpdate
from flask import Flask, render_template,send_from_directory




app = Flask(__name__)
@app.route("/")
def Index():#首页
    check = autoUpdate.checkVersion()
    return render_template("index.html",check=check[0],content=check[1],home_active="mdui-list-item-active",apdate=autoUpdate)

@app.route("/files")
def Files():
        list = fileOpt.allFiles(os.getcwd())
        files = list["files"]
        dirs = list["dirs"]
        return render_template("files.html",files = files,dirs=dirs,files_active="mdui-list-item-active")
@app.route("/mods")
def Mods():
    return render_template("mods.html",mods_active="mdui-list-item-active")

@app.route("/downloads")
def Downloads():
    return render_template("index.html",downloads_active="mdui-list-item-active")

@app.route("/settings")
def Settings():
    return render_template("settings.html",settings_active="mdui-list-item-active")

@app.route("/lunch")
def Lunch():
    luncher.forgeLuncher(r"F:\Java8\bin\javaw.exe","./.minecraft","1.7.10-Forge10.13.4.1614-1.7.10","Yixixi","480","854")
    return render_template("lunch.html")
    
if __name__ == "__main__":
    app.run(debug=True,port=43433)


