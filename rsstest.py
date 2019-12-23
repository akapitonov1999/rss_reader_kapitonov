from unittest import TestCase
import json
import rss_reader


class MyTestCase(TestCase):
    def test_news_collector_empty_url(self):
        rss = rss_reader.ParserRSS('')
        self.assertEqual(rss.news_collector(), 'No url or url is incorrect!')

    def test_news_collector_invalid_url(self):
        rss = rss_reader.ParserRSS('12345')
        self.assertEqual(rss.news_collector(), 'No url or url is incorrect!')

    def test_news_collector_empty_url_limit(self):
        rss = rss_reader.ParserRSS('', 3)
        self.assertEqual(rss.news_collector(), 'No url or url is incorrect!')

    def test_news_collector_empty_url_and_limit(self):
        rss = rss_reader.ParserRSS('', '')
        self.assertEqual(rss.news_collector(), 'No url or url is incorrect!')

    def test_news_collector_valid_url_invalid_limit(self):
        rss = rss_reader.ParserRSS('https://news.yahoo.com/rss/', '')
        self.assertEqual(rss.news_collector(), None)

    def test_news_collector_invalid_url_valid_limit(self):
        rss = rss_reader.ParserRSS('123', 5)
        self.assertEqual(rss.news_collector(), 'No url or url is incorrect!')

    def test_custom_collector_empty_url(self):
        rss = rss_reader.ParserRSS('')
        self.assertEqual(rss.news_collector_custom(), 'No url or'
                                                      ' url is incorrect!')

    def test_custom_collector_invalid_url(self):
        rss = rss_reader.ParserRSS('12345')
        self.assertEqual(rss.news_collector_custom(), 'No url or '
                                                      'url is incorrect!')

    def test_to_epub_empty_url(self):
        rss = rss_reader.ParserRSS('')
        self.assertEqual(rss.to_epub(), None)

    def test_to_epub_invalid_url(self):
        rss = rss_reader.ParserRSS('12345')
        self.assertEqual(rss.to_epub(), None)

    def test_to_epub_empty_url_and_limit(self):
        rss = rss_reader.ParserRSS('', '')
        self.assertEqual(rss.to_epub(), None)

    def test_json_converter_custom_empty_url(self):
        rss = rss_reader.ParserRSS('')
        self.assertEqual(rss.json_converter_custom(), None)

    def test_cache_news_empty_url(self):
        rss = rss_reader.ParserRSS('')
        self.assertEqual(rss.cache_news(), None)

    def test_cache_extractor_empty_url(self):
        rss = rss_reader.ParserRSS('')
        self.assertEqual(rss.cache_extractor(), None)


