from .config import API_URL

import os
import requests
import json


POST_STR = "post"
GET_STR = "get"


class Requests():

    def __init__(self):
        self.base_url = API_URL

    def handle_request(self, data):
        if data["request"] == POST_STR:
            res = self.post_data(
                d_type=data["type"], data={data["type"]: data["data"]}
            )
        elif data["request"] == GET_STR:
            res = self.get_data(d_type=data["type"], args=data["data"])
        else:
            res = "404"
        return str(res)
        
    def post_data(self, d_type: str, data: dict):
        url = self.base_url + d_type + "/"
        response = requests.post(
            url = url,
            json = data,
        )
        if response.status_code != 200:
            return "400"
        return response
    
    def get_data(self, d_type: str, args: str = ""):
        if len(d_type) == 0:
            return "400"
        url = self.base_url + args
        response = requests.get(
            url = url,
        )
        if response.status_code != 200:
            return "400"
        data = response.json()["data"].replace("\'", '\"')
        data = json.loads(data)
        return data[d_type]
