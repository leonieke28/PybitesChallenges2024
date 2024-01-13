from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    start_date = PYBITES_BORN + timedelta(days=100)

    while True:
        yield start_date
        start_date += timedelta(days=100)
