import statistics


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
    returns a sequence of same length with the averages.
    You can assume all items in sequence are numeric."""
    averages = []
    for i in range(len(sequence)):
        average = round(statistics.mean(sequence[: i + 1]), 2)
        averages.append(average)

    return averages
