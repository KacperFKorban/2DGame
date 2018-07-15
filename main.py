import pygame
import time
from settings import Settings
from player import Player
from background import Map
from actions import actionListener
from menu import Menu


def launchGame():
    pygame.init()
    st = Settings()
    mapa = Map(st, './images/maps/temptilesbig.jpg', './maps/map')
    pl = Player(st)
    menu = Menu()
    npcs = []
    screen = pygame.display.set_mode((st.screenX, st.screenY))
    pygame.display.set_caption("2DGame")

    while st.runningFlag:
        if st.menuFlag:
            menu.actionListener(st)
            menu.update(screen, st)
            pygame.display.update()
        else:
            screen.fill(mapa.color)
            actionListener(pl, st, mapa, npcs)
            mapa.update(st, screen, pl)
            pl.update(st, screen)
            pygame.display.update()
            time.sleep(0.06)

launchGame()