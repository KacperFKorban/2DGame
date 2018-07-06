import pygame

class Map:
    def __init__(self, st):
        self.graphic = pygame.image.load("Images/Maps/tiledbackground.png")
        self.rect = self.graphic.get_rect()
        self.size = self.graphic.get_size()
        self.xSize = self.size[0]
        self.ySize = self.size[1]
        self.color = (0,162,0)
        self.x = 100
        self.y = 100
        self.xIncrement = 0
        self.yIncrement = 0
        self.xChunks = self.xSize / st.chunkSize
        self.yChunks = self.ySize / st.chunkSize

    def update(self, st, screen):
        if isValid(self.x, self.y, self.xIncrement, self.yIncrement, st):
            self.x += self.xIncrement
            self.y += self.yIncrement
        graphicRect = (self.x, self.y, st.screenX, st.screenY)
        screenRect = (0, 0, st.screenX, st.screenY)
        screen.blit(self.graphic, screenRect, graphicRect)

def isValid(x, y, xi, yi, st):
    if x+xi < 0:
        return False
    if x+xi > st.screenX:
        return False
    if y+yi < 0:
        return False
    if y+yi > st.screenY:
        return False
    return True