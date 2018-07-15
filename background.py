import pygame
from maploader import loadMap

class Map:
    def __init__(self, st, mapGraphic, mapSource):
        self.graphic = pygame.image.load(mapGraphic)
        self.rect = self.graphic.get_rect()
        self.size = self.graphic.get_size()
        self.xSize = self.size[0]
        self.ySize = self.size[1]
        self.color = (255,255,255)
        self.x = 0
        self.y = 0
        self.xChunks = self.xSize / st.chunkSize
        self.yChunks = self.ySize / st.chunkSize
        self.collision = loadMap(mapSource)

    def update(self, st, screen, pl):
        if st.xToGo != 0 or self.isXValid(st, pl):
            if st.xToGo == 0:
                st.xToGo = st.xMovement
            if st.xToGo != 0:
                self.x += st.xStep * sgn(st.xToGo)
                pl.walkingX = sgn(st.xToGo)
                st.xToGo -= st.xStep * sgn(st.xToGo)
        if st.yToGo != 0 or self.isYValid(st, pl):
            if st.yToGo == 0:
                st.yToGo = st.yMovement
            if st.yToGo != 0:
                self.y += st.yStep * sgn(st.yToGo)
                pl.walkingY = sgn(st.yToGo)
                st.yToGo -= st.yStep * sgn(st.yToGo)
        graphicRect = (self.x, self.y, self.x+st.screenX, self.y+st.screenY)
        screenRect = (0, 0, st.screenX, st.screenY)
        screen.blit(self.graphic, screenRect, graphicRect)

    def isXValid(self, st, pl):
        if self.x+st.xMovement < 0:
            return False
        if self.x+st.xMovement+st.screenX > self.xSize:
            return False
        if self.collision[int((self.y + st.yToGo + pl.y * st.chunkSize) / st.chunkSize)][int((self.x + st.xMovement + pl.x * st.chunkSize) / st.chunkSize)] == '0':
            return False
        return True

    def isYValid(self, st, pl):
        if self.y + st.yMovement < 0:
            return False
        if self.y + st.yMovement + st.screenY > self.ySize:
            return False
        if self.collision[int((self.y + st.yMovement + pl.y * st.chunkSize) / st.chunkSize)][int((self.x + st.xToGo + pl.x * st.chunkSize) / st.chunkSize)] == '0':
            return False
        return True

    def isValid(self, st, pl):
        return isXValid(self, st, pl) and isYValid(self, st, pl)

def sgn(a):
    if a == 0:
        return 0
    if a > 0:
        return 1
    else:
        return -1

    