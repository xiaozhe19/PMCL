import requests as re
import json

#yggdrasil verify

def yggdrasil(account,password):
    url = "https://authserver.mojang.com/authenticate"
    dic = {

            "agent": {
                "name": "Minecraft",
                "version": 1
            },
            "username": account,
            "password": password,

        
    }
    data = json.dumps(dic)
    print(data)
    res = re.post(url=url,data=data)
    print(res.text)

yggdrasil("bruno.declerck@live.fr","fa369651")