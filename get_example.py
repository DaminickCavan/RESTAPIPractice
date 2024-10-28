import requests

class ApiExample():

    def get_place_holder(self):
        api_url = "https://jsonplaceholder.typicode.com/todos/1"
        response = requests.get(api_url)
        print('RESPONSE', response.json())  # show entire response
        print('STATUS', response.status_code)  # get only status code from response
        print('CONTENT-TYPE', response.headers["Content-Type"]) # get only content type from response

get_ex = ApiExample()
get_ex.get_place_holder()
