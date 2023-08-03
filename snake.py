import pygame as pg
from random import randint

pg.init()

WIDTH = 600
HEIGHT = 600
CASE_DIM = 20
IPS = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

snake_pos = [
    (10, 15),
    (11, 15),
    (12, 15),
    (13, 15),
]
dir = (-1, 0)
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

def init_snake(screen, snake_pos, dim, color):
    for i in range(len(snake_pos)-1):
        snake = pg.Rect(snake_pos[i][0]*dim, snake_pos[i][1]*dim, dim, dim)
        pg.draw.rect(screen, color, snake)

def update_snake(screen, snake_pos, dim, color, dir):
    snake_pos.insert(0, tuple(map(lambda i, j: i+j, dir, snake_pos[0])))
    snake_pos.pop(-1)
    return snake_pos

def init_case(screen, snake_pos, dim=CASE_DIM, white=WHITE, black=BLACK):
    switched_case = snake_pos[-1]
    rect = pg.Rect(switched_case[0]*dim, switched_case[1]*dim, dim, dim)
    color = white if (snake_pos[-1][0]+snake_pos[-1][1])%2==0 else black
    pg.draw.rect(screen, color, rect)


while run:

    clock.tick(IPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                run = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                dir = (0, -1)
            elif event.key == pg.K_DOWN:
                dir = (0, 1)

            elif event.key == pg.K_LEFT:
                dir = (-1, 0)
            elif event.key == pg.K_RIGHT:
                dir = (1, 0)

    if dir != (0, 0):
        init_case(screen, snake_pos)
    update_snake(screen, snake_pos, CASE_DIM, GREEN, dir)
    init_snake(screen, snake_pos, CASE_DIM, GREEN)


    pg.display.update()

pg.quit()
