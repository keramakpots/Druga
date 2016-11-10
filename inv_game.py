import collections
import sys
import operator
import csv


def option(inv, loot):
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
        display_inventory(inv)
        option(inv, loot)
        pass
    elif option1 == "exit":
        sys.exit()
        pass

def display_inventory(inv):
    items = str(sum(inv.values()))
    print("Inventory:")
    for key, value in inv.items():
        print('{}: {}'.format(key, value))
    print("Total number of items:", items)


def add_to_inventory(inv, loot):
    inv = collections.Counter(inv)
    loot = collections.Counter(loot)
    inv = inv+loot
    return inv


#still not sorting
def print_table(inv):
    order = input("Select the way how your inventory should be display: ")
    items = str(sum(inv.values()))
    if order == "":
        print("Inventory:")
        print("count      item name")
        print("-----------------")
        for key, value in inv.items():
            print('{:>5} {:>14}'.format(value, key))
        print("-----------------")
        print("Total number of items:", items)
    elif order == "count,desc":
        sorted_inv = sorted(inv.items(), key=operator.itemgetter(1))
        sorted_inv.reverse()
        print("Inventory:")
        print("count      item name")
        print("-----------------")
        for key, value in sorted_inv:
            print('{:>5} {:>14}'.format(value, key))
        print("-----------------")
        print("Total number of items:", items)
    elif order == "count,asc":
        sorted_inv = sorted(inv.items(), key=operator.itemgetter(1))
        print("Inventory:")
        print("count      item name")
        print("-----------------")
        for key, value in sorted_inv:
            print('{:>5} {:>14}'.format(value, key))
        print("-----------------")
        print("Total number of items:", items)


def import_inventory(inv):
    with open('import_inventory.csv') as download:
        imported = csv.reader(download)
        loot2 = dict(imported)
        inv = inv.append(loot2)
        return inv

def export_inventory(inv):
    with open('export_inventory.csv', 'w', newline='') as saved:
        exported = csv.writer(saved)
        for key, value in inv.items():
            exported.writerow([key, value])


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12,
    'tomahawknr2323232323': 1443}
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby',
    'shield', 'shield', 'shield', 'golden crown', 'golden crown']
option(inv, loot)
