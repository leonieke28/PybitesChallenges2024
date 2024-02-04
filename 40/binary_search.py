def binary_search(sequence, target):
    if not sequence:
        return None
    mid = len(sequence) // 2
    if sequence[mid] == target:
        return mid
    elif sequence[mid] > target:
        return binary_search(sequence[:mid], target)
    else:
        result = binary_search(sequence[mid + 1 :], target)
        if result is not None:
            return mid + 1 + result
