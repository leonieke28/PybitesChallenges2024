import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = []
    for file in files:
        with open(file, "r") as f:
            movie_data = json.loads(f.read())
            movies.append(movie_data)
    return movies


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if "Comedy" in movie["Genre"]:
            return movie["Title"]


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    most_nominations = 0
    most_nominated_movie = ""
    for movie in movies:
        nominations = int(movie["Awards"].split(" ")[-2])
        if nominations > most_nominations:
            most_nominations = nominations
            most_nominated_movie = movie["Title"]
    return most_nominated_movie


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    longest_runtime = 0
    longest_movie = ""
    for movie in movies:
        runtime = int(movie["Runtime"].split(" ")[0])
        if runtime > longest_runtime:
            longest_runtime = runtime
            longest_movie = movie["Title"]
    return longest_movie
