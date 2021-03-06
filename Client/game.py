#!/usr/bin/pyhon2.7.9
import gomoku
import guessWhat
import client


class Game:
    def __init__(self, host='localhost', port=50001, data_size=1024):
        self.host = host
        self.port = port
        self.data_size = data_size
        self.client = None

    def run(self):
        self.client = client.MyClient(self.host, self.port, self.data_size)
        version = raw_input("Select game:\n 1 - Gomoku\n 2 - Guess number\n")
        response = self.client.sendMsg(version)
        if response == "good":
            print "good"
        else:
            print "wrong input"
            exit(1)

        if version == "1":
            size = raw_input("Give a size of grid (from 3 to 10): ")
            while self.client.sendMsg(size) != "good":
                size = raw_input("Wrong size, try again: ")
            game = gomoku.Gomoku(self.client, int(size))
        elif version == "2":
            game = guessWhat.GuessWhat(self.client)
        else:
            print "Wrong input"
            exit(1)
        game.run()


if __name__ == "__main__":
#    host = raw_input("Put host name: ")
    games = Game()
    games.run()
