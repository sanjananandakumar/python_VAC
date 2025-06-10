import pygame
import sys
import random

# Constants
WIDTH = 400
HEIGHT = 600
hit_counter = 0

# Initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paddle Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)
# bricks
brick_rows = 5
brick_cols = 8
brick_width = WIDTH // brick_cols
brick_height = 20
bricks = [ pygame.Rect(col*brick_width, row*brick_height,brick_width - 2, brick_height - 2 )
          for row in range(brick_rows) for col in range (brick_cols)]

# Paddle
paddle = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 30, 100, 10)
paddle_speed = 7

# Ball
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)

# Score
score = 0
# lives
lives =3
#speed
ball_speed=[4,-4]

def draw_paddle():
    pygame.draw.rect(screen, (0, 0, 0), paddle)

def draw_ball():
    pygame.draw.ellipse(screen, (200, 0, 0), ball)

def display_score():
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    text = font.render(f"Lives: {lives}", True, (0, 0, 0))
    screen.blit(text, (270, 10))

def game_over_function(final_score):
        screen.fill((255, 255, 255))
        game_over_text = font.render(f"Game Over! Final Score: {final_score}", True,       (0, 0, 125))
        score_text = font.render(f"final_score: {final_score}", True, (0, 0, 0))
        msg_text = font.render("thanks for playing", True, (0, 0, 0))
        screen.blit(game_over_text,(WIDTH// 2 - game_over_text.get_width() // 2, 120))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 200))
        screen.blit(msg_text, (WIDTH // 2 - msg_text.get_width() // 2, 250))
        pygame.display.flip()
        pygame.time.delay(3000) # wait for 3 seconds
def game_win_function(final_score):
        screen.fill((255, 255, 255))
        game_over_text = font.render(f"YOU WON !!!!!! Final Score: {final_score}", True,       (0, 0, 125))
        score_text = font.render(f"final_score: {final_score}", True, (0, 0, 0))
        msg_text = font.render("thanks for playing", True, (0, 0, 0))
        screen.blit(game_over_text,(WIDTH// 2 - game_over_text.get_width() // 2, 120))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 200))
        screen.blit(msg_text, (WIDTH // 2 - msg_text.get_width() // 2, 250))
        pygame.display.flip()
        pygame.time.delay(3000) # wait for 3 seconds

# Game Loop
running = True
while running:
    screen.fill((200, 255, 255))  # Light background
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed
#move ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]
    #bounce of walls
    if ball.left<=0 or ball.right >=WIDTH:
        ball_speed[0] =- ball_speed[0]
    if ball.top <=0:
        ball_speed[1] =- ball_speed[1]
#colloid
    if ball.colliderect(paddle):
        ball_speed[1] =- ball_speed[1]
        score += 1
        hit_counter +=1 
# brick collision
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed[1] =- ball_speed[1]
            score += 10
            hit_counter += 1
            break
    if len(bricks) == 0:
        game_win_function(score)
        pygame.quit()
        sys.exit()
    # increase speed of every 100
    if hit_counter and hit_counter % 100 == 0:
        ball_speed[0] += 1 if ball_speed[0] > 0 else -1
        ball_speed[1] += 1 if ball_speed[1] > 0 else -1
        hit_counter += 1

    # ball missed
    if ball.bottom>=HEIGHT:
        lives-=1
        if lives == 0:
            game_over_function(score)
            running = False
            # pygame.quit()
            # sys.exit()
        else:
            ball.topleft = (200,200)
            speed = [2,-2]
            hit_counter = 0 
            next_speed_increase =100
            increment =50
    # drawing
    screen.fill((255 , 255,255))
    pygame.draw.rect( screen, ((255,255,255)),ball)
    pygame.draw.rect(screen, ((0, 255 ,0 )),paddle)
    for brick in bricks:
        pygame.draw.rect(screen, ( random.randint(100,255),random.randint(50,200), 255), brick)

    
    draw_paddle()
    draw_ball()
    display_score()
   
   

    pygame.display.flip()

pygame.quit()
sys.exit()
