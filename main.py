import pygame
import time
from settings import Settings
from player import Player
from background import Map
from actions import actionListener
from menu import Menu
from npc import Npc, NpcType

def launchGame():
    pygame.init()
    st = Settings()
    mapa = Map(st, './images/maps/temptilesbig.jpg', './maps/map')
    pl = Player(st)
    menu = Menu()
    npcs = [Npc("./images/sprite_scaled/front1.png", 12, 10, NpcType.neutral)]
    screen = pygame.display.set_mode((st.screenX, st.screenY))
    pygame.display.set_caption("2DGame")

    while st.runningFlag:
        if st.menuFlag:
            menu.actionListener(st)
            menu.update(screen, st)
            pygame.display.update()
        elif st.inventoryFlag:
            pl.inventory.actionListener(pl, st)
            pl.inventory.update(screen)
            pygame.display.update()
        else:
            screen.fill(mapa.color)
            actionListener(pl, st, mapa, npcs)
            mapa.update(st, screen, pl)
            for npc in npcs:
                npc.update(mapa, screen, st)
            pl.update(st, screen)
            pygame.display.update()
            time.sleep(0.06)

launchGame()