class InventoryItemInfo(object):
    def __init__(self, id, name, stock, price):
        self.__id = int(id)
        self.__name = name
        self.__stock = int(stock)
        self.__price = float(price)

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name  
    
    def get_stock(self):
        return self.__stock

    def get_price(self):
        return self.__price

    def restock(self, amount):
        if amount > 0:
            self.__stock += amount
            return True
        return False

    def purchase(self, amount):
        if amount > 0:
            if self.__stock >= amount:
                self.__stock -= amount
                return True
            return False
        return False

    def __str__(self):
        return "ID: " + str(self.__id) + ", Name: " + self.__name + ", Stock: " + str(self.__stock) + ", Price: " + str(self.__price)