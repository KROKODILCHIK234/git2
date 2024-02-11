

class settings:
    __inn = ""
    __check = ""
    __korr_check = ""
    __bik = ""
    __name_product = ""
    __name_company = ""

    @property
    def bik(self):
        return self.__bik

    @property
    def check(self):
        return self.__check

    @property
    def korr_check(self):
        return self.__korr_check

    @property
    def inn(self):
        return self.__inn

    @property
    def name_product(self):
        return self.__name_product

    @property
    def name_company(self):
        return self.__name_company


    @bik.setter
    def bik(self, value: str):
        if not isinstance(value, str) and len(value) == 9 and value.isnumeric():
            raise Exception("Неверный аргумент!")

        self.__bik = value.strip()

    @check.setter
    def check(self, value: str):
        if not isinstance(value, str) and len(value) == 11 and value.isnumeric():
            raise Exception("Неверный аргумент!")

        self.__check = value.strip()

    @korr_check.setter
    def korr_check(self, value: str):
        if not isinstance(value, str) and len(value) == 11 and value.isnumeric():
            raise Exception("Неверный аргумент!")

        self.__korr_check = value.strip()

    @.setter
    def (self, value: str):
        if not isinstance(value, str) and len(value) == 12 and value.isnumeric():
            raise Exception("Неверный аргумент!")

        self.__inn = value.strip()

    @name_of_product.setter
    def name_product(self, value: str):
        if not isinstance(value, str):
            raise Exception("Неверный аргумент!")

        self.__name_product = value.strip()

    @name_of_company.setter
    def name_company(self, value: str):
        if not isinstance(value, str) and len(value) == 5:
            raise Exception("Неверный аргумент!")

        self.__name_company = value.strip()
        
        
