from tech_news.database import get_collection
import pymongo


# Requisito 10
def top_5_news():
    db = get_collection()
    order_news = db.find().sort([
        ("comments_count", pymongo.DESCENDING),
        ("title", pymongo.ASCENDING)]).limit(5)
    news_list = []
    for new in order_news:
        news_list.append((new["title"], new["url"]))
    return news_list


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
