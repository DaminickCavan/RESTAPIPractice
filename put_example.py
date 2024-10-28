import requests
'''
NOTES
- Will always return a 200 instead of 201, because you're not creating a new resource but updating an existing one
- Notice 10 at the end of the URL. This tells the API which todo to update
- Any data sent with a put request will completely replace the existing values of the todo
'''
class ApiExample():
    def put_method(self):
        api_url = "https://jsonplaceholder.typicode.com/todos/10"
        response = requests.get(api_url)
        print('GET RESPONSE', response.json())
        todo = {"userId": 1,
                "title": "Wash car",
                "completed": True
                }
        response = requests.put(api_url, json=todo)
        print('PUT RESPONSE', response.json())
        print('PUT RESPONSE STATUS CODE', response.status_code)

api_ex = ApiExample()
api_ex.put_method()

