# This file is placed in the Public Domain.


"scan tests"


import unittest


from bot.command import irc
from bot.handler import Command
from bot.scanner import scancmd


class TestScan(unittest.TestCase):

    "scan unittest"

    def test_scan(self):
        "test scanning of the irc module"
        scancmd(irc)
        self.assertTrue("icfg" in Command.cmd)
