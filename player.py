import pygame
from settings import Settings

class Player:
    def __init__(self):
        self.x = st.xChunks / 2
        self.y = st.yChunks / 2
        self.xIncrement = 0
        self.yIncrement = 0

def goLeft(pl):
    pl.xIncrement = -st.chunkSize

def goRight(pl):
    pl.xIncrement = st.chunkSize

def goUp(pl):
    pl.yIncrement = -st.chunkSize

def goDown(pl):
    pl.yIncrement = st.chunkSize

