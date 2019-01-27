import pygame

SCROLL_RATE = 1


class Background:


    def __init__(self, screen):
        self.sprite = pygame.image.load("resources/background.png")
        self.screen = screen
        self.sprite_width = self.sprite.get_width()
        self.sprite_height = self.sprite.get_height()
        self.xpos = 0

    def animate(self):
        self.scroll()
        self.screen.blit(self.sprite, [self.xpos, 0, self.sprite_width, self.sprite_height])
        self.screen.blit(self.sprite, [self.xpos + self.sprite_width, 0, self.sprite_width, self.sprite_height])

    def scroll(self):
        self.xpos = self.xpos - SCROLL_RATE if self.xpos + self.sprite_width > 0 else 0