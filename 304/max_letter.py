from typing import Tuple


def max_letter_word(text: str) -> Tuple[str, str, int]:
    """
    Find the word in text with the most repeated letters. If more than one word
    has the highest number of repeated letters choose the first one. Return a
    tuple of the word, the (first) repeated letter and the count of that letter
    in the word.
    >>> max_letter_word('I have just returned from a visit...')
    ('returned', 'r', 2)
    >>> max_letter_word('$5000 !!')
    ('', '', 0)
    """
    pass