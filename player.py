import pygame

class Player:
    def __init__():
        self.x = 0
        self.y = 0

def actionListener(Player player):
    pygame.event.Event in_put = pygame.event.pygame.event.poll
    if in_put.type != pygame.NOEVENT:
        action(in_put, player)

def actionActivist(pygame.event.Event event, Player player):
    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            goLeft(player)
        elif event.key == K_RIGHT:
            goRight(player)
        elif event.key == K_UP:
            goUp(player)
        elif event.key == K_DOWN:
            goDown(player)

def goLeft(Player player):
    pass

def goRight(Player player):
    pass

def goUp(Player player):
    pass

def goDOwn(Player player):
    pass