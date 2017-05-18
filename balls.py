import pygame
import random
from ball import Ball

pygame.init()
screen = pygame.display.set_mode((640,480))
screen_width, screen_height = screen.get_size()
clock = pygame.time.Clock()

balls = []
for i in range(100):
  ball = Ball(screen.get_size())
  balls.append(ball)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill((40,40,40))
  screen.lock()

  for ball in balls:
    if ball.x <= 5 or ball.x >= screen_width-5:
      ball.x_speed *= -1 
    if ball.y <= 5 or ball.y >= screen_height-5:
      ball.y_speed *= -1
    ball.x += ball.x_speed
    ball.y += ball.y_speed

    pygame.draw.circle(screen, ball.color, (ball.x,ball.y), ball.radius)

  screen.unlock()
  pygame.display.update()
  clock.tick(60)

pygame.quit()
quit()