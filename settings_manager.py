import os
import json
import uuid
from settings import settings

class settings_maneger(object):
    __file_name = "settings.json"
    __unique_number = 1
    __data = {}
    __settings = settings()
    
    __keys = ['inn', 'check', 'korr_check', 'bik', 'name_product', 'name_company']

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_maneger, cls).__new__(cls)
        return cls.instance


    def __init__(self) -> None:
        self.__unique_number = uuid.uuid4()

    @property
    def unique_number(self) -> str:
        return str(self.__unique_number.hex)

    def opener(self, file_name: str) -> bool:
        if not isinstance(file_name, str):
            raise Exception("Неверный аргумент!")

        if file_name == "":
            raise Exception("Неверный аргумент!")

        self.__file_name = file_name.strip()

        try:
            self.__open()
        except:
            return False

        return True

    @property
    def data(self) -> {}:
        return self.__data

    def convert(self):
        if len(self.__data) == 0:
            raise Exception("проблема при создании экземпляра класса settings")
        fields = self.__settings.get_data_keys
        if len(self.__data) < len(fields):
            raise Exception("Входных данных мало, есть пустые поля")
        for field in fields:
            value = self.__data[field]
            setattr(self.__settings, field, value)

    @property
    def __open(self):
        file_path = os.path.split(__file__)
        settings_file = "%s/%s" % (file_path[0], self.__file_name)
        if not os.path.exists(settings_file):
            raise Exception(
                "Неверный аргумент",
                settings_file)

        with open(settings_file, "r") as read_file:
            self.__data = json.load(read_file)
