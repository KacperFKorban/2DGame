import pygame

class Settings:
    def __init__(self):
        self.screenX = 800
        self.screenY = 600
        self.runningFlag = True
        self.chunkSize = 50
        self.xChunks = self.screenX / self.chunkSize
        self.yChunks = self.screenY / self.chunkSize
        self.animateHorizontalLength = 12
        self.animateVerticalLength = 7