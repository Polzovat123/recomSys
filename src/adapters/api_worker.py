import json

import requests


class RequestAdapter:

    @staticmethod
    def get_best_course(user_id, get=10):
        response = requests.get("http://26.191.10.163:3002/api/ml/embeddings", params={'id': user_id})
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise "empty response"

    @staticmethod
    def get_course():
        response = requests.get("http://26.191.10.163:3002/api/ml/courses", headers={'Accept': 'application/json'})
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise "empty response"