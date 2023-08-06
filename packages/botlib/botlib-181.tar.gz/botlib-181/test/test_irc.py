# This file is placed in the Public Domain.


"irc"


import unittest


from bot.irc import IRC


class TestIRC(unittest.TestCase):


    "irc unittest"


    def test_irc(self):
        "test irc constructor"
        i = IRC()
        self.assertEqual(type(i), IRC)
