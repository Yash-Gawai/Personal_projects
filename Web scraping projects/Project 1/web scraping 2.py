from bs4 import BeautifulSoup
import requests

price_selector = ".price_color"
title_selector = ".product_pod h3 a"
rating_selector = ".star-rating"

rating_mapping = {
    "One" : "1/5",
    "Two" : "2/5",
    "Three" : "3/5",
    "Four" : "4/5",
    "Five" : "5/5"
}

def get_rating(tag): # Converting the rating to a readable/writable format
    for term,rating in rating_mapping.items():
        if term in tag["class"]:
            return rating

data = requests.get("https://books.toscrape.com/catalogue/page-1.html").content

soup = BeautifulSoup(data, "html.parser") # Load the html document. Parser tells what type of doc it is

prices = soup.select(price_selector) # Select data from the specific html tags
titles = soup.select(title_selector)
ratings = soup.select(rating_selector)

with open("books.csv","w",encoding="utf-8") as book_file:
    for price,title,rating in zip(prices,titles,ratings):
        book_file.write(f"{title['title']},{price.string},{get_rating(rating)}\n")