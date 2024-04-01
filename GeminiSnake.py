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

# ... (We'll define more functions later)

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Starting snake position and length 
    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    snake_length = 1

    # Random initial food position
    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    while not game_over:
        # Game Over handling
        while game_close:
            # Display Game Over message
            # ... 

        # Event Handling (Keyboard, Quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:  
                # Change snake direction
                # ...

        # Update snake position
        x1 += x1_change
        y1 += y1_change

        # Background
        screen.fill(black)

        # Draw snake
        # ...

        # Draw food
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        # Display Score
        display_score(snake_length - 1)

        # Refresh screen
        pygame.display.update()

        # Collision with edges
        # ...

        # Collision with self
        # ...

        # Snake eats food
        # ...

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
