import json
import os
import time

from flask import Flask, render_template


def get_all_path(open_file_path,version):
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
count = 0

app = Flask(__name__)
@app.route("/")
def indexHtml():
    return render_template("index.html", count = count)
@app.route("/count")#计数
def countlin():
    global count 
    count  = count+1
    return "True"
@app.route("/update-get",methods=['GET'])
def hello_world():
    data = open(r"server\update.json",encoding='utf-8')
    data = json.load(data)
    return data

@app.route("/update-post")
def update_post():
    check = get_all_path(r"server\newPack","0.0.1-beta")

    return str(check)
if __name__ == "__main__":
    app.run(debug=True)

