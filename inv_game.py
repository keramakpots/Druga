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
        import_inventory(inv)
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
    if order == "":
        print("Inventory:")
        print("count      item name")
        print("--------------------")
        for key, value in inv.items():
            print('{:>5} {:>14}'.format(value, key))
        print("--------------------")
        print("Total number of items:", items)
    elif order == "count,desc":
        sorted_inv = sorted(inv.items(), key=operator.itemgetter(1))
        sorted_inv.reverse()
        print("Inventory:")
        print("count      item name")
        print("--------------------")
        for key, value in sorted_inv:
            print('{:>5} {:>14}'.format(value, key))
        print("--------------------")
        print("Total number of items:", items)
    elif order == "count,asc":
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
     #not adding as in add function
    with open('import_inventory.csv') as download:
        imported = csv.reader(download)
        loot2 = dict(imported)
        loot2 = loot2.items()
        inv = collections.Counter(inv)
        loot2 = collections.Counter(loot2)
        #almost -
        inv = inv+loot2
        #import as a single item - i need multiple
        return inv#so i have to divide imported items

def export_inventory(inv):
    """it send current inventory to the csv file"""
    with open('export_inventory.csv', 'w', newline='') as saved:
        exported = csv.writer(saved)
        for key, value in inv.items():
            exported.writerow([key, value])


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby',
    'shield', 'shield', 'shield', 'golden crown', 'golden crown']
    #i've added shield to check how it works with other stuff
option(inv, loot)
