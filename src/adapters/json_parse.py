import numpy as np


class JSONAdapter:

    @staticmethod
    def parse_request_enc_description(json_request):
        description_raw = json_request.description
        return description_raw

    @staticmethod
    def parse_request_recommendation(json_request):
        id = json_request.id_user
        size_pool = json_request.size_pool
        return id, size_pool

    @staticmethod
    def parse_request_best_course(json_request):
        data = json_request['data']

        best_course = []
        ids = []
        for item in data:
            id = item.get("id")
            embed = item.get("embedding")
            best_course.append(embed)
            ids.append(id)

        return best_course, ids

    @staticmethod
    def parse_request_tags_description(json_request):
        description_raw = json_request.description
        tags = json_request.tags

        ans_tag = []
        for tag in tags:
            id = tag.id
            name = tag.name
            ans_tag.append((id, name))
        return description_raw, ans_tag


    @staticmethod
    def parse_request_make_test(json_request):
        return json_request.task