from .config import API_URL

import requests
import json


POST_STR = "post"
GET_STR = "get"


class Requests():

    def __init__(self, api_url=API_URL):
        self.base_url = api_url

    def handle_request(self, data):
        assert data["request"] in (POST_STR, GET_STR)
        if data["request"] == POST_STR:
            res = self.post_data(
                d_type=data["type"], data={data["type"]: data["data"]}
            )
        else:
            res = self.get_data(d_type=data["type"], args=data["data"])
        return res
        
    def post_data(self, d_type: str, data: dict):
        url = self.base_url + d_type + "/"
        response = requests.post(
            url = url,
            json = data,
        )
        return response
    
    def get_data(self, d_type: str, args: str = ""):
        url = self.base_url + args
        response = requests.get(
            url = url,
        )
        data = response.json()["data"].replace("\'", '\"')
        data = json.loads(data)
        return data[d_type]
