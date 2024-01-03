import os
import re
import urllib.request
from collections import Counter

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, "feed")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/feed", tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


def extract_tags(content):
    pattern = r"<category>(.*?)</category>"
    matches = re.findall(pattern, content)
    return matches


blog_tags = extract_tags(content)


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
    data already loaded into the content variable"""
    counter = Counter(blog_tags)
    return counter.most_common(n)
