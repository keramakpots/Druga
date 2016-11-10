import collections
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
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

def print_table(inv, order)
    



inv = add_to_inventory(inv, loot)

display_inventory(inv)

print_table(inv, order)
