import snake as sn
import pygame
import random

class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, sn.grid_width-1)*sn.gridsize, random.randint(0, sn.grid_height-1)*sn.gridsize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (sn.gridsize, sn.gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)