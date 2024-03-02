from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple("Game", "title link")


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    feed = feedparser.parse(FEED_URL)

    games = []
    for game in feed["items"]:
        title = game["title"]
        link = game["link"]
        games.append(Game(title, link))

    return games
