import requests
import base64
import json
import time

# {"data": {"collection_id": "ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgMCB7Z8JDA"}, "message": "Collection created successfully.", "success": true}
headers = {
    "x-api-key":"Fhpm5sx61t7IsUFt3bYRH9cefkPYDAxG5U8UZfJJ",
    "Content-Type":"application/json",  
}

url = "https://api.chui.ai/v1/collection"


def create():
    #{"data": {"collection_id": "ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgMCB7Z8JDA"}, "message": "Collection created successfully.", "success": true}
    data = {
        "name":"Baby",
    }
    r  = requests.post(url,data=json.dumps(data),headers=headers)
    print(r.content)

def add_profiles():
    cid = 'ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgMCB7Z8JDA'
    data = {
        "enrollment_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgMCn148KDA",
        "collection_id": cid,
        "name": "bathroom"
    }
    r  = requests.post(url, data=json.dumps(data),headers=headers)
    print("bathroom")
    print(r.content)

    time.sleep(3)
    eid = "ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgKCcovcIDA"
    data = {
        "enrollment_id": eid,
        "collection_id": cid,
        "name": "hungry"
    }
    r  = requests.post(url, data=json.dumps(data),headers=headers)
    print("hungry")
    print(r.content)

    time.sleep(3)
    eid = "ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgMDji5QKDA"
    data = {
        "enrollment_id": eid,
        "collection_id": cid,
        "name": "pain"
    }
    r  = requests.post(url, data=json.dumps(data),headers=headers)
    print("pain")
    print(r.content)

    time.sleep(3)
    eid = "ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgMCBwoYKDA"
    data = {
        "enrollment_id": eid,
        "collection_id": cid,
        "name": "tired"
    }
    r  = requests.post(url, data=json.dumps(data),headers=headers)
    print("tired")
    print(r.content)


if __name__ == '__main__':
    add_profiles()
