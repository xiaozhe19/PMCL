import json


try:
    data = open("./config.json")
    jsons = json.load(data)
    # print(jsons)
    version = jsons["version"]
    update_url = jsons["update-url"]
    java_path = jsons["java-path"]
    mc_path = jsons[r".minecraft-path"]
    debug = jsons["debug"]
    last_game_version = jsons["last-game-version"]
    maxMem = jsons["maxMem"]
    height = jsons["height"]
    length = jsons["length"]
except:
    version = False
    update_url = False
    java_path = False
    mc_path = False
    debug = False
    last_game_version = False
    maxMem = False
    height = False
    length = False  
def juniorJson(Version,mcPath,javaPath,MaxMem,Height,Length):
    datadic = {}
    datadic["version"] =version
    datadic["update-url"] = update_url
    datadic["java-path"] =javaPath
    datadic[r".minecraft-path"] = mcPath
    datadic["debug"] = debug
    datadic["last-game-version"] = Version
    datadic["maxMem"] = MaxMem
    datadic["height"] = Height
    datadic["length"] = Length
    dataJson = json.dumps(datadic)
    file= open("./config.json","w")
    file.write(dataJson)
    file.close()

juniorJson("Version","mcPath","javaPath","MaxMem","Height","Length")



