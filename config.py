import os

class Config:

    SOURCE_BASE_URL = 'https://newsapi.org/v1/sources?language=en&category={}&apiKey={}'
    ARTICLE_BASE_URL ='https://newsapi.org/v1/articles/{}?api_key={}'

    NEWS_API_KEY = os.environ.get('News_API_KEY')


class ProdConfig(Config):

    pass


class DevConfig(Config):


    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
