#!/usr/bin/pyhon2.7.9

import pygame
from math import log
from pygame.locals import *
from computer import Ai
from board import Board


class Gomoku:
    def __init__(self, server, width, ai_turn=False):
        pygame.init()

        self.fps_clock = pygame.time.Clock()

        self.server = server
        self.board = Board(width)
        self.ai = Ai(self.board)
        self.ai_turn = ai_turn

    def run(self):
        while not self.handle_events():
            self.board.draw()
            if self.ai_turn and self.board.game:
                move = self.ai.make_turn()
                self.server.connection.send(str(move))
                self.ai_turn = False
            self.fps_clock.tick(15)

    def handle_events(self):
        msg = self.server.getMsg()
        if msg == "quit":
            pygame.quit()
            self.server.connection.send("good")
            return True
        if self.board.game:
            x, y = map(int, msg.split())
            if not self.ai_turn:
                self.ai_turn = self.board.player_move(self.server, x, y)


if __name__ == "__main__":
    game = Gomoku(4)
    game.run()