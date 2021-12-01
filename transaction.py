class TransactionItem(object):
    """
    TransactionItem class
    """
    def __init__(self, item_id, item_name, item_price, item_quantity):
        self.__id = item_id
        self.__name = item_name
        self.__price = item_price
        self.__quantity = item_quantity

    def get_id(self):
        return self.__id

    def set_id(self, item_id):
        self.__id = item_id

    def get_name(self):
        return self.__name

    def set_name(self, item_name):
        self.__name = item_name

    def get_price(self):
        return self.__price

    def set_price(self, item_price):
        self.__price = item_price
    
    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, item_quantity):
        self.__quantity = item_quantity

    def calc_cost(self):
        return self.__price * self.__quantity

    def __str__(self):
        return "Item ID: {}, Item Name: {}, Item Price: {}, Item Quantity: {}".format(self.__id, self.__name, self.__price, self.__quantity)