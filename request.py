import requests
import json

url = 'http://202.204.121.159/book/book184/postDrag.php'
headers = {
    "Host": "202.204.121.159",
    "Connection": "keep-alive",
    # "Content-Length": "9",
    "Accept": "*/*",
    "Origin": "http://202.204.121.159",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
    "Referer": "http://202.204.121.159/book/book184/app_index.php?unit=1",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "NCCE=1acf337a350acefa62f2503f4216c660; Hm_lvt_8a1d0cf914523c7ed112dbd25e018957=1521388665; Hm_lpvt_8a1d0cf914523c7ed112dbd25e018957=1521389835"
}


r = requests.post(url, data=json.dumps({
    'ItemID':10
}), headers=headers)
print(r.content)
