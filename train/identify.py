import requests
import base64
import json

headers = {
    "x-api-key":"Fhpm5sx61t7IsUFt3bYRH9cefkPYDAxG5U8UZfJJ",
    "Content-Type":"application/json",  
}

url = "https://api.chui.ai/v1/identify"

cid = 'ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgMCB7Z8JDA'
data = {
    "img":base64.b64encode(open('BabyPhotos/Baby Tired/Tired8.jpg','rb').read()),
    "collection_id": cid
}

r  = requests.post(url,data=json.dumps(data),headers=headers)

print(r.json())
