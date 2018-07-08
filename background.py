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
        if st.xToGo != 0 or isXValid(self.x, st.xMovement, self.xSize, st):
            if st.xToGo == 0:
                st.xToGo = st.xMovement
            if st.xToGo != 0:
                self.x += st.xStep * sgn(st.xToGo)
                st.xToGo -= st.xStep * sgn(st.xToGo)
        if st.yToGo != 0 or isYValid(self.y, st.yMovement, self.ySize, st):
            if st.yToGo == 0:
                st.yToGo = st.yMovement
            if st.yToGo != 0:
                self.y += st.yStep * sgn(st.yToGo)
                st.yToGo -= st.yStep * sgn(st.yToGo)
        graphicRect = (self.x, self.y, self.x+st.screenX, self.y+st.screenY)
        screenRect = (0, 0, st.screenX, st.screenY)
        screen.blit(self.graphic, screenRect, graphicRect)

def isXValid(x, xi, xSize, st):
    if x+xi < 0:
        return False
    if x+xi+st.screenX > xSize:
        return False
    return True

def isYValid(y, yi, ySize, st):
    if y+yi < 0:
        return False
    if y+yi+st.screenY > ySize:
        return False
    return True

def isValid(x, y, xi, yi, xSize, ySize, st):
    return isXValid(x, xi, xSize, st) and isYValid(y, yi, ySize, st)

def sgn(a):
    if a == 0:
        return 0
    if a > 0:
        return 1
    else:
        return -1