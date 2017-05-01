#!/usr/bin/pyhon2.7.9


class GuessWhat:
    def __init__(self, client):
        self.client = client

    def run(self):
        number = raw_input("Give a number (from 0 to 150): ")
        response = self.client.sendMsg(number)
        while response != "good":
            print response
            number = raw_input("Try again: ")
            response = self.client.sendMsg(number)
        print "You win, number is {}".format(number)
