import os
'''
def correctMinecraftMainDic():
    getAllFiles = os.listdir()
    if '.minecraft' in getAllFiles:#寻找.minecraft文件夹,.不可做变量名开头，改为_
        _minecraft = True
    else:
        _minecraft = False
    getAllFiles = os.walk("./.minecraft")
    for root,dirs,files in getAllFiles:
        print(root)
        print(dirs)
        print(files)
    return _minecraft,assets,lib,versions
    '''


def getVersion(path):  # 获取所有存在的版本
    versions = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if 'json' in file:  # 获取json文档
                versions.append(os.path.splitext(file)[0])

    return versions




def allFiles(path):
    results = {"dirs": 0,
               "files": 0, }
    files = []
    dirs = []
    path = os.listdir(path)
    for p in path:
        if os.path.isdir(p):
            dirs.append(p)
        elif os.path.isfile(p):
            files.append(p)
    results["dirs"] = dirs
    results['files'] = files
    return results
