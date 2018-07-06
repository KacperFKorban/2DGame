import pygame

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xIncrement = 0
        self.yIncrement = 0

def goLeft(pl):
    pl.xIncrement = -1

def goRight(pl):
    pl.xIncrement = 1

def goUp(pl):
    pl.yIncrement = -1

def goDown(pl):
    pl.yIncrement = 1

