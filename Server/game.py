#!/usr/bin/pyhon2.7.9
import gomoku
import guessWhat
import server


class Game:
    def __init__(self, host='localhost', port=50001, data_size=1024):
        self.host = host
        self.port = port
        self.data_size = data_size
        self.server = None

    def run(self):
        self.server = server.MyServer(self.host, self.port, self.data_size)
        self.server.getConnection()

        version = self.server.getMsg()
        if version == "1":
            print "Play gomoku"
            self.server.connection.send("good")
            size = self.server.getMsg()
            while not 3 <= int(size) <= 10:
                self.server.connection.send("wrong")
                print "Wrong size"
                size = self.server.getMsg()
            self.server.connection.send("good")
            game = gomoku.Gomoku(self.server, int(size))
        elif version == "2":
            print "Play guessWhat"
            self.server.connection.send("good")
            game = guessWhat.GuessWhat(self.server, 150)
        else:
            self.server.connection.send("wrong")
            print "Wrong input"
            exit(1)
        game.run()


if __name__ == "__main__":
    games = Game()
    games.run()
