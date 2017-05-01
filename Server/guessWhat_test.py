#!/usr/bin/pyhon2.7.9

import unittest
from guessWhat import GuessWhat


class Connection:
    def __init__(self):
        pass

    def send(self, str):
        pass


class ServerMock:
    def __init__(self):
        self.connection = Connection()


class TestGuessWhat(unittest.TestCase):
    def setUp(self):
        self.game = GuessWhat(ServerMock())

    def test_put_string(self):
        self.assertTrue(self.game.guess("asd"))

    def test_put_smaller_value(self):
        self.assertTrue(self.game.guess("-10"))

    def test_put_bigger_value(self):
        self.assertTrue(self.game.guess("200"))

    def test_put_right_value(self):
        self.assertFalse(self.game.guess("63"))

if __name__ == "__main__":
        unittest.main()
