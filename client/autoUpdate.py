import requests as r
import os
import zipfile
import json

def checkVersion():
    data = open("./config.json")
    aq = json.load(data)
    data.close()
    version = aq["version"]
    url = aq["update-url"]
    url = url+r"/update-get"
    try:  # 检验连接
        re = r.get(url)  # 尝试连接
        result = json.loads(re.text)
        if version == result["version"]:
            return [False,""]
        else:
            return [True,result["content"]]
    except Exception as exc:
        return [False,exc]

def update():
    data = open("./config.json")
    aq = json.load(data)
    data.close()
    version = aq["version"]
    url = aq["update-url"]
    url = url+r"/update"
    re = r.get(url)  # 尝试连接
    try:  # 检验连接
        re.raise_for_status()
        # 写入
        download = open("./download.txt", "wb")
        for chunk in re.iter_content(chunk_size=512):
            if chunk:
                download.write(chunk)
        download.close()
        # 重命名为压缩包
        os.rename("./download.txt", "download.zip")
        # 解压
        #zfile = zipfile.ZipFile("./download.zip", "r")
        #zfile.extractall()

    except Exception as exc:
        print('There was a problem: %s' % (exc))
