import player
import pygame

def actionListener(pl):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          runningFlag = False
        elif event.type != pygame.NOEVENT:
            actionActivist(event, pl)

def actionActivist(event, pl):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.goLeft(pl)
        elif event.key == pygame.K_RIGHT:
            player.goRight(pl)
        elif event.key == pygame.K_UP:
            player.goUp(pl)
        elif event.key == pygame.K_DOWN:
            player.goDown(pl)