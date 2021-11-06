from snake import Snake
from food import Food
import snake as sn
import pygame

def drawGrid(surface):
    for y in range(0, int(sn.grid_height)):
        for x in range(0, int(sn.grid_width)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x*sn.gridsize, y*sn.gridsize), (sn.gridsize,sn.gridsize))
                pygame.draw.rect(surface,(93,216,228), r)
            else:
                rr = pygame.Rect((x*sn.gridsize, y*sn.gridsize), (sn.gridsize,sn.gridsize))
                pygame.draw.rect(surface, (84,194,205), rr)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((sn.screen_width, sn.screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("monospace",16)

    while (True):
        clock.tick(10)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()

main()