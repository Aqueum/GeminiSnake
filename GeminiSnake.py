import pygame
import random

# Initialize Pygame
print("Initializing Pygame")
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
        return True, False  # Collision with wall, no food
    for segment in snake_list[:-1]: 
        if head == segment:
            return True, False  # Collision with self, no food
    if head[0] == foodx and head[1] == foody:
        return False, True  # No Collision, food eaten
    return False, False  # No collision, no food

def generate_new_food_position(snake_list, screen_width, screen_height):
    # ... (Existing function code)

def game_over_display():  
  font_style = pygame.font.SysFont(None, 50)  # Larger font 
  message = font_style.render("Game Over! Final Score: " + str(snake_length - 1), True, white)
  screen.blit(message, [screen_width / 6, screen_height / 3])
  pygame.display.update()  

# Main game loop
def game_loop():
    # ... (Initialization: x1, y1, x1_change, y1_change, snake_list, foodx, foody)

    while True: # Game now runs indefinitely
        
        while game_close:  # Game over display loop
            game_over_display()
            for event in pygame.event.get():
                # ... (Handle restart or quit logic)

        for event in pygame.event.get():
            # ... (Handle movement controls)

        x1 += x1_change
        y1 += y1_change

        collision, food_eaten = check_collision(snake_list, foodx, foody, screen_width, screen_height)
        if collision:  # Only end the game on wall collisions
            if not food_eaten: 
                game_over = True
                game_close = True  

        if food_eaten:
            snake_length += 1
            foodx, foody = generate_new_food_position(snake_list, screen_width, screen_height)
        
        screen.fill(black)

        # Update snake position (move the body)
        new_head = (x1, y1)
        snake_list.append(new_head)
        if len(snake_list) > snake_length:
            del snake_list[0]  # Remove the tail if the snake is not growing

        for x, y in snake_list:
            pygame.draw.rect(screen, green, [x, y, snake_block, snake_block])

        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
        display_score(snake_length - 1) 
        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
