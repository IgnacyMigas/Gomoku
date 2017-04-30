#!/usr/bin/pyhon2.7.9
import gomoku
import guessWhat
import server

if __name__ == "__main__":
    host = 'localhost'
    port = 50001
    data_size = 1024
    server = server.MyServer(host, port, data_size)
    server.getConnection()
    version = server.getMsg()

    if version == "1":
        print "Play gomoku"
        server.connection.send("good")
        size = server.getMsg()
        while not 3 <= int(size) <= 10:
            server.connection.send("wrong")
            print "Wrong size"
            size = server.getMsg()
        server.connection.send("good")
        game = gomoku.Gomoku(server, int(size))
    elif version == "2":
        print "Play guessWhat"
        server.connection.send("good")
        game = guessWhat.GuessWhat(server, 150)
    else:
        server.connection.send("wrong")
        print "Wrong input"
        exit(1)
    game.run()