import pygame
from pygame.locals import *
from settings import Settings
from player import Player
from background import Map
from actions import actionListener

def launchGame():
    pygame.init()
    st = Settings()
    mapa = Map(st)
    pl = Player(st)
    screen = pygame.display.set_mode((st.screenX, st.screenY))
    pygame.display.set_caption('2DGame')
    screen.fill(mapa.color)
    pygame.display.flip()

    while st.runningFlag:
        actionListener(pl, st)
        mapa.update(st, screen)
        pl.update(st, screen)
        pygame.display.update()

launchGame()