class Smartphone:
    def __init__(self, manufacturer, model, price):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__price = price

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        self.__price = price

    def get_manufacturer(self):
        return self.__manufacturer

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"Manufacturer: {self.__manufacturer}, Model: {self.__model}, Price: {self.__price}"