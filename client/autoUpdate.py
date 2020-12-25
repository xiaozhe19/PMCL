import requests as r
import os
import zipfile

url = "http://localhost:5000/update/0.0.1"


re = r.get(url)#尝试连接
try:#检验连接
    re.raise_for_status()
    #写入
    download = open("./download.txt","wb")
    for chunk in re.iter_content(chunk_size=512):
        if chunk:
            download.write(chunk)
    download.close()
    #重命名为压缩包
    os.rename("./download.txt","download.zip")
    #解压
    zfile = zipfile.ZipFile("./download.zip","r")
    zfile.extractall()

except Exception as exc:
    print('There was a problem: %s' % (exc))


