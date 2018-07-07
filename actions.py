import player
import pygame

def actionListener(pl, st, mapa):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          st.runningFlag = False
        elif event.type != pygame.NOEVENT:
            actionActivist(event, pl, st, mapa)

def actionActivist(event, pl, st, mapa):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            goLeft(pl, st, mapa)
        elif event.key == pygame.K_RIGHT:
            goRight(pl, st, mapa)
        elif event.key == pygame.K_UP:
            goUp(pl, st, mapa)
        elif event.key == pygame.K_DOWN:
            goDown(pl, st, mapa)
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            standLeft(pl, st, mapa)
        elif event.key == pygame.K_RIGHT:
            standRight(pl, st, mapa)
        elif event.key == pygame.K_UP:
            standUp(pl, st, mapa)
        elif event.key == pygame.K_DOWN:
            standDown(pl, st, mapa)

def goLeft(pl, st, mapa):
    st.xIncrement -= st.chunkSize

def goRight(pl, st, mapa):
    st.xIncrement += st.chunkSize

def goUp(pl, st, mapa):
    st.yIncrement -= st.chunkSize

def goDown(pl, st, mapa):
    st.yIncrement += st.chunkSize

def standLeft(pl, st, mapa):
    st.xIncrement += st.chunkSize

def standRight(pl, st, mapa):
    st.xIncrement -= st.chunkSize

def standUp(pl, st, mapa):
    st.yIncrement += st.chunkSize

def standDown(pl, st, mapa):
    st.yIncrement -= st.chunkSize