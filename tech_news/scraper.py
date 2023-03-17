import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3)
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
    try:
        selector = Selector(html_content)
        next_page = selector.css(".next::attr(href)").get()
        return next_page
    except not next_page:
        return None


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".meta-author a::text").get()
    comments_text = selector.css(".post-comments .title-block::text").get()
    if not comments_text:
        comments_count = 0
    else:
        comments_count = comments_text.split(' ')[0]
    summary = selector.css(".entry-content > p:first-of-type *::text").getall()
    summary = "".join(summary).strip()
    tags = selector.css(".post-tags a::text").getall()
    category = selector.css("span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    URL = 'https://blog.betrybe.com/'
    news_list = []

    while len(news_list) < amount:
        response = fetch(URL)
        news = scrape_novidades(response)
        for new in news:
            if len(news_list) == amount:
                break
            response_new = fetch(new)
            scrape_new = scrape_noticia(response_new)
            news_list.append(scrape_new)
        URL = scrape_next_page_link(response)

    create_news(news_list)
    return news_list
