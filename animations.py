import pygame

def animateVertically(pl, st, tab, screen):
    direction = int(st.xIncrement/50)
    distance = st.xIncrement
    while st.xIncrement != 0:
        screen.blit(tab[int(st.xIncrement/st.animateWalkLength)%len(tab)], (pl.x, pl.y))
        st.xIncrement -= direction
        pl.x += direction

def animateHorizontally(pl, st, tab, screen):
    direction = int(st.yIncrement/50)
    distance = st.yIncrement
    while st.yIncrement != 0:
        screen.blit(tab[int(st.yIncrement/st.animateWalkLength)%len(tab)], (pl.x, pl.y))
        st.yIncrement -= direction
        pl.y += direction