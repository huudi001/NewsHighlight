import unittest
from .models import articles
Source = source..Source
class News_test(unittest.TestCase):
    def setUp(self):
        self.new_source = ("abc-news-au","ABC News 'au'","Australia's most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.","Your daily roundup of the biggest TechCrunch stories and startup news.", " "http://www.abc.net.au/news", "general")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
    unittest.main()
