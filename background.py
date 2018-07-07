import pygame

class Map:
    def __init__(self, st):
        #self.graphic = pygame.image.load("Images/Maps/tiledbackground.png")
        self.graphic = pygame.image.load("Images/Maps/temp1.jpg")
        self.rect = self.graphic.get_rect()
        self.size = self.graphic.get_size()
        self.xSize = self.size[0]
        self.ySize = self.size[1]
        self.color = (0,162,0)
        self.x = 0
        self.y = 0
        self.xChunks = self.xSize / st.chunkSize
        self.yChunks = self.ySize / st.chunkSize

    def update(self, st, screen):
        if isValid(self.x, self.y, st.xIncrement, st.yIncrement, self.xSize, self.ySize, st):
            self.x += st.xIncrement
            self.y += st.yIncrement
        graphicRect = (self.x, self.y, self.x+st.screenX, self.y+st.screenY)
        screenRect = (0, 0, st.screenX, st.screenY)
        screen.blit(self.graphic, screenRect, graphicRect)

def isValid(x, y, xi, yi, xSize, ySize, st):
    if x+xi < 0:
        return False
    if x+xi+st.screenX > xSize:
        return False
    if y+yi < 0:
        return False
    if y+yi+st.screenY > ySize:
        return False
    return True