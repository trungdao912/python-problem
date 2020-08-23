import time
import json

modify_data = {
    "expiration_time": 200,
    "product": "qchat",
    "utm_campaign": str(time.time()),
    "storefront": {
        "banner_enabled": False,
        "purchase_options": [
            {
                "button_text": "Dynamic offer 1 - button_text",
                "description": "Dynamic offer 1 - description",
                "id": "",
                "price": "99.99",
                "price_text": "price_text",
                "session_count": "0",
                "subtitle": "Dynamic offer - subtitle",
                "title": "Dynamic offer - title",
                "suffix": "Dynamic offer - suffix",
                "trial_duration": 0,
                "min_member_count": 1,
                "max_member_count": 1,
                "action": "purchase",
                "frequency_view": "monthly",
                "free_learning_subscription": False,
                "team_type": "personal",
                "frequency": None,
            }
        ]
    }
}


class StorefrontConfig:
    def __init__(self, data: object):
        self.data = data

    def helper(self, modify_data: dict, data: dict):
        for k, v in modify_data.items():
            if isinstance(v, dict):
                self.helper(v, data[k])
                continue
            if isinstance(v, list):
                for index, item in enumerate(v):
                    if isinstance(item, dict):
                        self.helper(item, data[k][index])
                        continue

                    if isinstance(item, str):
                        item = data[k][index]
                        continue
                continue
            if isinstance(v, str) or isinstance(v, int):
                data[k] = v

    def update(self, modify_data: dict):
        self.helper(modify_data, self.data)
        return self.data

class FileController:
    @staticmethod
    def read_file(file_name: str):
        with open(file_name) as json_file:
            data = json.load(json_file)
            return StorefrontConfig(data)


config = FileController.read_file('data.json')
print(config.update(modify_data))
