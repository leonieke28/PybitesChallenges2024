from typing import List


def changed_dependencies(old_reqs: str, new_reqs: str) -> List[str]:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """