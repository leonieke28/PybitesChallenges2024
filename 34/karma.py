from collections import namedtuple
from datetime import datetime

Transaction = namedtuple(
    'Transaction',
    'giver points date',
    defaults=(None, None, datetime.now()))


class User:
    pass