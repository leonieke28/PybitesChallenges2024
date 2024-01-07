def is_valid_number(value, variable_name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{variable_name} moet een getal zijn")


def positive_divide(numerator, denominator):
    is_valid_number(numerator, "Numerator")
    is_valid_number(denominator, "Denominator")

    if denominator == 0:
        return 0

    resultaat = numerator / denominator

    if resultaat < 0:
        raise ValueError("Het resultaat van de deling moet positief zijn")

    return resultaat
