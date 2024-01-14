import os
import re
import urllib.request
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, "stopwords")
harry_text = os.path.join(tmp, "harry")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt", stopwords_file
)
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/harry.txt", harry_text
)

with open(stopwords_file, "r") as f:
    stopwords = f.read().split()


def get_harry_most_common_word():
    with open(harry_text, "r", encoding="utf-8") as f:
        text = f.read()

    clean_text = re.sub("[^A-Za-z \\n]+", "", text)
    lowercase_text = clean_text.lower()
    words = lowercase_text.split()
    filtered_words = [word for word in words if word not in stopwords]

    word_counts = Counter(filtered_words)
    most_common_word = word_counts.most_common(1)[0]
    return most_common_word
