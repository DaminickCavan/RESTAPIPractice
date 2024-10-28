import requests
'''
NOTES
- Will update the contents of the resouce, not replacing the entire resource itself
- It only modifies the values set in the JSON sent with the request.

'''
class ApiExample():
    def patch_method(self):
        api_url = "https://jsonplaceholder.typicode.com/todos/10"
        response = requests.get(api_url)
        todo = {"userId": 1,
                "title": "Wash car",
                "completed": True
                }
        response = requests.put(api_url, json=todo)
        print('PUT RESPONSE', response.json())
        
        todo2 = {"title": "Mow lawn"} 
        response = requests.patch(api_url, json=todo2)
        print('PATCH RESPONSE', response.json())

api_ex = ApiExample()
api_ex.patch_method()