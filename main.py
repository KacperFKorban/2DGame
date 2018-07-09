import pygame
import time
from pygame.locals import *
from settings import Settings
from player import Player
from background import Map
from actions import actionListener


def launchGame():
    pygame.init()
    st = Settings()
    mapa = Map(st, './Images/Maps/temptilesbig.jpg', './map')
    pl = Player(st)
    screen = pygame.display.set_mode((st.screenX, st.screenY))
    pygame.display.set_caption("2DGame")

    while st.runningFlag:
        screen.fill(mapa.color)
        actionListener(pl, st, mapa)
        mapa.update(st, screen, pl)
        pl.update(st, screen)
        pygame.display.update()
        time.sleep(0.02)

launchGame()