import collections
import sys
import operator
import csv
from termcolor import colored, cprint


def main():
    # starting dictionaries
    inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

    loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby',
        'shield', 'shield', 'shield', 'golden crown', 'golden crown']
        # I've added shield to check how it works with other stuff
    cprint("Welcome stranger in DUNGEON GAME!", 'green', 'on_red')
    option(inv, loot)


def option(inv, loot):
    """starting menu about inventory"""
    option1 = input("Choose an option(display/add/import/export/table/exit): ")
    if option1 == 'add':
        inv = add_to_inventory(inv, loot)
        # to save inventory to next operations
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
    elif option1 == "instructions":
        instructions(inv, loot)
    elif option1 == "exit":
        sys.exit()
        pass


def display_inventory(inv):
    """it showing  inventory in random way"""
    items = str(sum(inv.values()))
    # to delete unnecessery ''
    print("Inventory:")
    for key, value in inv.items():
        print('{}: {}'.format(value, key))
    print("Total number of items:", items)


def add_to_inventory(inv, loot):
    """it adding loot to current inventory"""
    inv = collections.Counter(inv)
    # collections module helps to add dictionaries value
    loot = collections.Counter(loot)
    inv = inv+loot
    return inv


def print_table(inv):
    """it showing inventory as a table in three ways"""
    order = input("Select the way how your inventory should be display: ")
    items = str(sum(inv.values()))
    # length = int(len(max(inv, key=len)))
    # something like that, but i have to figure out how to implement that to,
    # width of columns
    if order == "":
        print("Inventory:")
        print("count      item name")
        print("--------------------")
        for key, value in inv.items():
            cprint('{:>5} {:>14}'.format(value, key), 'green')
            # right justify by > insted of <
        print("--------------------")
        print("Total number of items:", items)
    elif order == "count,desc":
        # sorted with operator module in ascending values
        sorted_inv = sorted(inv.items(), key=operator.itemgetter(1))
        # reversing to get descending values
        sorted_inv.reverse()
        print("Inventory:")
        print("count      item name")
        print("--------------------")
        for key, value in sorted_inv:
            cprint('{:>5} {:>14}'.format(value, key), 'green')
        print("--------------------")
        print("Total number of items:", items)
    elif order == "count,asc":
        # as above
        sorted_inv = sorted(inv.items(), key=operator.itemgetter(1))
        print("Inventory:")
        print("count      item name")
        print("--------------------")
        for key, value in sorted_inv:
            cprint('{:>5} {:>14}'.format(value, key), 'green')
        print("--------------------")
        print("Total number of items:", items)


def import_inventory(inv):
    """it imports inventory from a file"""
    with open('import_inventory.csv', mode='r') as infile:
        reader = csv.reader(infile)
        loot2 = {row[0]: row[1] for row in reader}
        loot2 = {k: int(v) for k, v in loot2.items()}
        # because second row wasn't a value but string
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


def instructions(inv, loot):
    """it shows how to move in a dungeon game"""
    cprint("Use WSAD to move up/down/left/right in DUNGEON GAME", 'green', 'on_grey')
    cprint("Made by Maria Steimetz, Mateusz Siga and Marek Stopka", 'green', 'on_grey')
    exit = input("Press <q> to go back to menu: ")
    if exit == 'q':
        option(inv, loot)
    else:
        cprint("Are you ready to go on?", attrs=['bold'])
        instructions(inv, loot)
main()
