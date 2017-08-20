import requests
import base64
import json

headers = {
    "x-api-key":"Fhpm5sx61t7IsUFt3bYRH9cefkPYDAxG5U8UZfJJ",
    "Content-Type":"application/json",
}
url = "https://api.chui.ai/v1/enroll"

data_bathroom = {
    "img_bathroom_1":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom1.png','rb').read()).decode("utf-8")),
    "img_bathroom_2":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom10.jpg','rb').read()).decode("utf-8")),
    "img_bathroom_3":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom2.jpg','rb').read()).decode("utf-8")),
    "img_bathroom_4":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom3.jpg','rb').read()).decode("utf-8")),
    "img_bathroom_5":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom4.jpg','rb').read()).decode("utf-8")),
    "img_bathroom_6":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom5.jpg','rb').read()).decode("utf-8")),
    "img_bathroom_6":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom6.jpg','rb').read()).decode("utf-8")),
    "img_bathroom_8":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom7.jpg','rb').read()).decode("utf-8")),
    "img_bathroom_9":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom8.jpg','rb').read()).decode("utf-8")),
    "img_bathroom_10":str(base64.b64encode(open('BabyPhotos/Baby Bathroom/Bathroom9.jpg','rb').read()).decode("utf-8")),
    "name": "bathroom"
}

data_hungry = {
    "img_hungry_1":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry1.jpg','rb').read()),
    "img_hungry_2":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry10.jpg','rb').read()),
    "img_hungry_3":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry2.jpg','rb').read()),
    "img_hungry_4":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry3.jpg','rb').read()),
    "img_hungry_5":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry4.jpg','rb').read()),
    "img_hungry_6":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry5.jpg','rb').read()),
    "img_hungry_7":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry6.jpg','rb').read()),
    "img_hungry_8":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry7.png','rb').read()),
    "img_hungry_9":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry8.jpg','rb').read()),
    "img_hungry_10":base64.b64encode(open('BabyPhotos/Baby Hungry/Hungry9.jpg','rb').read()),
    "name": "hungry"
}

data_pain = {
    "img_pain_1":base64.b64encode(open('BabyPhotos/Baby Pain/Pain10.jpg','rb').read()),
    "img_pain_2":base64.b64encode(open('BabyPhotos/Baby Pain/Pain2.jpg','rb').read()),
    "img_pain_3":base64.b64encode(open('BabyPhotos/Baby Pain/Pain3.jpg','rb').read()),
    "img_pain_4":base64.b64encode(open('BabyPhotos/Baby Pain/Pain4.jpg','rb').read()),
    "img_pain_5":base64.b64encode(open('BabyPhotos/Baby Pain/Pain5.jpg','rb').read()),
    "img_pain_6":base64.b64encode(open('BabyPhotos/Baby Pain/Pain6.jpg','rb').read()),
    "img_pain_7":base64.b64encode(open('BabyPhotos/Baby Pain/Pain7.jpg','rb').read()),
    "img_pain_8":base64.b64encode(open('BabyPhotos/Baby Pain/Pain8.jpg','rb').read()),
    "img_pain_9":base64.b64encode(open('BabyPhotos/Baby Pain/Pain9.jpg','rb').read()),
    "name": "pain"
}
data_tired = {
    "img_tired_1":base64.b64encode(open('BabyPhotos/Baby Tired/Tired1.jpg','rb').read()),
    "img_tired_2":base64.b64encode(open('BabyPhotos/Baby Tired/Tired10.jpg','rb').read()),
    "img_tired_3":base64.b64encode(open('BabyPhotos/Baby Tired/Tired2.jpg','rb').read()),
    "img_tired_4":base64.b64encode(open('BabyPhotos/Baby Tired/Tired3.jpg','rb').read()),
    "img_tired_5":base64.b64encode(open('BabyPhotos/Baby Tired/Tired4.jpg','rb').read()),
    "img_tired_6":base64.b64encode(open('BabyPhotos/Baby Tired/Tired5.jpg','rb').read()),
    "img_tired_7":base64.b64encode(open('BabyPhotos/Baby Tired/Tired6.jpg','rb').read()),
    "img_tired_8":base64.b64encode(open('BabyPhotos/Baby Tired/Tired7.jpg','rb').read()),
    "img_tired_9":base64.b64encode(open('BabyPhotos/Baby Tired/Tired8.jpg','rb').read()),
    "img_tired_10":base64.b64encode(open('BabyPhotos/Baby Tired/Tired9.jpg','rb').read()),
    "name":"tired"
}

#r  = requests.post(url, data=json.dumps(data_hungry), headers=headers)
#print(r.json())

print(json.dumps(data_bathroom))
