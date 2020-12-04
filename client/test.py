import requests as r
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

re = r.get("https://authserver.mojang.com",headers = headers)
print(re.text)
 