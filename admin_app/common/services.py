import json
import requests


class UserService:
    endpoint = "http://users_backend:8000/api/"

    @staticmethod
    def get(path, **kwargs):
        headers = kwargs.get("headers", [])
        return requests.get(UserService.endpoint + path, headers=headers)

    @staticmethod
    def post(path, **kwargs):
        headers = kwargs.get("headers", [])
        data = kwargs.get("data", [])
        return requests.post(
            UserService.endpoint + path, headers=headers, data=json.dumps(data)
        )

    @staticmethod
    def put(path, **kwargs):
        headers = kwargs.get("headers", [])
        data = kwargs.get("data", [])
        print(data)
        headers = dict(headers)

        re = requests.put(
            UserService.endpoint + path, headers=headers, data=json.dumps(data)
        )
        print(re.__dict__)
        return re
