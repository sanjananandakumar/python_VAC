import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Simple Platformer")

clock = pygame.time.Clock()

# # Player attributes
player = pygame.Rect(50, 300, 40, 60)
player_vel_y = 0
gravity = 1
jump_speed = -15
ground_y = 300
on_ground = True

running = True
while running:
      clock.tick(60)
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False

      keys = pygame.key.get_pressed()

     # Jump
      if keys[pygame.K_SPACE] and on_ground:
          player_vel_y = jump_speed # -15
          on_ground = False

#      # Apply gravity
      player_vel_y += gravity
      player.y += player_vel_y

#      # Floor collision
      if player.y >= ground_y:
          player.y = ground_y
          player_vel_y = 0
          on_ground = True

      screen.fill((135, 206, 235))  # sky blue background
      pygame.draw.rect(screen, (0, 128, 0), (0, ground_y + 60, 600, 40))  # ground
      pygame.draw.rect(screen, (255, 0, 0), player)  # player

      pygame.display.flip()

pygame.quit()
