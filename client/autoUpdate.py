import requests 

def lunchCount(url):
    re = requests.get(url)
    return True