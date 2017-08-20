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
    data_hungry = {
        "img0":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry9.jpg','rb').read()),
        "img1":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry10.jpg','rb').read()),
        "name": "hungry"
    }
    r  = requests.post(url, data=json.dumps(data_hungry), headers=headers)
    print(r.json())

def additional_enroll():
    #{u'message': u'Enrollment processed successfully.', u'data': {u'enrollment_id': u'ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgKCcovcIDA'}, u'success': True}
    # data_additional = {
    #     "enrollment_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgKCcovcIDA",
    #     "img0":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry2.jpg','rb').read()),
    #     "img1":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry3.jpg','rb').read()),
    # }
    # print("1st additional")
    # r  = requests.post(url,data=json.dumps(data_additional),headers=headers)
    # print(r.text)

    data_additional2 = {
        "enrollment_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgKCcovcIDA",
        "img0":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry4.jpg','rb').read()),
        "img1":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry5.jpg','rb').read()),
    }
    print("2nd additional")
    r  = requests.post(url,data=json.dumps(data_additional2),headers=headers)
    print(r.text)

    time.sleep(3)
    data_additional3 = {
        "enrollment_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgKCcovcIDA",
        "img0":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry6.jpg','rb').read()),
        "img1":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry7.png','rb').read()),
    }
    print("3rd additional")
    r  = requests.post(url,data=json.dumps(data_additional3),headers=headers)
    print(r.text)

    time.sleep(3)
    data_additional4 = {
        "enrollment_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgKCcovcIDA",
        "img0":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry8.jpg','rb').read()),
    }
    print("4th additional")
    r  = requests.post(url,data=json.dumps(data_additional4),headers=headers)
    print(r.text)


if __name__ == '__main__':
    #initial_enroll()
    additional_enroll()
