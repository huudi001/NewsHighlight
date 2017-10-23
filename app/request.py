# from app import app
import urllib.request,json
from .models import Article
from .models import Source
# creating news class
# Article = article.Article
# Source = source.Source
apiKey = None

source_url  = None

article_url = None


def configure_request(app):

    global apiKey, source_url, article_url
    # get api key
    apiKey = app.config['NEWS_API_KEY']
    # get source_url
    source_url = app.config['SOURCE_BASE_URL']
    #  get article_url
    article_url = app.config['ARTICLE_BASE_URL']

# def get_source(category):
#     get_sources_details_url = source_url.format(category,apiKey)
#
#     with urllib.request.urlopen(get_sources_details_url) as url:
#         source_details_data = url.read()
#         source_details_response = json.loads(source_details_data)
#
#         source_results = None
#         if source_details_response['sources']:
#             sources_results_list = source_details_response['sources']
#             source_results = process_sources(sources_results_list)
#     return source_results


def get_source(category):
    get_sources_details_url = source_url.format(category,apiKey)

    with urllib.request.urlopen(get_sources_details_url) as url:
        source_details_data = url.read().decode('utf8')
        source_details_response = json.loads(source_details_data)

        source_results = None
        if source_details_response['sources']:
            sources_results_list = source_details_response['sources']
            source_results = process_sources(sources_results_list)

    return source_results

def process_sources(source_results_list):
    source_results = []
    for source_item in source_results_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        if url:
            source_object = Source(id , name, description, url, category)
            source_results.append(source_object)

    return source_results



def get_articles(id):
    get_article_url = article_url.format(id,apiKey)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read().decode('utf8')
        get_article_response = json.loads(get_article_data)

        news_articles = None

        if get_article_response['articles']:
            news_articles_list = get_article_response['articles']
            news_articles = process_articles(news_articles_list)


    return news_articles

def process_articles(news_article_list):
    '''
    Function  that processes the new result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_articles= []
    for article_item in news_article_list:
        author = article_item.get("author")
        title = article_item.get("title")
        description = article_item.get("description")
        url = article_item.get("url")
        url_to_image = article_item.get("urlToImage")
        published_at = article_item.get("published_at")


        if url_to_image:
            article_object = Article(author,title,description,urlToImage,published_at)
            news_articles.append(article_object)
    return news_article
