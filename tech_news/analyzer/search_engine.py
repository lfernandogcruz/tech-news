from tech_news.database import search_news


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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
