import re


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
    2014-07-03T23:30:37"""
    pattern = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")
    return bool(pattern.search(text))


def is_integer(number):
    """Return True if number is an integer"""
    return isinstance(number, int)


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    return bool(re.search(r"\b\w+-\w+\b", text))


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
    'Good morning (afternoon)' -> 'Good morning' (so don't forget
    leading spaces)"""
    pattern = r"\s?\([^)]*\)"
    return re.sub(pattern, "", text)


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
    ['hi', 'how are you doing', 'blabla']
    (make sure you strip trailing spaces)"""
    split_strings = re.split("[?!.,;]+", text)
    return [s.strip() for s in split_strings if s.strip() != ""]


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    return re.sub(r"\s+", " ", text)


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    pattern = re.compile(r"[aeiou]{3}")
    return bool(pattern.search(word))


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
    (AMER date format)"""
    pattern = re.compile(r"(\d{2})/(\d{2})/(\d{4})")
    return re.sub(pattern, r"\2/\1/\3", date)
