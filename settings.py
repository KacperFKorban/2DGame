import pygame

class Settings:
    def __init__(self):
        self.screenWidth = 800
        self.screenHeight = 600
        self.runningFlag = True
        self.chunkSize = 50
        self.xChunks = self.screenWidth / self.chunkSize
        self.yChunks = self.screenHeight / self.chunkSize
        self.xMovement = 0
        self.yMovement = 0