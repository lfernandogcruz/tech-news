import time
from parsel import Selector
import requests
from tech_news.database import create_news


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
    selector = Selector(text=html_content)
    # url - link para acesso da notícia.
    # <head><link rel="canonical" href=LINK></head>
    url = selector.css("link[rel=canonical]::attr(href)").get()
    # title - título da notícia.
    # <h1 class="entry-title">TITLE</h1>
    title = selector.css(".entry-title::text").get().rstrip()
    # timestamp - data da notícia, no formato dd/mm/AAAA.
    # <li class="meta-date">DATE</li>
    timestamp = selector.css(".meta-date::text").get()
    # writer - nome da pessoa autora da notícia.
    # <span class="author"><a ...>AUTHOR</a></span>
    writer = selector.css(".author a::text").get()
    # comments_count - número de comentários que a notícia recebeu.
    # <ol class="comment-list"><li>COMMENT</li></ol>
    comments = selector.css(".comment-list li").getall()
    # Se a informação não for encontrada, salve este atributo como 0 (zero)
    comments_count = len(comments)
    # summary - o primeiro parágrafo da notícia.
    # <div class="entry-content"><p>SUMMARY</p>...</div>
    # summary = selector.css(".entry-content p::text").getall()[0].rstrip()
    summary = selector.xpath("string(//p)").get().rstrip()
    # summary = selector.xpath("string(//p)").get()
    # tags - lista contendo tags da notícia.
    # <section class="post-tags">
    # <ul>
    # <li><h5 class="title-tags">Tags:</h5></li>
    # <li><a ... rel="tag">TAG</a></li>
    # <li><a ... rel="tag">TAG</a></li>
    # </ul>
    # </section>
    tags = selector.css(".post-tags a[rel=tag]::text").getall()
    # category - categoria da notícia.
    # <div class="meta-category"><a ...><span ...>XX</span>
    # <span class="label">CATEGORY</span></a></div>
    category = selector.css(".meta-category span.label::text").get()

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


# to remove trailing whitespaces at the end of TITLE and SUMMARY
# used rstrip() method, detailed at:
# https://www.w3schools.com/python/ref_string_rstrip.asp

# to get the first paragraph of SUMMARY
# used the xpath method to select the p nodes, detailed at:
# https://parsel.readthedocs.io/en/latest/usage.html


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    content = fetch(url)

    news = []
    while len(news) < amount:
        news_list = scrape_updates(content)
        for new in news_list:
            news.append(scrape_news(fetch(new)))

            if len(news) == amount:
                break

        next_page_link = scrape_next_page_link(content)
        content = fetch(next_page_link)

    create_news(news)

    return news
