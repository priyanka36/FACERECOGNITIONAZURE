import requests
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion'
}
face_api_url = 'https://faceapinic.cognitiveservices.azure.com/face/v1.0/detect'
KEY = '17a63c1022094fd5a94b6590381aaacc'
OCTET_HEADER = {'Content-Type': 'application/octet-stream',
                'Ocp-Apim-Subscription-Key': KEY}
image_path = "shushant.jpg"

# Read the image into a byte array
image_data = open(image_path, "rb").read()

face_response = requests.post(
                face_api_url, params=params, headers=OCTET_HEADER, data=image_data)

print(face_response.json())