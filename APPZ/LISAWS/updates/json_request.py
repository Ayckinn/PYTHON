# ==================================
# = JSON REQUEST MODULE MANAGEMENT =
# ==================================

import requests


class JSONRequest:

    def __init__(self):
        pass

    def update_json_file(self):
        self.api_link = "https://api.openweathermap.org/data/2.5/weather?q=castelnau-le-lez&lang=fr&appid=738e9d1489491771d579f8b5db5fd21a"
        self.json_data = requests.get(self.api_link).json()

        return self.json_data
