import os
import re
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = "safari.logs"
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = "🐍", "."

urllib.request.urlretrieve(
    f"https://bites-data.s3.us-east-2.amazonaws.com/{DATA}", SAFARI_LOGS
)


def create_chart():
    with open(SAFARI_LOGS) as f:
        logs = f.readlines()

    books_by_date = {
        date: ""
        for date in set(re.search(r"\d{2}-\d{2}", line).group() for line in logs)
    }

    for i, line in enumerate(logs):
        if "sending to slack channel" in line:
            date = re.search(r"\d{2}-\d{2}", line).group()
            if "Python" in logs[i - 1]:
                books_by_date[date] += PY_BOOK
            else:
                books_by_date[date] += OTHER_BOOK

    for date in sorted(books_by_date.keys()):
        print(date, books_by_date[date])


create_chart()
