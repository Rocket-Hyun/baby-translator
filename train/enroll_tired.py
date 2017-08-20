import requests
import base64
import json
import time

headers = {
    "x-api-key":"Fhpm5sx61t7IsUFt3bYRH9cefkPYDAxG5U8UZfJJ",
    "Content-Type":"application/json",
}
url = "https://api.chui.ai/v1/enroll"


def initial_enroll():
    #{u'message': u'Enrollment processed successfully.', u'data': {u'enrollment_id': u'ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgMCBwoYKDA'}, u'success': True}
    data = {
        "img0":base64.b64encode(open('BabyPhotos/Baby Tired/Tired2.jpg','rb').read()),
        "img1":base64.b64encode(open('BabyPhotos/Baby Tired/Tired3.jpg','rb').read()),
#        "img0":base64.b64encode(open('BabyPhotos/Baby Tired/Tired1.jpg','rb').read()),
#        "img0":base64.b64encode(open('BabyPhotos/Baby Tired/Tired10.jpg','rb').read()),
        "name": "tired"
    }
    r  = requests.post(url, data=json.dumps(data), headers=headers)
    print(r.json())

def additional_enroll():
    data_additional2 = {
        "enrollment_id": "ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgMCBwoYKDA",
        "img0":base64.b64encode(open('BabyPhotos/Baby Tired/Tired4.jpg','rb').read()),
        "img1":base64.b64encode(open('BabyPhotos/Baby Tired/Tired5.jpg','rb').read()),
    }
    print("2nd additional")
    r  = requests.post(url,data=json.dumps(data_additional2),headers=headers)
    print(r.text)

    time.sleep(3)
    data_additional3 = {
        "enrollment_id": "ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgMCBwoYKDA",
        "img0":base64.b64encode(open('BabyPhotos/Baby Tired/Tired6.jpg','rb').read()),
        "img1":base64.b64encode(open('BabyPhotos/Baby Tired/Tired7.jpg','rb').read()),
    }
    print("3rd additional")
    r  = requests.post(url,data=json.dumps(data_additional3),headers=headers)
    print(r.text)

    time.sleep(3)
    data_additional4 = {
        "enrollment_id": "ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgMCBwoYKDA",
        "img0":base64.b64encode(open('BabyPhotos/Baby Tired/Tired8.jpg','rb').read()),
        "img1":base64.b64encode(open('BabyPhotos/Baby Tired/Tired9.jpg','rb').read()),
    }
    print("4th additional")
    r  = requests.post(url,data=json.dumps(data_additional4),headers=headers)
    print(r.text)


if __name__ == '__main__':
    #initial_enroll()
    additional_enroll()
