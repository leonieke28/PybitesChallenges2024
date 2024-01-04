# fmt: off
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


# fmt: on


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
    each name appears only once"""
    return list(set(name.title() for name in names))


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    sorted_surname_desc = sorted(names, key=lambda x: x.split()[1], reverse=True)
    return sorted_surname_desc


def shortest_first_name(names):
    """Returns the shortest first name (str).
    You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    first_name = min(names, key=lambda x: len(x.split()[0]))
    return first_name.split()[0]
