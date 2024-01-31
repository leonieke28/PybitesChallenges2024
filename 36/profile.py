def get_profile(name, age, *sports, **awards):
    if not isinstance(age, int):
        raise ValueError("Age must be an integer.")
    if len(sports) > 5:
        raise ValueError("You can't play more than 5 sports.")

    result = {"name": name, "age": age}

    if sports:
        result["sports"] = sorted(sports)

    if awards:
        result["awards"] = awards

    return result
