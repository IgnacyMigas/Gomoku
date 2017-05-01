#!/usr/bin/pyhon2.7.9

import abc
import pygame
import pygame.locals


def player_marker(x_player):
    return "X" if x_player else "O"


def check_win(markers, x_player, width):
    find = [player_marker(x_player)] * width
    if width > 5:
        find = [player_marker(x_player)] * 5
    seq = range(width)

    def marker(xx, yy):
        return markers[xx + yy * width]

    # sprawdzamy kazdy rzad
    for x in seq:
        row = [marker(x, y) for y in seq if marker(x, y)]
        string = "".join(row)
        found = "".join(find)
        if string.find(found) >= 0:
            return True

    # sprawdzamy kazda kolumne
    for y in seq:
        col = [marker(x, y) for x in seq if marker(x, y)]
        string = "".join(col)
        found = "".join(find)
        if string.find(found) >= 0:
            return True

    # sprawdzamy przekatne
    diagonal1 = [marker(i, i) for i in seq if marker(i, i)]
    diagonal2 = [marker(i, abs(i - 2)) for i in seq if marker(i, abs(i - 2))]
    str1 = "".join(diagonal1)
    str2 = "".join(diagonal2)
    found = "".join(find)
    if str1.find(found) >= 0 or str2.find(found) >= 0:
        return True


class AbstractBoard(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def draw(self, w):
        pass

    @abc.abstractmethod
    def draw_net(self):
        pass


class Board(AbstractBoard):
    def __init__(self, width):
        self.w = width
        self.surface = pygame.display.set_mode((width * 100, width * 100), 0, 32)
        pygame.display.set_caption('Gomoku')

        pygame.font.init()
        font_path = pygame.font.match_font('arial')
        self.font = pygame.font.Font(font_path, 48)

        self.markers = [None] * width * width
        self.game = True

    def draw(self, *args):
        background = (0, 0, 0)
        self.surface.fill(background)
        self.draw_net()
        self.draw_markers()
        self.draw_score()
        for drawable in args:
            drawable.draw_on(self.surface)

        pygame.display.update()

    def draw_net(self):
        color = (255, 255, 255)
        width = self.surface.get_width()
        for i in range(1, self.w):
            pos = width / self.w * i
            # linia pozioma
            pygame.draw.line(self.surface, color, (0, pos), (width, pos), 1)
            # linia pionowa
            pygame.draw.line(self.surface, color, (pos, 0), (pos, width), 1)

    def player_move(self, client, x, y):
        response = client.sendMsg(str(x) + " " + str(y))
        cell_size = self.surface.get_width() / self.w
        x /= cell_size
        y /= cell_size
        if response == "good":
            self.markers[x + y * self.w] = player_marker(True)
            return True
        return False

    def draw_markers(self):
        box_side = self.surface.get_width() / self.w
        for x in range(self.w):
            for y in range(self.w):
                marker = self.markers[x + y * self.w]
                if not marker:
                    continue
                center_x = x * box_side + box_side / 2
                center_y = y * box_side + box_side / 2

                self.draw_text(self.surface, marker, (center_x, center_y))

    def draw_text(self, surface, text, center, color=(180, 180, 180)):
        text = self.font.render(text, True, color)
        rect = text.get_rect()
        rect.center = center
        surface.blit(text, rect)

    def draw_score(self):
        if check_win(self.markers, True, self.w):
            score = u"Wygrales(as)"
        elif check_win(self.markers, False, self.w):
            score = u"Przegrales(as)"
        elif None not in self.markers:
            score = u"Remis!"
        else:
            return

        i = self.surface.get_width() / 2
        self.draw_text(self.surface, score, center=(i, i), color=(255, 26, 26))
        self.game = False


if __name__ == '__main__':
    bd = Board(4)
    bd.draw_net()
