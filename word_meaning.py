import requests
from datetime import datetime
from bs4 import BeautifulSoup


def show_origin(soup):
    try:
        origin = soup.find('span', {'unbox': 'wordorigin'})
        print('\nOrigin -> ', origin.text)
    except AttributeError:
        pass


def show_definitions(soup):
    print()
    senseList = []
    senses = soup.find_all('li', class_='sense')
    for s in senses:
        definition = s.find('span', class_='def').text
        print("-", definition)

        # Examples
        examples = s.find_all('ul', class_='examples')
        for e in examples:
            for ex in e.find_all('li'):
                print('\t-', ex.text)


word_to_search = input("Enter word to look up: ")
scrape_url = 'https://www.oxfordlearnersdictionaries.com/definition/english/' + word_to_search
headers = {"User-Agent": ""}
web_response = requests.get(scrape_url, headers=headers)

if web_response.status_code == 200:
    soup = BeautifulSoup(web_response.text, 'html.parser')

    try:
        show_origin(soup)
        show_definitions(soup)
    except AttributeError:
        print('Word not found!!')
else:
    print('Failed to get response...')