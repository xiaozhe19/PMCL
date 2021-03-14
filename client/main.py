import json
import os
import time
import fileS
import launcher
import autoUpdate
from flask import Flask, render_template, send_from_directory, jsonify, request, redirect, url_for
import config
import importlib
import webbrowser

app = Flask(__name__)


@app.route("/")
def Index():  # 首页
    check = autoUpdate.checkVersion()
    return render_template("index.html", check=check[0], content=check[1], home_active="mdui-list-item-active", apdate=autoUpdate, user=config.username, way=config.way,icon="icon")


@app.route("/files")
def Files():
    list = fileS.allFiles(os.getcwd())
    files = list["files"]
    dirs = list["dirs"]
    return render_template("files.html", files=files, dirs=dirs, files_active="mdui-list-item-active")


@app.route("/mods")
def Mods():
    return render_template("mods.html", mods_active="mdui-list-item-active")


@app.route("/downloads")
def Downloads():
    return render_template("index.html", downloads_active="mdui-list-item-active")


@app.route("/settings")
def Settings():
    versions = fileS.getVersion("./.minecraft/versions")
    return render_template("settings.html", versions=versions, chosen_version=config.last_game_version, settings_active="mdui-list-item-active", gamePath=config.mc_path, javaPath=config.java_path, maxMem=config.maxMem, length=config.length, height=config.height,
                           bkimg=config.bkimg, downloadsource=config.downloadsource, port=config.port, debug=config.debug)


@app.route("/launch")
def Launch():
    launcher.launcher(config.java_path, config.mc_path, config.last_game_version,
                      "516m", config.maxMem, config.username, config.height, config.length)
    return render_template("launch.html")


@app.route("/juniorjson", methods=["POST"])
def juniorjson():
    data_list = []
    # request.get_data(as_text=True) ： 获取前端POST请求传过来的 json 数据
    data = json.loads(request.get_data(as_text=True))
    config.juniorJson(data["version"], data["gamePath"], data["javaPath"],
                      data["maxMem"], data["height"], data["length"])
    importlib.reload(config)
    return data


@app.route("/pmcljson", methods=["POST"])
def pmcljson():
    data_list = []
    data = json.loads(request.get_data(as_text=True))
    config.pmclJson(data["bkimg"], data["downloadsource"],
                    data['port'], data["debug"])
    importlib.reload(config)
    return data


@app.route("/offline", methods=["POST"])
def offline():
    data_list = []
    data = json.loads(request.get_data(as_text=True))
    config.offlineJson(data["id"])
    importlib.reload(config)
    return redirect("./")


@app.route("/signout", methods=["POST", "GET"])
def signout():
    config.offlineJson(False)
    importlib.reload(config)
    return redirect("./")


if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:'+config.port, 0, False)
    app.run(debug=config.debug, port=config.port)
