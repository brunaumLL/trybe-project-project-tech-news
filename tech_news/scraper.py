import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url, header={"user-agent": "Fake user-agent"}, timeout=3)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    novidades = []

    for novidade in selector.css(".post-outer"):
        url = novidade.css(".entry-title a::attr(href)").get()
        novidades.append(url)
    return novidades


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
