import json

def loadConfig():
    try:
        data = open("./config.json")
        jsons = json.load(data) 
        #print(jsons)
        version = jsons["version"]
        update_url= jsons["update-url"]
        java_path = jsons["java-path"]
        mc_path = jsons[r".minecraft-path"]
        debug = jsons["debug"]
        last_game_version = jsons["last-game-version"]
        maxMem = jsons["maxMem"]
        height = jsons["height"]
        length = jsons["length"]
        return [version,update_url,java_path,mc_path,debug,last_game_version,maxMem,height,length]
    except Exception as exc:
        return exc
