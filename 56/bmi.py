import argparse


def calc_bmi(weight, length):
    """Provided/DONE:
    Calc BMI give a weight in kg and length in cm, return the BMI
    rounded on 2 decimals"""
    bmi = int(weight) / ((int(length) / 100) ** 2)
    return round(bmi, 2)


def create_parser():
    """TODO:
    Create an ArgumentParser adding the right arguments to pass the tests,
    returns a argparse.ArgumentParser object"""
    parser = argparse.ArgumentParser(
        prog="Calculate BMI",
        description="Calculate your BMI",
    )
    parser.add_argument("-w", "--weight", type=float, help="Your weight in kg")
    parser.add_argument("-l", "--length", type=float, help="Your length in cm")

    return parser


def handle_args(args=None):
    """Provided/DONE:
    Call calc_bmi with provided args object.
    If args are not provided get them from create_parser"""
    if args is None:
        parser = create_parser()
        args = parser.parse_args()

    if args.weight and args.length:
        bmi = calc_bmi(args.weight, args.length)
        print(f"Your BMI is: {bmi}")
    else:
        print("Need both weight and length args")


if __name__ == "__main__":
    handle_args()
