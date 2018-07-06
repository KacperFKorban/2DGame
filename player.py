import pygame

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0

def actionListener(player):
    in_put = pygame.event.pygame.event.poll
    if in_put.type != pygame.NOEVENT:
        action(in_put, player)

def actionActivist(event, player):
    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            goLeft(player)
        elif event.key == K_RIGHT:
            goRight(player)
        elif event.key == K_UP:
            goUp(player)
        elif event.key == K_DOWN:
            goDown(player)

def goLeft(player):
    pass

def goRight(player):
    pass

def goUp(player):
    pass

def goDown(player):
    pass