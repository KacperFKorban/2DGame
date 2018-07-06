import pygame

class Player:
    def __init__(self, st):
        self.x = st.xChunks / 2
        self.y = st.yChunks / 2
        self.xIncrement = 0
        self.yIncrement = 0
    def update(self, st):
        pass

def goLeft(pl, st):
    pl.xIncrement -= st.chunkSize

def goRight(pl, st):
    pl.xIncrement += st.chunkSize

def goUp(pl, st):
    pl.yIncrement -= st.chunkSize

def goDown(pl, st):
    pl.yIncrement += st.chunkSize

def standLeft(pl, st):
    pl.xIncrement += st.chunkSize

def standRight(pl, st):
    pl.xIncrement -= st.chunkSize

def standUp(pl, st):
    pl.yIncrement += st.chunkSize

def standDown(pl, st):
    pl.yIncrement -= st.chunkSize
