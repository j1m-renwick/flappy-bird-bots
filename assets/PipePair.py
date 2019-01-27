import random

import pygame

SCROLL_RATE = 2
PIPE_GAP = 100

class PipePair:

    def __init__(self, screen, xpos):
        self.pipe_bottom = pygame.image.load("resources/pipe_bottom.png")
        self.pipe_top = pygame.image.load("resources/pipe_top.png")
        self.screen = screen
        self.sprite_width = 55
        self.sprite_height = 500
        self.xpos = xpos
        self.generate_gap()

    def reset(self):
        self.xpos = self.screen.get_width()
        self.generate_gap()

    def generate_gap(self):
        self.gap_start = random.randint(50, self.screen.get_height() - PIPE_GAP - 50)
        self.gap_end = self.gap_start + PIPE_GAP

    def animate(self):
        self.scroll()
        self.screen.blit(self.pipe_bottom, [self.xpos, self.gap_end, self.sprite_width, self.sprite_height])
        self.screen.blit(self.pipe_top, [self.xpos, -(self.screen.get_height() - self.gap_start), self.sprite_width, self.sprite_height])

    def scroll(self):
        if self.xpos + self.sprite_width > 0:
            self.xpos -= SCROLL_RATE
        else:
            self.reset()