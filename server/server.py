import json
import os
import time

from flask import Flask, render_template,send_from_directory


def get_all_path(open_file_path,version):#写入新版本
    data = open(r"server\update.json",'w',encoding="utf-8")
    info = []
    index = ["name","path","last_alter_time","in_version"]
    output =[]
    localtime = time.asctime( time.localtime(time.time()) )
    for root,dirs,files in os.walk(open_file_path):
        for file in files:
            _path = os.path.join(root,file)
            _mtime = time.ctime(os.stat(_path).st_mtime)
            info.append(file)
            info.append(_path)
            info.append(_mtime)
            info.append(version)
            dic = dict(zip(index,info))
            info.clear()
            output.append(dic)
    writeInJson = {"version":version,"publish_time":str(localtime),"file":output}
    data.write(json.dumps(writeInJson))
    return True


def updateData(version):#获取当亲最新版本
    file = open(r"server\update.json",'r',encoding="utf-8")
    data = json.loads(file.read())
    if version == data["version"]:
        path = 'fku'
        return path
    else:
        path = data["version"]+".zip"
        return path
count = 0

app = Flask(__name__)
@app.route("/")
def indexHtml():#首页
    return render_template("index.html", count = count)

@app.route("/count")#计数
def countlin():
    global count 
    count  = count+1
    return "True"

@app.route("/update-get",methods=['GET'])#获取最新版本
def hello_world():
    data = open(r"server\update.json",encoding='utf-8')
    data = json.load(data)
    VERSION = data["version"]
    return VERSION

@app.route("/update/<Nversion>",methods=['GET'])#获取更新
def update(Nversion):
    check = updateData(Nversion)
    if check == "fku":
        return "False"
    else:
        directory = os.getcwd()+'/server'  # 当前目录
        return send_from_directory(directory,filename=check,as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

