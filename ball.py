import random

class Ball(object):
  color = (0,255,0)
  pos = (0,0)
  radius = 1

  def __init__(self, screenSize):
    self.x = int(screenSize[0]/2) if screenSize else 0
    self.y = int(screenSize[1]/2) if screenSize else 0
    self.x_speed = 1+random.randint(0,6)
    self.y_speed = 1+random.randint(0,6)
    self.color = (random.randint(240,255),random.randint(0,0),random.randint(136,255))
    self.pos = (self.x,self.y)
    self.radius = 10
