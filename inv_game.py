import collections
import sys
import operator
import csv


def option(inv, loot):
    """starting menu about inventory"""
    option1 = input("Choose an option: ")
    if option1 == 'add':
        inv = add_to_inventory(inv, loot)
        option(inv, loot)
        pass
    elif option1 == 'display':
        display_inventory(inv)
        option(inv, loot)
        pass
    elif option1 == 'export':
        export_inventory(inv)
        option(inv, loot)
        pass
    elif option1 == 'table':
        print_table(inv)
        option(inv, loot)
        pass
    elif option1 == 'import':
        inv = import_inventory(inv)
        option(inv, loot)
        pass
    elif option1 == "exit":
        sys.exit()
        pass

def display_inventory(inv):
    """it showing  inventory in random way"""
    items = str(sum(inv.values()))
    print("Inventory:")
    for key, value in inv.items():
        print('{}: {}'.format(key, value))
    print("Total number of items:", items)


def add_to_inventory(inv, loot):
    """it adding loot to current inventory"""
    inv = collections.Counter(inv)
    #collections module helps to add dictionaries value
    loot = collections.Counter(loot)
    inv = inv+loot
    return inv



def print_table(inv):
    """it showing inventory as a table in three ways"""
    order = input("Select the way how your inventory should be display: ")
    items = str(sum(inv.values()))
    length = int(len(max(inv, key = len)))
    #something like that, but i have to figure out how to implement that to,
    #width of columns
    if order == "":
        print("Inventory:")
        print("count      item name")
        print("--------------------")
        for key, value in inv.items():
            print('{:>5} {:>14}'.format(value, key))
        print("--------------------")
        print("Total number of items:", items)
    elif order == "count,desc":
        #sorted with operator module in ascending values
        sorted_inv = sorted(inv.items(), key=operator.itemgetter(1))
        #reversing to get descending values
        sorted_inv.reverse()
        print("Inventory:")
        print("count      item name")
        print("--------------------")
        for key, value in sorted_inv:
            print('{:>5} {:>14}'.format(value, key))
        print("--------------------")
        print("Total number of items:", items)
    elif order == "count,asc":
        #as above
        sorted_inv = sorted(inv.items(), key=operator.itemgetter(1))
        print("Inventory:")
        print("count      item name")
        print("--------------------")
        for key, value in sorted_inv:
            print('{:>5} {:>14}'.format(value, key))
        print("--------------------")
        print("Total number of items:", items)


def import_inventory(inv):
    """it imports inventory from a file"""
    with open('import_inventory.csv', mode='r') as infile:
        reader = csv.reader(infile)
        loot2 = {row[0]:row[1] for row in reader}
        loot2 = {k:int(v) for k,v in loot2.items()}
        #because second row wasn't a value but string
        loot2 = collections.Counter(loot2)
        inv = collections.Counter(inv)
        inv = inv+loot2
        return inv



def export_inventory(inv):
    """it send current inventory to the csv file"""
    with open('export_inventory.csv', 'w', newline='') as saved:
        exported = csv.writer(saved)
        for key, value in inv.items():
            exported.writerow([key, value])

#starting dictionaries
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby',
    'shield', 'shield', 'shield', 'golden crown', 'golden crown']
    #i've added shield to check how it works with other stuff
option(inv, loot)
