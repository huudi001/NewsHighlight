from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news,get_newses, search_news

@app.route('/news/<source>')
def news(source):

    news_source= get_news(source)
    title =  '{news.title}'

    return render_template('news.html',title = title,news_source = news_source)

@app.route('/')
def index():
    top_news = get_newses('top')
    populer_news = get_newses('populer')
    latest_news = get_newses('latest')


    title = 'Home - Welcome to The best news Website Online'
    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', title = title, top = top_news, populer = populer_news, latest = latest_news )

@app.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_newses= search_news(news_name_format)
    title =  {news_name.title}
    return render_template('search.html',news = searched_newses)
