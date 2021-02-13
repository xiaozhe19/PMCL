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
    datadic = {}
    datadic["version"] =version
    datadic["way"] =way
    datadic["update-url"] = update_url
    datadic["java-path"] =javaPath
    datadic[r".minecraft-path"] = mcPath
    datadic["debug"] = debug
    datadic["last-game-version"] = Version
    datadic["maxMem"] = MaxMem
    datadic["height"] = Height
    datadic["length"] = Length
    datadic["background"] = bkimg
    datadic["downloadsource"] = downloadsource
    datadic["port"] = port
    datadic["username"] = "xiao_zhe"
    dataJson = json.dumps(datadic)
    file= open("./config.json","w")
    file.write(dataJson)
    file.close()

def pmclJson(Bkimg,Downloadsource,Port,Debug):
    datadic = {}
    datadic["version"] =version
    datadic["update-url"] = update_url
    datadic["java-path"] =java_path
    datadic[r".minecraft-path"] = mc_path
    datadic["debug"] = Debug
    datadic["way"] =way
    datadic["last-game-version"] = last_game_version
    datadic["maxMem"] = maxMem
    datadic["height"] = height
    datadic["length"] = length
    datadic["background"] = Bkimg
    datadic["downloadsource"] = Downloadsource
    datadic["port"] = Port
    datadic["username"] = "xiao_zhe"
    dataJson = json.dumps(datadic)
    file= open("./config.json","w")
    file.write(dataJson)
    file.close()

def offlineJson(id):
    datadic = {}
    datadic["way"] ="offline"
    datadic["version"] =version
    datadic["update-url"] = update_url
    datadic["java-path"] =java_path
    datadic[r".minecraft-path"] = mc_path
    datadic["debug"] = debug
    datadic["last-game-version"] = last_game_version
    datadic["maxMem"] = maxMem
    datadic["height"] = height
    datadic["length"] = length
    datadic["background"] = bkimg
    datadic["downloadsource"] = downloadsource
    datadic["port"] = port
    datadic["username"] = id
    dataJson = json.dumps(datadic)
    file= open("./config.json","w")
    file.write(dataJson)
    file.close()

