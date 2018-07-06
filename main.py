import pygame
from pygame.locals import *
from settings import Settings

def launchGame():
    pygame.init()
    st = Settings()
    screen = pygame.display.set_mode((st.screenWidth, st.screenHeight))
    pygame.display.set_caption('2DGame')
    screen.fill((255,255,255))
    pygame.display.flip()
    runningFlag = True
    while runningFlag:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          runningFlag = False

launchGame()