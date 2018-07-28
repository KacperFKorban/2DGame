import pygame
from enum import Enum

class Npc:
    def __init__(self, graphicPath, x, y, typ):
        self.x = x
        self.y = y
        self.graphic = pygame.image.load(graphicPath)
        self.type = typ

    def update(self, mapa, screen, st):
        if self.isInRange(mapa, st):
            screen.blit(self.graphic, (self.x * st.chunkSize - mapa.x, self.y * st.chunkSize - mapa.y))

    def isInRange(self, mapa, st):
        x = self.x * st.chunkSize
        y = self.y * st.chunkSize
        if x >= mapa.x and x < mapa.x + st.screenX and y >= mapa.y and y < mapa.y + st.screenY:
            return True
        else:
            return False

    def interact(self):
        if self.type == NpcType.friendly:
            self.interactFriendly()
        elif self.type == NpcType.neutral:
            self.interactNeutral()
        elif self.type == NpcType.hostile:
            self.interactHostile()

    def interactFriendly(self):
        pass

    def interactNeutral(self):
        pass

    def interactHostile(self):
        pass

class NpcType(Enum):
    friendly = 1
    neutral = 2
    hostile = 3