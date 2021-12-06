class TransactionItem(object):
    """
    TransactionItem class
    """
    def __init__(self, item_id, item_name, item_price, item_quantity):
        self.__id = int(item_id)
        self.__name = item_name
        self.__price = float(item_price)
        self.__quantity = int(item_quantity)

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price
    
    def get_qty(self):
        return self.__quantity

    def set_qty(self, new_qty):
        self.__quantity = new_qty

    def calc_cost(self):
        return self.__price * self.__quantity

    def __str__(self):
        return "Item ID: {}, Item Name: {}, Item Price: {}, Item Quantity: {}".format(self.__id, self.__name, self.__price, self.__quantity)