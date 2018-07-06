import pygame

class Settings:
    def __init__(self):
        self.screenX = 800
        self.screenY = 600
        self.runningFlag = True
        self.chunkSize = 50
        self.xChunks = self.screenX / self.chunkSize
        self.yChunks = self.screenY / self.chunkSize
<<<<<<< HEAD
        self.xMovement = 0
        self.yMovement = 0
        self.animateWalkLength = 7
=======
        self.animateHorizontalLength = 12
        self.animateVerticalLength = 7
>>>>>>> 897f21717b3acf736d06f3c7a00e4ef166319c99
