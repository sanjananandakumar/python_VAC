import pygame
import random
import sys

# Initialize
pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Platformer")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
big_font = pygame.font.SysFont(None, 70)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Ground
GROUND_Y = 300

# Player
dino = pygame.Rect(100, GROUND_Y - 40, 40, 40)
vel_y = 0
gravity = 1
jumping = False
speed = 5

# Obstacles
obstacles = []
OBSTACLE_WIDTH = 30
OBSTACLE_HEIGHT = 50
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 1500)

# # Score
score = 0

def draw_dino():
    pygame.draw.rect(screen, GREEN, dino)

def draw_obstacles():
    for obs in obstacles:
        pygame.draw.rect(screen, RED, obs)

def draw_ground():
    pygame.draw.rect(screen, BLACK, (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))

def display_score(score):
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

def game_over_screen(final_score):
    screen.fill(WHITE)
    game_over_text = big_font.render("Thanks for playing !", True, RED)
    score_text = font.render(f"Final Score: {final_score}", True, BLACK)


    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, 120))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 200))
   

    pygame.display.flip()
    pygame.time.delay(3000)  # Wait for 3 seconds

# # Game Loop
running = True
while running:
    screen.fill(WHITE)
    draw_ground()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWN_EVENT:
            obstacles.append(pygame.Rect(WIDTH, GROUND_Y - OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

#     # Key input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and dino.left > 0:
        dino.x -= speed
    if keys[pygame.K_RIGHT] and dino.right < WIDTH:
        dino.x += speed
    if keys[pygame.K_SPACE] and not jumping:
        vel_y = -15
        jumping = True

#     # Apply gravity
    vel_y += gravity
    dino.y += vel_y
    if dino.y >= GROUND_Y - dino.height:
        dino.y = GROUND_Y - dino.height
        vel_y = 0
        jumping = False

#     # Move obstacles
    for obs in obstacles:
        obs.x -= 6
    obstacles = [obs for obs in obstacles if obs.x > -OBSTACLE_WIDTH]

#     # Collision
    for obs in obstacles:
        if dino.colliderect(obs):
            game_over_screen(score)
            pygame.quit()
            sys.exit()

#     # Score
    score += 1

#     # Draw everything
    draw_dino()
    draw_obstacles()
    display_score(score // 10)

    pygame.display.flip()
    clock.tick(30)
