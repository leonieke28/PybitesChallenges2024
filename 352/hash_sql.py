def hash_query(query: str, length: int = 32) -> str:
    """Return a hash value for a given query.

    Args:
        query (str): An SQL query.
        length (int, optional): Length of the hash value. Defaults to 32.

    Raises:
        ValueError: Parameter length has to be greater equal 1.
        TypeError: Parameter length has to be of type integer.

    Returns:
        str: String representation of the hashed value.
    """
    raise NotImplementedError("Delete this line and start coding your solution!")