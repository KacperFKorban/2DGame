import pygame

class Settings:
    def __init__(self):
        self.screenX = 800
        self.screenY = 600
        self.runningFlag = True
        self.chunkSize = 50
        self.xChunks = self.screenX / self.chunkSize
        self.yChunks = self.screenY / self.chunkSize
        self.xMovement = 0
        self.yMovement = 0
        self.animateWalkLength = 7
        self.xIncrement = 0
        self.yIncrement = 0