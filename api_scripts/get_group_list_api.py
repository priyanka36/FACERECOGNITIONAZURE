import requests
key = "17a63c1022094fd5a94b6590381aaacc"
url_endpoint = "https://faceapinic.cognitiveservices.azure.com/face/v1.0"

JSON_HEADER = {'Content-Type': 'application/json',
               'Ocp-Apim-Subscription-Key': key}


# to get list of the groups mantained in azure database
def get_group_list():
    url = url_endpoint + '/persongroups'
    parameters = {"start": "0",
                  "top": "10",
                  "returnRecognitionModel": "true"}
    response = requests.get(url=url, params=parameters, headers=JSON_HEADER)
    print("status 200: group list obtained : ", response.status_code)
    if response.status_code == 200:
        group_list = response.json()
        list_name = [gr['name'] for gr in group_list]
        list_id = [gr['personGroupId'] for gr in group_list]
    return [list_name, list_id]

list_name,list_id = get_group_list()
print("name of groups:", list_name)
print("ids of groups:",list_id)
