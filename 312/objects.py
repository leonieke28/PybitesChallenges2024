from typing import Dict, List

scores = {
    "builtin": 1,
    "keyword": 2,
    "module": 3,
}


def score_objects(objects: List[str],
                  scores: Dict[str, int] = scores) -> int:
    pass