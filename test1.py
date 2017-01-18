checking
    largest
    cells
    title_list = ["inx", "Class", "__str__", "Perimeter", "Formula", "Area", "Formula"]
    cell_size = list()

    for i, title in enumerate(title_list):
        cell_size.append(len(title))

    for items in self.shapes:
        for i, item in enumerate(vars(items)):
            try:
                if cell_size[i] < len(str(item)):
                    cell_size[i] = len(str(item))
            except:
                cell_size.append(len(item))

    # how big table
    table_size = 1
    for dash in cell_size:
        table_size += (dash + 3)

    # printing table
    print('-' * table_size)

    for i, title in enumerate(title_list):
        if i == 0:
            print('|', end="")
        print(' {:{width}} |'.format(title, width=cell_size[i]), end="")

    print('\n' + '-' * table_size)

    for i, shape in enumerate(self.shapes):
        if i == 0:
            print('|', end="")
        print(
            '{!s:{width}}| {!s:{width}} | {!s:{width}} | {!s:{width}} | {!s:{width}} | {!s:{width}} | {!s:{width}} |\n'.format(
                i, str(shape).split(",")[0], shape, "{0:.2f}".format(shape.get_perimeter()),
                shape.get_perimeter_formula(str(type(shape))), "{0:.2f}".format(shape.get_area()),
                shape.get_area_formula(str(type(shape))), width=cell_size[i]), end="")
    print()

    print('-' * table_size)
    return "Table")