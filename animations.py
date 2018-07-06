import pygame

def animateVertically(pl, st, tab, screen):
    direction = int(pl.xIncrement/50)
    distance = pl.xIncrement
    while pl.xIncrement != 0:
        screen.blit(tab[int(pl.xIncrement/st.animateWalkLength)%len(tab)], [pl.x, pl.y])
        pl.xIncrement -= direction
        pl.x += direction

def animateHorizontally(pl, st, tab, screen):
    direction = int(pl.yIncrement/50)
    distance = pl.yIncrement
    while pl.xIncrement != 0:
        screen.blit(tab[int(pl.yIncrement/st.animateWalkLength)%len(tab)], [pl.x, pl.y])
        pl.yIncrement -= direction
        pl.y += direction