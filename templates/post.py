import json,requests
url="stark-brook-57528.herokuapp.com/api/chat"
headers = {
    "Content-Type": "application/json"
    }
requestPayload = {
"msg":"hello"
}
resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)
print(jsonify(json.loads(resp.content)))