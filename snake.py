import pygame as pg
from random import randint

pg.init()

WIDTH = 600
HEIGHT = 600
CASE_DIM = 20
IPS = 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

snake_pos = [
    (10, 15),
    (11, 15),
    (12, 15),
]
run = True

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

def set_background(white, black, dim):
    for i in range(30):
        for j in range(30):
            rect = pg.Rect(i*dim, j*dim, dim, dim)
            if (i+j)%2==0:
                pg.draw.rect(screen, white, rect)
            else: 
                pg.draw.rect(screen, black, rect)

set_background(WHITE, BLACK, CASE_DIM)

def snake(screen, snake_pos, dim, color):
    for i in range(len(snake_pos)):
        snake = pg.Rect(snake_pos[i][0]*dim, snake_pos[i][1]*dim, dim, dim)
        pg.draw.rect(screen, color, snake)

snake(screen, snake_pos, CASE_DIM, GREEN)

while run:
    clock.tick(IPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                run = False

    # random_color = (randint(0,255), randint(0,255), randint(0,255))
    # screen.fill(random_color)
    pg.display.update()

pg.quit()
