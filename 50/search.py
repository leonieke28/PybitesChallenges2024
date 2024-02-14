from collections import namedtuple
from datetime import date

import feedparser

FEED = "https://bites-data.s3.us-east-2.amazonaws.com/all.rss.xml"

Entry = namedtuple("Entry", "date title link tags")


def _convert_struct_time_to_dt(stime):
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)
    """
    return date(stime.tm_year, stime.tm_mon, stime.tm_mday)


def get_feed_entries(feed=FEED):
    """Use feedparser to parse PyBites RSS feed.
    Return a list of Entry namedtuples (date = date, drop time part)
    """
    parsed_feed = feedparser.parse(feed)
    entries = []
    for entry in parsed_feed.entries:
        date = _convert_struct_time_to_dt(entry.published_parsed)
        title = entry.title
        link = entry.link
        tags = {
            tag.term.lower() for tag in entry.tags
        }  # Verander alle tags naar kleine letters
        entries.append(Entry(date, title, link, tags))
    return entries


def filter_entries_by_tag(search, entry):
    """Check if search matches any tags as stored in the Entry namedtuple
    (case insensitive, only whole, not partial string matches).
    Returns bool: True if match, False if not.
    Supported searches:
    1. If & in search do AND match,
       e.g. flask&api should match entries with both tags
    2. Elif | in search do an OR match,
       e.g. flask|django should match entries with either tag
    3. Else: match if search is in tags
    """
    search_terms = [
        term.lower() for term in search.split("&" if "&" in search else "|")
    ]
    if "&" in search:
        return all(term in entry.tags for term in search_terms)
    elif "|" in search:
        return any(term in entry.tags for term in search_terms)
    else:
        return search.lower() in entry.tags


def main():
    """Entry point to the program
    1. Call get_feed_entries and store them in entries
    2. Initiate an infinite loop
    3. Ask user for a search term:
       - if enter was hit (empty string), print 'Please provide a search term'
       - if 'q' was entered, print 'Bye' and exit/break the infinite loop
    4. Filter/match the entries (see filter_entries_by_tag docstring)
    5. Print the title of each match ordered by date ascending
    6. Secondly, print the number of matches: 'n entries matched'
       (use entry if only 1 match)
    """
    entries = get_feed_entries()
    while True:
        search = input("Search for (q for exit): ")
        if not search:
            print("Please provide a search term")
            continue
        if search.lower() == "q":
            print("Bye")
            break
        matches = [entry for entry in entries if filter_entries_by_tag(search, entry)]
        for match in sorted(matches, key=lambda x: x.date):
            print(f"{match.date} | {match.title} | {match.link}")
        print(
            f'\n{len(matches)} {"entry" if len(matches) == 1 else "entries"} matched "{search}"\n'
        )


if __name__ == "__main__":
    main()
