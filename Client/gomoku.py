#!/usr/bin/pyhon2.7.9

import pygame
import board


class Gomoku:
    def __init__(self, client, width, ai_turn=False):
        pygame.init()
        self.fps_clock = pygame.time.Clock()

        self.client = client
        self.board = board.Board(width)
        self.ai_turn = ai_turn

    def run(self):
        while not self.handle_events():
            self.board.draw()
            if self.ai_turn and self.board.game:
                move = self.client.reciveMsg()
                self.board.markers[int(move)] = board.player_marker(False)
                self.ai_turn = False
            self.fps_clock.tick(15)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                self.client.sendMsg("quit")
                return True

            if event.type == pygame.locals.MOUSEBUTTONDOWN and self.board.game:
                if self.ai_turn:
                    continue
                x, y = pygame.mouse.get_pos()
                self.ai_turn = self.board.player_move(self.client, x, y)
