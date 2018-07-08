import pygame

def animateVertically(pl, st, tab, screen):
    direction = int(st.xMovement / 50)
    distance = st.xMovement
    while st.xMovement != 0:
        screen.blit(tab[int(st.xMovement / st.animateWalkLength) % len(tab)], (pl.x, pl.y))
        st.xMovement -= direction
        pl.x += direction

def animateHorizontally(pl, st, tab, screen):
    direction = int(st.yMovement / 50)
    distance = st.yMovement
    while st.yMovement != 0:
        screen.blit(tab[int(st.yMovement / st.animateWalkLength) % len(tab)], (pl.x, pl.y))
        st.yMovement -= direction
        pl.y += direction