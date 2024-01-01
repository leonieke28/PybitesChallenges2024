def sum_numbers(numbers=None):
    if numbers is None:
        return sum(range(1, 101))
    else:
        return sum(numbers)
