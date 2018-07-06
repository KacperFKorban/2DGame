import player
import pygame

def actionListener(pl, st):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          st.runningFlag = False
        elif event.type != pygame.NOEVENT:
            actionActivist(event, pl, st)

def actionActivist(event, pl, st):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.goLeft(pl, st)
        elif event.key == pygame.K_RIGHT:
            player.goRight(pl, st)
        elif event.key == pygame.K_UP:
            player.goUp(pl, st)
        elif event.key == pygame.K_DOWN:
            player.goDown(pl, st)
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            player.standLeft(pl, st)
        elif event.key == pygame.K_RIGHT:
            player.standRight(pl, st)
        elif event.key == pygame.K_UP:
            player.standUp(pl, st)
        elif event.key == pygame.K_DOWN:
            player.standDown(pl, st)

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