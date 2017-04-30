#!/usr/bin/pyhon2.7.9

import random


class GuessWhat:
    def __init__(self, client, to=100):
        self.to = to
        self.number = 0
        self.client = client

    def init_rand(self):
        self.number = random.randint(0, self.to)

    def run(self):
        self.init_rand()
        number = int(input("Give a number (from 0 to 150): "))
        response = self.client.sendMsg(str(number))
        while response != "good":
            print response
            number = int(input("Try again: "))
            response = self.client.sendMsg(str(number))
        print "You win, number is {}".format(number)
