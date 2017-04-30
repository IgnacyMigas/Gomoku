#!/usr/bin/pyhon2.7.9

import random


class GuessWhat:
    def __init__(self, server, to=100):
        self.to = to
        self.number = 0
        self.server = server

    def init_rand(self):
        self.number = random.randint(0, self.to)

    def run(self):
        self.init_rand()
        number = self.server.getMsg()
        print self.number
        while self.guess(number):
            number = self.server.getMsg()

    def guess(self, number):
        print number
        if self.number == int(number):
            self.server.connection.send("good")
            print "You win, number is {}".format(self.number)
            return 0
        elif self.number > int(number):
            self.server.connection.send("Number is bigger")
            print "Number is bigger"
        else:
            self.server.connection.send("Number is smaller")
            print "Number is smaller"
        return 1
