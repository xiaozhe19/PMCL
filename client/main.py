import json
import os
import time
import fileOpt
import launcher
import autoUpdate
from flask import Flask, render_template,send_from_directory,jsonify,request
import config



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
    versions = fileOpt.getVersion("./.minecraft/versions")
    return render_template("settings.html",versions=versions,settings_active="mdui-list-item-active")

@app.route("/lunch")
def Lunch():
    launcher.launcher(r"F:\Java8\bin\javaw.exe","./.minecraft","1.7.10","1024m","2048m","Yixixi","480","854")
    return render_template("lunch.html")
 


@app.route("/juniorjson",methods=["POST"])
def juniorjson():
    data_list = []
    data = json.loads(request.get_data(as_text=True))   # request.get_data(as_text=True) ： 获取前端POST请求传过来的 json 数据
    print(data)
    config.juniorJson(data["version"],data["gamePath"],data["javaPath"],data["maxMem"],data["height"],data["length"])
    return data


@app.route("/pmcljson",methods=["POST"])
def pmcljson():
    data_list = []
    data = json.loads(request.get_data(as_text=True))   # request.get_data(as_text=True) ： 获取前端POST请求传过来的 json 数据
    print(data)
    return data

if __name__ == "__main__":
    app.run(debug=config.debug,port=43433)


