import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set("PassWord@1 PyBit$s9".split())


def validate_password(password):
    if not 6 <= len(password) <= 12:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if sum(char.islower() for char in password) < 2:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in PUNCTUATION_CHARS for char in password):
        return False
    if password in used_passwords:
        return False
    else:
        used_passwords.add(password)
    return True
