import pygame
import random
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640,480))

class Ball(object):
  color = (0,255,0)
  pos = (0,0)
  radius = 1

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = false

  screen.fill((40,40,40))
  screen.lock()


  screen.unlock()
  pygame.display.update()

pygame.quit()
quit()