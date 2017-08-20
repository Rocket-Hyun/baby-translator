import requests
import base64
import json

headers = {
    "content-type":"application/json",
    "x-api-key":"Fhpm5sx61t7IsUFt3bYRH9cefkPYDAxG5U8UZfJJ",
}

url = "https://api.chui.ai/v1/train"

cid = 'ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgMCB7Z8JDA'
data = {
  "collection_id": cid
}

r  = requests.post(url,data=json.dumps(data),headers=headers)

#{'data': {'collection_id': 'ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgMCB7Z8JDA'}, 'message': 'Retraining the classifier.', 'success': True}

print(r.json())
