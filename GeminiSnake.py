import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Clock for controlling game speed
clock = pygame.time.Clock()

# -- Game Logic Variables --
snake_block = 10 
snake_speed = 15

font_style = pygame.font.SysFont(None, 30)

# Function to display score
def display_score(score):
    value = font_style.render("Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

def check_collision(snake_list, foodx, foody, screen_width, screen_height):
  head = snake_list[-1]  
  if head[0] >= screen_width or head[0] < 0 or head[1] >= screen_height or head[1] < 0:
    return True
  for segment in snake_list[:-1]: 
    if head == segment:
      return True
  if head[0] == foodx and head[1] == foody:
    return True
  return False

def game_over_display():  
  message = font_style.render("Game Over! Press R to restart or Q to quit", True, white)
  screen.blit(message, [screen_width / 6, screen_height / 3])
  pygame.display.update()  

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_over_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop() 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

        screen.fill(black)

        for x, y in snake_list:
          pygame.draw.rect(screen, green, [x, y, snake_block, snake_block])

        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        display_score(snake_length - 1)

        pygame.display.update()

        if check_collision(snake_list, foodx, foody, screen_width, screen_height):
            game_over = True
            game_close = True

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
