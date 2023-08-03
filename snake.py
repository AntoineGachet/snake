import pygame as pg
from random import choice

pg.init()

WIDTH = 600
HEIGHT = 600
CASE_DIM = 20
IPS = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

counter = 0
snake = [
    (14, 15),
    (15, 15),
    (16, 15),
    (17, 15),
    (18, 15),
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

def available_case(snake):
    available = [(u, v) for u in range(30) for v in range(30)]
    for i in snake:
        if i in available:
            available.remove(i)
    return available

available = available_case(snake)
print(available)
apple_pos = choice(available)

def wall_coll(snake):
    head = snake[0]
    if (head[0] < 0) or (head[0] >= 29) or (head[1] < 0) or (head[1] >= 29):
        return False
    return True

def self_coll(snake):
    for i in range(1, len(snake)):
        if snake[0] == snake[i]:
            return False
    return True

def show_snake(screen, snake, dim, color):
    for i in range(len(snake)-1):
        snake_ = pg.Rect(snake[i][0]*dim, snake[i][1]*dim, dim, dim)
        pg.draw.rect(screen, color, snake_)

def update_snake(snake, dir):
    snake.insert(0, tuple(map(lambda i, j: i+j, dir, snake[0])))
    snake.pop(-1)
    return snake

def update_case(screen, snake, dim=CASE_DIM, white=WHITE, black=BLACK):
    switched_case = snake[-1]
    rect = pg.Rect(switched_case[0]*dim, switched_case[1]*dim, dim, dim)
    color = white if (snake[-1][0]+snake[-1][1])%2==0 else black
    pg.draw.rect(screen, color, rect)

def new_apple(available=available):
    new_pos = choice(available)
    return new_pos

def display_apple(apple_pos, dim=CASE_DIM, red=RED, screen=screen):
    apple = pg.Rect(apple_pos[0]*dim, apple_pos[1]*dim, dim, dim)
    pg.draw.rect(screen, red, apple)

def check_apple_eaten(apple_pos=apple_pos, snake=snake):
    if snake[0] == apple_pos:

        if snake[-1][0] != snake[-2][0]:
            diff = snake[-2][0] - snake[-1][0]
            snake.append((snake[-1][0]-diff,snake[-1][1]))
        
        if snake[-1][1] != snake[-2][1]:
            diff = snake[-2][1] - snake[-1][1]
            snake.append((snake[-1][0],snake[-1][1]-diff))
        return True
    return False


while run:
    counter += 1
    clock.tick(IPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                run = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                if dir == (0, 1):
                    continue
                dir = (0, -1)
            elif event.key == pg.K_DOWN:
                if dir == (0, -1):
                    continue
                dir = (0, 1)

            elif event.key == pg.K_LEFT:
                if dir == (1,0):
                    continue
                dir = (-1, 0)
            elif event.key == pg.K_RIGHT:
                if dir == (-1, 0):
                    continue
                dir = (1, 0)

    display_apple(apple_pos)
    update_case(screen, snake)
    update_snake(snake,dir)
    if check_apple_eaten(apple_pos):
        apple_pos = new_apple()
    show_snake(screen, snake, CASE_DIM, GREEN)
    run = self_coll(snake) + wall_coll(snake)
    if run < 2:
        run = False

    pg.display.update()

pg.quit()
