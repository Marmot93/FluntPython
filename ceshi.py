# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 3:54 PM
# @Author  : Marmot
# @File    : ceshi.py

import requests

url = "https://127.0.0.1:8080/v1/user"
Authorization = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MzEyNzkwNDYsImlkIjoyLCJuYmYiOjE1MzEyNzkwNDYsInVzZXJuYW1lIjoibWFybW90In0.9I08P-OsHnFtoAekEaErBwaEGZpRrlvcvA3_kX3UmbY"
headers = {
    'Authorization': Authorization,
    'Cache-Control': "no-cache"
}
cert = "/Users/marmot/go/src/marmot/src/marmot/conf/server.crt"
key = "/Users/marmot/go/src/marmot/src/marmot/conf/server.key"

response = requests.request("GET", url, headers=headers, cert=(cert, key))

print(response.text)
