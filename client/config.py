import json


try:
    data = open("./config.json")
    jsons = json.load(data)
    # print(jsons)
    version = jsons["version"]
    update_url = jsons["update-url"]
    java_path = jsons["java-path"]
    username = jsons["username"]
    mc_path = jsons[r".minecraft-path"]
    debug = jsons["debug"]
    last_game_version = jsons["last-game-version"]
    maxMem = jsons["maxMem"]
    height = jsons["height"]
    length = jsons["length"]
    bkimg = jsons["background"]
    downloadsource = jsons['downloadsource']
    port =jsons["port"]
    way = jsons["way"]
except Exception as e:
    version = "False"
    update_url = "False"
    java_path = "False"
    mc_path = "False"
    username = "False"
    debug = "False"
    last_game_version = "False"
    maxMem = "False"
    height = "False"
    length = "False"
    bkimg = "False"
    downloadsource = "False"
    way = "False"
    port ="False"
    print(e)
def juniorJson(Version,mcPath,javaPath,MaxMem,Height,Length):
    jsons["last-game-version"] = Version
    jsons[r".minecraft-path"] = mcPath
    jsons["java-path"] =javaPath
    jsons["maxMem"] = MaxMem
    jsons["height"] = Height
    jsons["length"] = Length
    dataJson = json.dumps(jsons)
    file= open("./config.json","w")
    file.write(dataJson)
    file.close()

def pmclJson(Bkimg,Downloadsource,Port,Debug):
    """启动器设置Json

    Args:
        Bkimg (String): [description]
        Downloadsource (String): [description]
        Port (String): [description]
        Debug (String): [description]
    """
    jsons["background"] = Bkimg
    jsons["downloadsource"] = Downloadsource
    jsons["port"] = Port
    jsons["debug"] = Debug
    dataJson = json.dumps(jsons)
    file= open("./config.json","w")
    file.write(dataJson)
    file.close()

def offlineJson(id):
    """离线模式启动json
    Args:
        id (String): 离线登录的id
    """
    jsons["way"] ="offline"
    jsons["username"] = id
    dataJson = json.dumps(jsons)
    file= open("./config.json","w")
    file.write(dataJson)
    file.close()

