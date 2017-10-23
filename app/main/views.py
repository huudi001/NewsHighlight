from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_articles,get_source
from ..models import Article, Source

@main.route('/')
def index():
    business_source = get_source('business')
    entertainment_source = get_source('entertainment')
    politics_source = get_source('politics')
    sport_source = get_source('sport')
    technology_source = get_source('technology')

    title = 'Home - Welcome to The best news Website Online'

    return render_template('index.html', title = title, business = business_source, entertainment = entertainment_source, politics = politics_source, sport = sport_source, technology = technology_source)


@main.route('/news/<id>')
def news(id):

    news_article = get_articles(id)
    title =  '{id}'

    return render_template('news.html',title = title, news_article = news_article)
