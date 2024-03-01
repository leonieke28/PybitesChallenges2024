INDENTS = 4


def print_hanging_indents(poem):
    lines = poem.splitlines()

    first_line = True

    for line in lines:
        if line == "":
            first_line = True
        elif first_line:
            print(line.strip())
            first_line = False
        else:
            print(INDENTS * " " + line.strip())
