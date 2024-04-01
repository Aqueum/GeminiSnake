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

all_scores = [] # Store scores across games

# Function to display score
def display_score(score):
    value = font_style.render("Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

# ... (Other functions: check_collision, generate_new_food_position - remain the same)

def game_over_display(score):  
  font_style = pygame.font.SysFont(None, 50)  
  message = font_style.render("Game Over! Final Score: " + str(score), True, white)
  screen.blit(message, [screen_width / 6, screen_height / 3])

  font_style = pygame.font.SysFont(None, 30) 
  message2 = font_style.render("Press Space to play again or Enter to quit", True, white)
  screen.blit(message2, [screen_width / 6 , screen_height / 3 + 50]) 

  pygame.display.update()  

def print_scores():
    print("Scores from this session:")
    for score in all_scores:
        print(score)

# Main game loop
def game_loop():
    print("Starting game loop")
    game_over = False
    game_close = False

    # ... (Initialization of x1, y1,  x1_change, y1_change, snake_list, foodx, foody - remains the same)

    while True: # Game now runs indefinitely
        
        while game_close:  
            game_over_display(snake_length - 1)  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: 
                        game_loop()  # Restart the game
                    if event.key == pygame.K_RETURN:  # Exit on Enter
                        game_over = True
                        game_close = False
                        print_scores()  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN: 
                # Updated comment to reflect added movement controls
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or \
                   event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
                    if (event.key == pygame.K_LEFT and x1_change != snake_block) or \
                       (event.key == pygame.K_RIGHT and x1_change != -snake_block): 
                        x1_change = -snake_block if event.key == pygame.K_LEFT else snake_block
                        y1_change = 0 
                    elif (event.key == pygame.K_UP and y1_change != snake_block) or \
                         (event.key == pygame.K_DOWN and y1_change != -snake_block):
                        y1_change = -snake_block if event.key == pygame.K_UP else snake_block 
                        x1_change = 0 

        x1 += x1_change
        y1 += y1_change

        collision, food_eaten = check_collision(snake_list, foodx, foody, screen_width, screen_height)
        if collision:  
            if not food_eaten: 
                game_over = True
                game_close = True
                all_scores.append(snake_length - 1)  # Add score to the list

        if food_eaten:
            snake_length += 1
            foodx, foody = generate_new_food_position(snake_list, screen_width, screen_height)
        
        # ... (Screen update, drawing, etc. - remains the same)

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
