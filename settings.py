import pygame

class Settings:
    def __init__(self):
        self.screenWidth = 800
        self.screenHeight = 600
        self.runningFlag = True
        self.chunkSize = 50
        self.xChunks = screenWidth / chunkSize
        self.yChunks = screenHeight / chunkSize