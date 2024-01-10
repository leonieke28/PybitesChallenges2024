from collections import namedtuple
from datetime import datetime
import json

blog = dict(
    name="PyBites",
    founders=("Julian", "Bob"),
    started=datetime(year=2016, month=12, day=19),
    tags=["Python", "Code Challenges", "Learn by Doing"],
    location="Spain/Australia",
    site="https://pybit.es",
)


# define namedtuple here


def dict2nt(dict_):
    # Creëer de namedtuple klasse en instantieer deze met de waarden van de dictionary
    NamedTuple = namedtuple("NamedTuple", dict_.keys())(*dict_.values())
    return NamedTuple


def nt2json(nt):
    nt_dict = nt._asdict()
    for key, value in nt_dict.items():
        if isinstance(value, datetime):
            nt_dict[key] = value.isoformat()

    return json.dumps(nt_dict)


Blog = namedtuple("Blog", blog.keys())(*blog.values())
json_object = nt2json(Blog)
print(json_object)
