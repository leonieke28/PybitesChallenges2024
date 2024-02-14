from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = "https://bites-data.s3.us-east-2.amazonaws.com/packt.html"
CONTENT = requests.get(PACKT).text

Book = namedtuple("Book", "title description image link")


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, "html.parser")
    title = soup.select_one(".dotd-title").text.strip()
    description = (
        soup.find("div", class_="dotd-main-book-summary")
        .find_all("div")[2]
        .get_text(strip=True)
    )
    image = soup.select_one(".dotd-main-book-image img")["src"]
    link = soup.select_one(".dotd-main-book-image a")["href"]
    return Book(title, description, image, link)
