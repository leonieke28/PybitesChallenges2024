import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = "https://bites-data.s3.us-east-2.amazonaws.com/"
TMP = os.getenv("TMP", "/tmp")

fname = "movie_metadata.csv"
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    directors = defaultdict(list)
    with open(MOVIE_DATA, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                director = row["director_name"]
                movie = row["movie_title"].strip()
                year = int(row["title_year"])
                score = float(row["imdb_score"])
            except ValueError:
                continue

            if year < MIN_YEAR:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
    round the mean to 1 decimal place"""
    scores = [m.score for m in movies]
    return round(sum(scores) / len(scores), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
    return a list of tuples (director, average_score) ordered by highest
    score in descending order.
    Only take directors into account with >= MIN_MOVIES"""
    averages = []
    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            avg = calc_mean_score(movies)
            averages.append((director, avg))

    averages.sort(key=lambda x: x[1], reverse=True)
    return averages
