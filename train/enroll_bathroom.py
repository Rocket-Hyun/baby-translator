import requests
import base64
import json

headers = {
    "x-api-key":"Fhpm5sx61t7IsUFt3bYRH9cefkPYDAxG5U8UZfJJ",
    "Content-Type":"application/json",
}
url = "https://api.chui.ai/v1/enroll"

# 'data': {'enrollment_id': 'ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgMCn148KDA'}, 'message': 'Enrollment processed successfully.', 'success': True}
data_bathroom = {
    "img0":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom1.png','rb').read()).decode("utf-8")),
    "img1":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom10.jpg','rb').read()).decode("utf-8")),
    "img3":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom2.jpg','rb').read()).decode("utf-8")),
    "img4":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom3.jpg','rb').read()).decode("utf-8")),
    "img5":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom4.jpg','rb').read()).decode("utf-8")),
    "img6":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom5.jpg','rb').read()).decode("utf-8")),
    "img6":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom6.jpg','rb').read()).decode("utf-8")),
    "img8":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom7.jpg','rb').read()).decode("utf-8")),
    "img9":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom8.jpg','rb').read()).decode("utf-8")),
    "img10":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom9.jpg','rb').read()).decode("utf-8")),
    "name": "bathroom"
}

data_hungry = {
    "img0":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry9.jpg','rb').read()),
    "img1":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry10.jpg','rb').read()),
    "img2":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry2.jpg','rb').read()),
    "img3":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry3.jpg','rb').read()),
    "img4":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry4.jpg','rb').read()),
    "img5":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry5.jpg','rb').read()),
    "img6":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry6.jpg','rb').read()),
    "img7":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry7.png','rb').read()),
    "img8":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry8.jpg','rb').read()),
    "name": "hungry"
}

data_pain = {
    "img0":base64.b64encode(open('BabyPhotos/Baby Pain/Pain10.jpg','rb').read()),
    "img1":base64.b64encode(open('BabyPhotos/Baby Pain/Pain2.jpg','rb').read()),
    "img2":base64.b64encode(open('BabyPhotos/Baby Pain/Pain3.jpg','rb').read()),
    "img3":base64.b64encode(open('BabyPhotos/Baby Pain/Pain4.jpg','rb').read()),
    "img4":base64.b64encode(open('BabyPhotos/Baby Pain/Pain5.jpg','rb').read()),
    "img5":base64.b64encode(open('BabyPhotos/Baby Pain/Pain6.jpg','rb').read()),
    "img6":base64.b64encode(open('BabyPhotos/Baby Pain/Pain7.jpg','rb').read()),
    "img7":base64.b64encode(open('BabyPhotos/Baby Pain/Pain8.jpg','rb').read()),
    "img8":base64.b64encode(open('BabyPhotos/Baby Pain/Pain9.jpg','rb').read()),
    "name": "pain"
}
data_tired = {
    "img0":base64.b64encode(open('BabyPhotos/Baby Tired/Tired1.jpg','rb').read()),
    "img1":base64.b64encode(open('BabyPhotos/Baby Tired/Tired10.jpg','rb').read()),
    "img2":base64.b64encode(open('BabyPhotos/Baby Tired/Tired2.jpg','rb').read()),
    "img3":base64.b64encode(open('BabyPhotos/Baby Tired/Tired3.jpg','rb').read()),
    "img4":base64.b64encode(open('BabyPhotos/Baby Tired/Tired4.jpg','rb').read()),
    "img5":base64.b64encode(open('BabyPhotos/Baby Tired/Tired5.jpg','rb').read()),
    "img6":base64.b64encode(open('BabyPhotos/Baby Tired/Tired6.jpg','rb').read()),
    "img7":base64.b64encode(open('BabyPhotos/Baby Tired/Tired7.jpg','rb').read()),
    "img8":base64.b64encode(open('BabyPhotos/Baby Tired/Tired8.jpg','rb').read()),
    "img9":base64.b64encode(open('BabyPhotos/Baby Tired/Tired9.jpg','rb').read()),
    "name":"tired"
}

r  = requests.post(url, data=json.dumps(data_hungry), headers=headers)
print(r.json())
