#!/usr/bin/pyhon2.7.9

import unittest
import mock
import math

import gomoku
from exception import *


class game_test(unittest.TestCase):
    def setUp(self):
        self.game = gomoku.Gomoku(4)


if __name__ == "__main__":
#    unittest.main()
    print "start"
    str=""
    found=""
    x=["X", None, "X", "R", "X", "W"]
    tmp = [x[y] for y in range(6) if x[y]]
    print tmp
    str = str.join(tmp)
    print str
    found="XW"
    print str.find(found)
    print "end"
