import requests
'''
NOTES
- Specify the endpoint with id of 10 to select which todo item to remove
- This will send a DELETE request toe the REST API and removes the matching resource
'''
class ApiExample():
    def del_method(self):
        api_url = "https://jsonplaceholder.typicode.com/todos/10"
        response = requests.delete(api_url)
        print('DEL RESPONSE', response.status_code)


api_ex = ApiExample()
api_ex.del_method()