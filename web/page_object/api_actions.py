import json

import jsonpath as jsonpath
import requests

updateUrl = "https://reqres.in/api/users/2"


class ApiActions:
    def get_request(self, url):
        """Send GET request"""
        respone = requests.get(url)
        if respone.status_code == 200:
            json_response = json.loads(respone.text)
            print(json_response)

            pages = jsonpath.jsonpath(json_response, "total_pages")
            # assert pages[0] == 2

        else:
            return None

    def post_request(self, url):
        login = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        post = requests.post(url, login)
        if post.status_code == 200:
            print(post)
        json_response = json.loads(post.text)
        print(json_response)

        # token = jsonpath.jsonpath(json_response, "token")
        # print(token)
        #
        # if token[0] != 'QpwL5tke4Pnpja7X4':
        #     return None
        # else:
        #     return 1

    def update_request(self, url):
        updateDict = {
            "name": "Dor",
            "job": "zion resident",
            "number": 1
        }

        update = requests.put(updateUrl, updateDict)
        assert update.status_code == 200

        json_response = json.loads(update.text)
        print(json_response)

        name = jsonpath.jsonpath(json_response, "name")
        print(name[0])
        print(updateDict['name'])

        assert name[0] == updateDict['name']

    def delete_request(self, url):

        delete = requests.delete("https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg")
        print(delete)
        # assert delete.status_code == 204

        # json_response = json.loads(delete.text)
        # print(json_response)
