import time
from parsel import Selector
import requests


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        header = {"user-agent": "Fake user agent"}
        response = requests.get(url, timeout=3, headers=header)

        if response.status_code == 200:
            return response.text

        return None

    except requests.ReadTimeout:
        None
    finally:
        None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    # <h2 class="entry-title"><a href=LINK>TITLE</a></h2>
    result_list = selector.css(".entry-title a::attr(href)").getall()

    return result_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    # <a class="next page-numbers" href=LINK>"Próxima"</a>
    result = selector.css(".next::attr(href)").get()

    return result


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# iniciando o projeto
