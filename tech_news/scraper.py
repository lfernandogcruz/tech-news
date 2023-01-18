import time
import requests


# Requisito 1
def fetch(url):
    try:
        header = {"user-agent": "Fake user agent"}
        time.sleep(1)
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
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# iniciando o projeto
