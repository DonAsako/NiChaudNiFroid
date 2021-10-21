import json


class Settings:
    def __init__(self):
        self.name_file = "settings.json"
        with open(self.name_file) as file:
            self.json = json.load(file)

    def create_file(self):
        with open(self.name_file, "w+") as file:
            json.dump(self.json, file)

    def get_setting(self, category_name: str, setting_name: str):
        return self.json.get(category_name).get(setting_name)

    def set_setting(self, category_name: str, setting_name: str, value):
        self.json.get(category_name)[setting_name] = value
