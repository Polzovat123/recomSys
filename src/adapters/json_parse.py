import numpy as np


class JSONAdapter:

    @staticmethod
    def parse_request_enc_description(json_request):
        description_raw = json_request.description
        return description_raw


    @staticmethod
    def parse_request_recommendation(json_request):
        id = json_request.get("id_user")
        size_pool = json_request.get("size_pool")
        return id, size_pool