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
    db = get_collection()
    abc = db.aggregate([
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}}
        ])
    news_list = []
    for a in abc:
        if len(news_list) == 5:
            break
        news_list.append(a["_id"])
    return news_list
