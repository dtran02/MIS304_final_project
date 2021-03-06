from transaction import *
from inventory import *
import os

def process_inventory():
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
    
def print_inventory(inventory):
    print("{:<5}{:<30}{:<10}{}".format("ID", "Item", "Price", "Qty Available"))
    for i in inventory:
        print("{:<5}{:<30}{:<10}{}".format(i.get_id(), i.get_name(), i.get_price(), i.get_stock()))
    print("Enter 0 when finished.\n")

def get_item_id(inventory):
    itemID = input("Enter the ID of the item you would like to purchase/return: ")
    try:
        itemID = int(itemID)
    except Exception as err:
        return None
    if itemID == 0:
        return 0
    elif retrieveItem(inventory, itemID):
        return retrieveItem(inventory, itemID).get_id()
    else:
        return None

def retrieveItem(inventory, item_id):
    for i in range(len(inventory)):
        if inventory[i].get_id() == item_id:
            return inventory[i]
    return False

def write_updated_inventory(inventory):
    file = open("UpdatedInventory.txt", "w")
    for i in inventory:
        file.write(str(i.get_id()) + "\n")
        file.write(str(i.get_name()) + "\n")
        file.write(str(i.get_stock()) + "\n")
        file.write(str(i.get_price()) + "\n")
    file.close()


def purchase(inventory):
    purchase_flag = True
    transactions = []
    while purchase_flag:
        print_inventory(inventory)
        itemID = get_item_id(inventory)
        if itemID == 0:
            purchase_flag = False
        elif itemID != None:
            item = retrieveItem(inventory, itemID)
            quantity = int(input("Enter the quantity (negative for return): "))
            if quantity < 0:
                name = item.get_name()
                price = item.get_price()
                transItem = TransactionItem(itemID, name, price, 0)
                transItem.set_qty(transItem.get_qty() + quantity)
                transactions.append(transItem) 
                item.restock(abs(quantity))
            elif not item.purchase(quantity):
                print("Sorry we don't have enough stock")
            elif quantity > 0:
                name = item.get_name()
                price = item.get_price()
                transItem = TransactionItem(itemID, name, price, 0)
                transItem.set_qty(transItem.get_qty() + quantity)
                transactions.append(transItem) 
        else:
            print("Input was invalid.")
    write_updated_inventory(inventory)
    return transactions
        
def print_invoice(transactions):
    if len(transactions) == 0:
        print("Thank you for your visit!")
    else:
        print("{:<5}{:<30}{:<10}{:<10}{}".format("ID", "Item", "Quantity", "Price", "Total"))
        for i in transactions:
            print("{:<5}{:<30}{:<10}{:<10}{:.2f}".format(i.get_id(), i.get_name(), i.get_qty(), i.get_price(), i.calc_cost()))
        total = sum([i.calc_cost() for i in transactions])
        tax = total * 0.085
        print("Price: ${:.2f}".format(total))
        print("Tax: ${:.2f}".format(tax))
        print("Total: ${:.2f}".format(total + tax))

def main():
    inventory = process_inventory()
    purchases = purchase(inventory)
    print_invoice(purchases)
    

if __name__ == '__main__':
    main()