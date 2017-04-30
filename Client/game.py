#!/usr/bin/pyhon2.7.9
import gomoku
import guessWhat
import client

if __name__ == "__main__":
    host = raw_input("Put host name: ")
    port = 50001
    data_size = 1024
    client = client.MyClient(host, port, data_size)

    version = raw_input("Select game:\n 1 - Gomoku\n 2 - Guess number\n")
    response = client.sendMsg(version)
    if response == "good":
        print "good"
    else:
        print "wrong input"
        exit(1)


#    resp = client.reciveMsg()
    if version == "1":
        size = 0
        size = raw_input("Give a size of grid (from 3 to 10): ")
        while client.sendMsg(size) != "good":
            size = raw_input("Wrong size, try again: ")
        game = gomoku.Gomoku(client, int(size))
    elif version == "2":
        game = guessWhat.GuessWhat(client, 150)
    else:
        print "Wrong input"
        exit(1)
    game.run()