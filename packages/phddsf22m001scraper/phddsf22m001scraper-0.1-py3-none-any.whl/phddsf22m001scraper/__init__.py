import requests
from bs4 import BeautifulSoup

def web_scraper(url, css_selectors):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = {}
    for key, value in css_selectors.items():
        result[key] = soup.select(value)
    return result
