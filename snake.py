import pygame as pg
from random import randint

pg.init()

WIDTH = 400
HEIGHT = 300
IPS = 1
run = True

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

while run:
    clock.tick(IPS)

    for event in pg.event.get():
        pass

    random_color = (randint(0,255), randint(0,255), randint(0,255))
    screen.fill(random_color)
    pg.display.update()