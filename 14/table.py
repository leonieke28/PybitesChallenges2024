import random

names = ["Julian", "Bob", "PyBites", "Dante", "Martin", "Rodolfo"]
aliases = ["Pythonista", "Nerd", "Coder"] * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = " | "


def format_row(elements):
    return SEPARATOR.join(str(element) for element in elements)


def generate_table(*sequences):
    results = []
    for elements in zip(*sequences):
        results.append(format_row(elements))
    return results
