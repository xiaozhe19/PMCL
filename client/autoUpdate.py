import requests as r
import os

url = "http://localhost:5000/update/0.0.1"


re = r.get(url)
try:#尝试连接
    re.raise_for_status()
    download = open("./download.txt","wb")
    for chunk in re.iter_content(chunk_size=512):
        if chunk:
            download.write(chunk)
    download.close()
    os.rename("./download.txt","download.zip")
except Exception as exc:
    print('There was a problem: %s' % (exc))
