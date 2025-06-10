import pygame

pygame.init()

# Setup
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Paddle Ball Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Game objects
ball = pygame.Rect(200, 200, 15, 15)
paddle = pygame.Rect(170, 380, 60, 10)
speed = [2, -2]  # Start slow

# State variables
score = 0
lives = 3
hit_counter = 0
next_speed_increase = 100  # first threshold
increment = 50  # increase threshold after each speedup

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= 5
    if keys[pygame.K_RIGHT] and paddle.right < 400:
        paddle.x += 5

    # Increase speed based on hit count thresholds
    if hit_counter >= next_speed_increase:
        speed[0] += 1 if speed[0] > 0 else -1
        speed[1] += 1 if speed[1] > 0 else -1
        next_speed_increase += increment
        increment += 50  # Increase interval (100 → 150 → 200 → ...)

    # Move ball
    ball.x += speed[0]
    ball.y += speed[1]

    # Bounce off walls
    if ball.left <= 0 or ball.right >= 400:
        speed[0] = -speed[0]
    if ball.top <= 0:
        speed[1] = -speed[1]

    # Paddle collision
    if ball.colliderect(paddle):
        speed[1] = -speed[1]
        score += 1
        hit_counter += 1

    # Ball missed
    if ball.bottom >= 400:
        lives -= 1
        if lives == 0:
            running = False
        else:
            ball.topleft = (200, 200)
            speed = [2, -2]
            hit_counter = 0
            next_speed_increase = 100
            increment = 50

    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (0, 255, 0), paddle)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    lives_text = font.render(f"Lives: {lives}", True, (255, 100, 100))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (300, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()