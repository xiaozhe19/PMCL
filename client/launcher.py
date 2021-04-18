import json
import os
import re
import threading
import time
import subprocess

# 启动器主逻辑
# 重写完成 2021.4.18

def launcher(java_path, game_path, game_version,Xmx,Xmn, username, height, width,extra="",uuid="074d7f3c274533daab03840cbfc275a9",accessToken="05df4d5f10354b708fb515655e3c3693"):
    """启动mc的模块

    Args:
        java_path (String): java路径
        game_path (String): 游戏本体路径
        game_version (String): 启动的游戏版本
        Xmx (String): 最大虚拟内存
        Xmn (String): 最小虚拟内存
        username (String): 用户名
        height (String): 窗口高度
        width (String): 窗口宽度
    """
    XX = "-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M"
    libpath = "-Djava.library.path="+game_path+"/versions/"+game_version+"/"+"natives"
    minMem = "-Xmn " + Xmn
    maxMem = "-Xmx " +Xmx
    data = open(game_path+'/versions/'+game_version+'/' +
                game_version+'.json', encoding='utf-8')
    jsonString = json.load(data)
    # 获取所需参数内容
    mainClass = jsonString['mainClass']

    #!需要优化
    minecraftArguments = jsonString["minecraftArguments"] 
    a = minecraftArguments.split(" ")
    s = ''
    b=[]
    c = [username,game_version,game_path,game_path+r'/assets',jsonString['id'],uuid,accessToken,'{}','Mojang']
    for i in range(0,len(a)):
        if "$"in a[i]:
            b.append(i)
    for i in range(0,len(b)):
        a[b[i]] = c[i]
    for i in range(0,len(a)):
        s= s+' '+a[i]
    minecraftArguments = s

    path = []
    libraries = jsonString['libraries']
    id = jsonString['id']
    jar = jsonString['assets']
    for i in range(0, len(libraries)):
        names = libraries[i]
        names = names['name'].split(':')
        first = names[0].replace('.', '/')
        second = names[1]
        third = names[2]
        fourth = second + '-' + third
        path.append(game_path+'/libraries/'+first + '/' +
                    second + '/' + third+'/'+fourth+'.jar')
    path.append("./.minecraft/versions/"+jar+'/'+jar+'.jar')
    path.append(#需要修改
        "./.minecraft/libraries/net/minecraftforge/forge/"+"1.8-11.14.4.1577"+"/"+"1.8-11.14.4.1577"+".jar")
    path.append(
        "./.minecraft/libraries/net/minecraft/launchwrapper/"+game_version+"/launchwrapper-"+game_version+".jar")
    mainClass = jsonString["mainClass"]
    javaPackage = '-cp' + ' "'
    extra_jvm=extra
    for i in path:
        javaPackage = javaPackage + i+';'
    javaPackage = javaPackage + '"'
    command = java_path+" " +" "+XX +" "+extra_jvm+"  "+libpath+" " + javaPackage +" "+mainClass+" "+minecraftArguments
    ret = subprocess.run(command, shell=True)
    print(command)

launcher("F:/Java8/bin/java.exe", "./.minecraft", r"1.7.10","1024m","2048m", "Yixixi", "480", "854")

