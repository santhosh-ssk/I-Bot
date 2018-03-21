import json,requests
image_path='/home/santhosh/svce_innovates/flask-chatterbot/Savior.jpeg'
response = requests.post('https://stark-brook-57528.herokuapp.com/api/image_classifier',
files={'image': open(image_path, 'rb')})
print(response.json())
files={'image': open(image_path, 'rb')}
print(files)
api_key = 'acc_a8a69b84e97af11'
api_secret = '97eed8248a51c9feaf65e172ee9010e8'
response = requests.post('https://api.imagga.com/v1/content',
auth=(api_key, api_secret),
files={'image': open(image_path, 'rb')})
print(response.json())