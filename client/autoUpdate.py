import requests as r
import os
import zipfile
import json
import config

#update
def checkVersion():
    version = config.version
    url = config.update_url
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
    version = config.version
    url = config.update_url
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
        return True
    except Exception as exc:
        return ('There was a problem: %s' % (exc))

def unzip(name):
    file = zipfile.ZipFile(name)
    file.extractall()
    file.close()

#下载完成后，弹出对话框，是否安装，安装完毕之后重启