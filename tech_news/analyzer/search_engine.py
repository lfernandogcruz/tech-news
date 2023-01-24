from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    found = search_news({"title": {"$regex": title, "$options": "i"}})
    list = []
    for item in found:
        list.append((item["title"], item["url"]))
    return list


# elemento de filtragem $regex sugerido na página:
# https://pythoniluminado.netlify.app/mongodb

# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        found = search_news(
            {
                "timestamp": {
                    "$eq": datetime.fromisoformat(date).strftime("%d/%m/%Y")
                }
            }
        )
        list = []
        for item in found:
            list.append((item["title"], item["url"]))
        return list
    except ValueError:
        raise ValueError("Data inválida")


# conversão de data de YYYY-MM-DD para DD/MM/YYYY sugerida em thread
# no StackOverflow no link:
# https://stackoverflow.com/questions/502726/converting-date-between-dd-mm-yyyy-and-yyyy-mm-dd


# Requisito 8
def search_by_tag(tag):
    found = search_news({"tags": {"$regex": tag, "$options": "i"}})
    list = []
    for item in found:
        list.append((item["title"], item["url"]))
    return list


# Requisito 9
def search_by_category(category):
    found = search_news({"category": {"$regex": category, "$options": "i"}})
    list = []
    for item in found:
        list.append((item["title"], item["url"]))
    return list
