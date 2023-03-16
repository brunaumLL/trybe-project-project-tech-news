from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news = search_news(query)
    news_list = []
    for new in news:
        news_list.append((new["title"], new["url"]))
    return news_list


# Requisito 7
def search_by_date(date):
    try:
        time = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        formatted_time = time.strftime("%d/%m/%Y")
    query = {"timestamp": formatted_time}
    news = search_news(query)
    news_list = []
    for new in news:
        news_list.append((new["title"], new["url"]))
    return news_list


# Requisito 8
def search_by_tag(tag):
    query = {"tags": {"$regex": tag, "$options": "i"}}
    news = search_news(query)
    news_list = []
    for new in news:
        news_list.append((new["title"], new["url"]))
    return news_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
