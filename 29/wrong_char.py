def get_index_different_char(chars):
    unique_count = 1
    alphanumeric_count = sum(1 for char in chars if str(char).isalnum())
    non_alphanumeric_count = sum(1 for char in chars if not str(char).isalnum())
    alphanumeric_index = next(
        (i for i, char in enumerate(chars) if str(char).isalnum()), None
    )
    non_alphanumeric_index = next(
        (i for i, char in enumerate(chars) if not str(char).isalnum()), None
    )
    return (
        alphanumeric_index
        if alphanumeric_count == unique_count
        else non_alphanumeric_index
    )
