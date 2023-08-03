import pygame as pg
import random

pg.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
FPS = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake initial position and direction
snake = [(WIDTH // 2, HEIGHT // 2)]
direction = (0, -GRID_SIZE)

# Food initial position
food = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
        random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)

# Initialize the screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snake Game")

clock = pg.time.Clock()

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pg.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pg.draw.line(screen, BLACK, (0, y), (WIDTH, y))

def draw_snake():
    for segment in snake:
        pg.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

def draw_food():
    pg.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

def move_snake():
    global snake, food

    # Get the head of the snake
    head_x, head_y = snake[0]

    # Calculate the new position of the head based on the direction
    new_head_x = head_x + direction[0]
    new_head_y = head_y + direction[1]

    # Add the new head position to the snake
    snake.insert(0, (new_head_x, new_head_y))

    # Check if the snake ate the food
    if (new_head_x, new_head_y) == food:
        # Generate new food position
        food = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)
    else:
        # If not, remove the last segment (snake is not growing)
        snake.pop()

def check_collision():
    # Check if the snake collided with the wall
    head_x, head_y = snake[0]
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        return True

    # Check if the snake collided with itself
    for segment in snake[1:]:
        if segment == snake[0]:
            return True

    return False

def main():
    global direction

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    run = False
                elif event.key == pg.K_UP and direction != (0, GRID_SIZE):
                    direction = (0, -GRID_SIZE)
                elif event.key == pg.K_DOWN and direction != (0, -GRID_SIZE):
                    direction = (0, GRID_SIZE)
                elif event.key == pg.K_LEFT and direction != (GRID_SIZE, 0):
                    direction = (-GRID_SIZE, 0)
                elif event.key == pg.K_RIGHT and direction != (-GRID_SIZE, 0):
                    direction = (GRID_SIZE, 0)

        move_snake()

        if check_collision():
            run = False

        screen.fill(WHITE)
        draw_grid()
        draw_food()
        draw_snake()
        pg.display.update()
        clock.tick(FPS)

    pg.quit()

main()