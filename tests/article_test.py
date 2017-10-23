import unittest
from .models import news
News = news.News
class News_test(unittest.TestCase):
    def setUp(self):
        self.new_news = News("TechCrunch","khaled Tito","Crunch report","Your daily roundup of the biggest TechCrunch stories and startup news.", "https://techcrunch.com/video/crunchreport/", "https://tctechcrunch2011.files.wordpress.com/2015/03/tccrshowogo.jpg?w=500&h=200&crop=1",2017-10-18T20:31:43Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()
