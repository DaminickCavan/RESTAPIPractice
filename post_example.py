import requests
import json
'''
NOTES
- when setting key argument json, it actuomaticcaly sets the request HTTP header content-type to application/json
- If key argument is not set, then you need to set the content-type and serialize the JSON manually.
- The drawback of manually seting is more lines of code but you get more control over the request
'''
class ApiExample():

    def post_with_keyarg(self):  # using key argument of json=
        api_url = "https://jsonplaceholder.typicode.com/todos"
        todo = {
            "userId": 1,
            "title": "Buy milk",
            "completed": False
        }
        response = requests.post(api_url, json=todo)  # when setting key argument json, it actuomaticcaly sets the request HTTP header content-type to application/json
        print('RESPONSE', response.json())
        print('STATUS', response.status_code)


    def post_manually_set_json_headers(self):  # manually setting headers and json
        api_url = "https://jsonplaceholder.typicode.com/todos"
        todo = {
            "userId": 1,
            "title": "Buy milk",
            "completed": False
        }
        headers =  {"Content-Type":"application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        print('RESPONSE', response.json())
        print('STATUS', response.status_code)

post_ex = ApiExample()

# post_ex.post_with_keyarg()
post_ex.post_manually_set_json_headers()