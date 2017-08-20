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
    #{u'message': u'Enrollment processed successfully.', u'data': {u'enrollment_id': u'ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgMDji5QKDA'}, u'success': True}
    data = {
#       "img0":base64.b64encode(open('BabyPhotos/Baby Pain/Pain10.jpg','rb').read()),
        "img0":base64.b64encode(open('BabyPhotos/Baby Pain/Pain2.jpg','rb').read()),
        "name": "pain"
    }
    r  = requests.post(url, data=json.dumps(data), headers=headers)
    print(r.json())

def additional_enroll():
    # data_additional = {
    #     "enrollment_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgMDji5QKDA",
    #     #"img0":base64.b64encode(open('BabyPhotos/Baby Pain/Pain3.jpg','rb').read()),
    #     "img0":base64.b64encode(open('BabyPhotos/Baby Pain/Pain4.jpg','rb').read()),
    # }
    # print("1st additional")
    # r  = requests.post(url,data=json.dumps(data_additional),headers=headers)
    # print(r.text)

    #time.sleep(3)
#     data_additional2 = {
#         "enrollment_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgMDji5QKDA",
#         "img0":base64.b64encode(open('BabyPhotos/Baby Pain/Pain5.jpg','rb').read()),
# #        "img1":base64.b64encode(open('BabyPhotos/Baby Pain/Pain6.jpg','rb').read()),
#     }
#     print("2nd additional")
#     r  = requests.post(url,data=json.dumps(data_additional2),headers=headers)
#     print(r.text)

#     time.sleep(3)
    data_additional3 = {
        "enrollment_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgMDji5QKDA",
        "img0":base64.b64encode(open('BabyPhotos/Baby Pain/Pain7.jpg','rb').read()),
        "img1":base64.b64encode(open('BabyPhotos/Baby Pain/Pain8.jpg','rb').read()),
    }
    print("3rd additional")
    r  = requests.post(url,data=json.dumps(data_additional3),headers=headers)
    print(r.text)

    time.sleep(3)
    data_additional4 = {
        "enrollment_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgMDji5QKDA",
        "img0":base64.b64encode(open('BabyPhotos/Baby Pain/Pain9.jpg','rb').read()),
    }
    print("4th additional")
    r  = requests.post(url,data=json.dumps(data_additional4),headers=headers)
    print(r.text)


if __name__ == '__main__':
    #initial_enroll()
    additional_enroll()
