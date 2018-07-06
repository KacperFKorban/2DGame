import pygame
from pygame.locals import *
from settings import Settings
from player import Player
from background import Background
from actions import actionListener

def launchGame():
    pygame.init()
    st = Settings()
    back = Background(st)
    pl = Player(st)
    screen = pygame.display.set_mode((st.screenWidth, st.screenHeight))
    pygame.display.set_caption('2DGame')
    screen.fill(back.color)
    pygame.display.flip()

    while st.runningFlag:
        actionListener(pl, st)
        pl.update(st)

launchGame()