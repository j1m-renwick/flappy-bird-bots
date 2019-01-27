import pygame
import numpy as np

from assets.Background import Background
from assets.Bird import Bird
from assets.PipePair import PipePair
from assets.Screen import Screen
from skynet.BirdBot import BirdBot
from skynet.Evolution import get_next_generation

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_X = 1000
SCREEN_Y = 500

pygame.init()
size = (SCREEN_X, SCREEN_Y)
clock = pygame.time.Clock()

screen = Screen(pygame.display.set_mode(size), SCREEN_Y - 20)

background = Background(screen.screen)

bird_population = []
dead_birds = []

for i in range(0, 50):
    bird_population.append(BirdBot(screen.screen))

pipes = []

for i in range(0, SCREEN_X, 200):
    pipes.append(PipePair(screen.screen, SCREEN_X + i))

while True:

    clock.tick(60)

    # for bird in bird_population:
    #     # get input data for bots
    #     next_pipe = screen.get_next_pipe(bird, pipes)
    #     top_pipe_dist = bird.ypos - next_pipe.gap_start
    #     bottom_pipe_dist = next_pipe.gap_end - bird.ypos + bird.sprite_height
    #     next_pipe_dist = next_pipe.xpos - bird.X_POS + bird.sprite_width
    #     # TODO normalise data!
    #     bird.input_data(np.array([bird.yvel, top_pipe_dist, bottom_pipe_dist, next_pipe_dist]))

    background.animate()
    for pipe in pipes:
        pipe.animate()
    for bird in bird_population:
        if screen.assess_death(bird, pipes):
            bird_population.remove(bird)
            dead_birds.append(bird)
            # print("score: " + str(dead_birds[0].score))
            # bird.ypos = 0
        # get input data for bots
        next_pipe = screen.get_next_pipe(bird, pipes)
        top_pipe_dist = (bird.ypos - next_pipe.gap_start)
        bottom_pipe_dist = (next_pipe.gap_end - bird.ypos + bird.sprite_height)
        next_pipe_dist = (next_pipe.xpos - bird.X_POS + bird.sprite_width) / SCREEN_X
        bird_vel = bird.yvel / 15
        bird.input_data(np.array([bird_vel, top_pipe_dist, bottom_pipe_dist, next_pipe_dist]))
        bird.animate()

    if len(bird_population) == 0:
        bird_population = get_next_generation(dead_birds, 0.1, screen.screen)
        dead_birds.clear()
        pipes.clear()
        for i in range(0, SCREEN_X, 200):
            pipes.append(PipePair(screen.screen, (SCREEN_X / 2) + i))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bird.jump()
