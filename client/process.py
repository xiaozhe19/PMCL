from multiprocessing import Process
from os import getpid
from random import randint
from time import time,sleep
import launcher
'''
def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
'''
def sponsor():
    print("launching, please wait...")

def main():
    start = time()
    p1 = Process(target=launcher.launcher, args=("F:/Java8/bin/java.exe", "./.minecraft", r"1.8","1024m","2048m", "Yixixi", "480", "854"))
    p1.start()
    p2 = Process(target=sponsor, args=())
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))

def noprocess():
    start = time()
    launcher.launcher("F:/Java8/bin/java.exe", "./.minecraft", r"1.8","1024m","2048m", "Yixixi", "480", "854")
    sponsor()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))
if __name__ == '__main__':
    main()