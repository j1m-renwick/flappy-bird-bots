import pygame

GRAVITY = 1.2
JUMP_VEL = -13


class Bird:
    ypos = 250
    X_POS = 100
    yvel = 0


    def __init__(self, screen):
        self.sprite = pygame.image.load("resources/bird.png")
        self.sprite_width = self.sprite.get_width()
        self.sprite_height = self.sprite.get_height()
        self.screen = screen

    def animate(self):
        self.yvel = min(self.yvel + GRAVITY, 15)
        self.ypos += min(self.yvel, 15)
        self.screen.blit(self.sprite, [self.X_POS, self.ypos, self.sprite_width, self.sprite_height])

    def jump(self):
        self.yvel = JUMP_VEL

