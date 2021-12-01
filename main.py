from transaction import *
from inventory import *
import os


def create_inventory():
    os.chdir('MIS_304/finalProject/MIS304_final_project')
    print(os.getcwd())
    file = open("Inventory.txt", "r")
    inven = file.readlines()
    inven = [x.strip() for x in inven]
    l = []
    counter = 0
    while counter < len(inven):
        j = []
        for i in range(4):
            j.append(inven[counter])
            counter += 1
        l.append(j)
    file.close() 
    inventory = []
    for i in l:
        p = InventoryItemInfo(i[0], i[1], i[2], i[3])
        inventory.append(p)
    return inventory
    
def menu(inventory):
    print("{:<5}{:<30}{:<10}{}".format("ID", "Item", "Price", "Qty Available"))
    for i in inventory:
        print("{:<5}{:<30}{:<10}{}".format(i.get_id(), i.get_name(), i.get_price(), i.get_stock()))
    print("Enter 0 when finished.\n")

def checkExistence(inventory, item_id):
    for i in inventory:
        if i.get_id() == item_id:
            return True
    return False

def retrieveItem(inventory, item_id):
    for i in range(len(inventory)):
        if inventory[i].get_id() == item_id:
            return i
    return None

def purchase(inventory):
    purchase_flag = True
    transactions = []
    while purchase_flag:
        try:
            menu(inventory)
            itemID = int(input("Enter the ID of the item you would like to purchase/return: "))
            if itemID == 0:
                purchase_flag = False
            elif checkExistence(inventory, itemID):
                index = retrieveItem(inventory, itemID)
                item = inventory[index]
                quantity = int(input("Enter the quantity (negative for return): "))
                if quantity > 0:
                    if not item.purchase(quantity):
                        print("Sorry we don't have enough stock")
                    else:
                        item.purchase(quantity)
                        name = inventory[itemID].get_name()
                        price = inventory[itemID].get_price()
                        transItem = TransactionItem(itemID, name, price, 0)
                        transItem.set_quantity(transItem.get_quantity() + quantity)
                        transactions.append(transItem) 
                else:
                    inventory[index].restock(abs(quantity))
            else:
                print("Input was invalid.")
        except ValueError:
            print("Input was invalid.")
    return transactions
        
def invoice(transactions):
    print("{:<5}{:<30}{:<10}{}".format("ID", "Item", "Price", "Total"))
    for i in transactions:
        print("{:<5}{:<30}{:<10}{}".format(i.get_id(), i.get_name(), i.get_price(), i.get_quantity() * i.get_price()))
    total = sum([i.get_price() for i in transactions])
    tax = total * 0.0825
    print("Price: ${:.2f}".format(total))
    print("Tax: ${:.2f}".format(tax))
    print("Total: ${:.2f}".format(total + tax))

def main():
    inventory = create_inventory()
    menu(inventory)
    purchases = purchase(inventory)
    invoice(purchases)
    

if __name__ == '__main__':
    main()