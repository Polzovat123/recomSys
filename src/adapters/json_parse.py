import numpy as np


class JSONAdapter:

    @staticmethod
    def parse_request_enc_description(json_request):
        description_raw = json_request.get("Description") if json_request.get("Description") is not None else np.nan
        return description_raw