import json
import os
import re
#启动器主逻辑

def forgeLuncher(java_path,game_path,game_version,username,height,width):
    #打开对应版本json
    data = open(game_path+'/versions/'+game_version+'/'+game_version+'.json', encoding='utf-8')
    jsonString = json.load(data)
    #获取所需参数内容
    mainClass = jsonString['mainClass']
    minecraftArguments = '--username '+username+'  --version '+game_version+'  --gameDir '+game_path+'  --assetsDir ' +game_path+'/assets'+'  --assetIndex 1.7.10  --uuid 645a46ff8a5f39037e5b3677a9f6d0c9  --accessToken 645a46ff8a5f39037e5b3677a9f6d0c9  --userProperties {}  --userType Legacy --tweakClass cpw.mods.fml.common.launcher.FMLTweaker  --height  '+ height +'   --width '+width
    libraries = jsonString['libraries']
    id = jsonString['id']
    jar = jsonString['assets']
    #通过json获取包的路径（forge）
    path=[]
    for i in range(0,len(libraries)):
        names = libraries[i]
        names = names['name'].split(':')
        first = names[0].replace('.','/')
        second = names[1]
        third = names[2]
        fourth = second + '-' + third
        path.append('./.minecraft/libraries/'+first +'/' +second +'/' +third+'/'+fourth+'.jar')
    path.append("./.minecraft/versions/"+jar+'/'+jar+'.jar')  
    path.append("./.minecraft/libraries/net/minecraftforge/forge/"+id+"/"+id+".jar")
    #通过json获取包路径（原版）
    data = open(game_path+'/versions/'+jar+'/'+jar+'.json',encoding='utf-8')
    jsonString = json.load(data)
    libraries = jsonString['libraries']

    for i in range(0,len(libraries)):
        names = libraries[i]
        names = names['name'].split(':')
        first = names[0].replace('.','/')
        second = names[1]
        third = names[2]
        fourth = second + '-' + third
        path.append('./.minecraft/libraries/'+first +'/' +second +'/' +third+'/'+fourth+'.jar')
    path.append("./.minecraft/libraries/net/minecraft/launchwrapper/1.12/launchwrapper-1.12.jar")
    #jvm参数
    _XX = '-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump  -XX:+UseConcMarkSweepGC  -XX:+CMSIncrementalMode  -XX:-UseAdaptiveSizePolicy  -XX:-OmitStackTraceInFastThrow'
    maxMem = '-Xmx1024m'
    Dsettings = '-Dfml.ignoreInvalidMinecraftCertificates=true -Dfml.ignorePatchDiscrepancies=true "-Djava.library.path=C:/Users/Zhenyu Zhang/Desktop/minecraft/.minecraft/versions/1.7.10-Forge10.13.4.1614-1.7.10/1.7.10-Forge10.13.4.1614-1.7.10-natives"'
    javaPackage = '-cp' + ' "'
    for i in path: 
        javaPackage = javaPackage   +i+';'
    javaPackage = javaPackage + '"'
    #拼接命令
    command = java_path+' '+_XX+' '+maxMem+' '+Dsettings+' '+' '+javaPackage+' '+mainClass+' '+minecraftArguments
    #执行
    os.system(command)



#forgeLuncher("java","./.minecraft","1.7.10-Forge10.13.4.1614-1.7.10","Yixixi","480","854")