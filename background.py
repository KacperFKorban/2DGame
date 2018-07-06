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
        self.xMovement = 0
        self.yMovement = 0
        self.xChunks = self.xSize / st.chunkSize
        self.yChunks = self.ySize / st.chunkSize

    def update(self, st, screen):

        graphicRect = (self.x, self.y, st.screenX, st.screenY)
        screenRect = (0, 0, st.screenX, st.screenY)
        screen.blit(self.graphic, screenRect, graphicRect)