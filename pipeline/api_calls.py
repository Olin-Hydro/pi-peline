from .config import API_URL, API_TOKEN

import os
import requests


class Requests():

    def __init__(self):
        self.base_url = API_URL
        self.api_token = API_TOKEN
        self.headers = self.create_headers()

    def create_headers(self):
        return {"api_token": self.api_token}
        
    def post_data(self, d_type: str, data: dict):
        url = self.base_url + d_type + "/"
        response = requests.post(
            url = url,
            json = data,
            #headers = self.headers
        )
        return response
    
    def get_data(self, d_type: str, args: str = ""):
        url = self.base_url + d_type + "/" + args
        response = requests.get(
            url = url,
            #headers = self.headers
        )
        return response
