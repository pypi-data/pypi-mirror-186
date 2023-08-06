# This file is placed in the Public Domain.


"rss"


import unittest


from bot.rss import Fetcher


class TestRss(unittest.TestCase):

    "rss unittest"

    def test_fetcher(self):
        "test fetcher constructor"
        fetcher = Fetcher()
        self.assertEqual(type(fetcher), Fetcher)
