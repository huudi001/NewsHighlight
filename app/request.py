from app import app
import urllib.request,json
from .models import news

News = news.News
api_key = app.config['NEWS_API_KEY']
base_url = app.config["NEWS_API_BASE_URL"]

def get_newses(category):
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_articles = None

        if get_news_response['articles']:
            news_articles_list = get_news_response['articles']
            news_articles = process_results(news_articles_list)


    return news_articles

def process_results(news_article_list):
    news_list= []
    for news_item in news_article_list:
        id = news_item.get("source")
        author = news_item.get("author")
        title = news_item.get("title")
        description = news_item.get("description")
        url = news_item.get("url")
        url_to_image = news_item.get("url_to_image")
        published_at = new_item.get("published_at")


        if url_to_image:
            news_object = News(source,author,title,description,url,url_to_image,published_at)
            news_list.append(news_object)
    return news_list
def get_news(source):
    get_news_details_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            source = news_details_response.get('source')
            author = news_details_response.get('author')
            title = news_details_response.get('title')
            description = news_details_response.get('description')
            url = news_details_response.get('url')
            url_to_image = news_details_response.get('url_to_image')
            published_at = news_details_response.get('published_at')

            news_object = News(source,author,title,description,url,url_to_image,published_at)

    return news_object
def search_news(news_name):
    search_news_url = 'https://newsapi.org/v1\search/news?api_key=6ad7a206321742c6b17f7ec2d8b3cab2&query=news_name'
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)


        search_news_articles = None

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_articles = process_results(search_news_list)


    return search_news_articles
