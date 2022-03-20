class MyBank(type):

    def __new__(mcs, name, bases, attrs):
        new_attrs = {}
        lst = ["BANK_LOGIN", "BANK_PASSWORD"]
        for attrs_name in attrs.keys():
            new_name = attrs_name if attrs_name not in lst else "_MyBank__" + attrs_name
            new_attrs[new_name] = attrs[attrs_name]
        return super().__new__(mcs, name, bases, new_attrs)

    @property
    def BANK_LOGIN(cls):
        return cls.__BANK_LOGIN

    @BANK_LOGIN.setter
    def BANK_LOGIN(cls, login):
        cls.__BANK_LOGIN = login

    @property
    def BANK_PASSWORD(cls):
        return cls.__BANK_PASSWORD

    @BANK_PASSWORD.setter
    def BANK_PASSWORD(cls, password):
        cls.__BANK_PASSWORD = password


class BBank(metaclass=MyBank):
    __money = 0
    BANK_LOGIN = "BelarusBank"
    BANK_PASSWORD = "qwert12345"

    def __init__(self, name, surname, age, user_name, password):
        if BBank.BANK_LOGIN == input("Введите логин: ") and BBank.BANK_PASSWORD == input("Введите пароль: "):
            self.name = name
            self.surname = surname
            self.age = age
            self.user_name = user_name
            self.password = password
        else:
            print("У Вас не полномочий открывать счет")


class BPSBank(metaclass=MyBank):
    __money = 0
    BANK_LOGIN = "BPSB"
    BANK_PASSWORD = "BPSqwert12345"

    def __init__(self, name, surname, age, user_name, password):
        if BPSBank.BANK_LOGIN == input("Введите логин: ") and BPSBank.BANK_PASSWORD == input("Введите пароль: "):
            self.name = name
            self.surname = surname
            self.age = age
            self.user_name = user_name
            self.password = password
        else:
            print("У Вас не полномочий открывать счет")
