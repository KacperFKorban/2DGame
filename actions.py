import pygame

def actionListener(pl, st, mapa):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            st.runningFlag = False
        else:
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
        elif event.key == pygame.K_ESCAPE:
            st.menuFlag = True
        elif event.key == pygame.K_SPACE:
            checkInteraction(pl, npcs, st)
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            standLeft(pl, st, mapa)
        elif event.key == pygame.K_RIGHT:
            standRight(pl, st, mapa)
        elif event.key == pygame.K_UP:
            standUp(pl, st, mapa)
        elif event.key == pygame.K_DOWN:
            standDown(pl, st, mapa)

def checkInteraction(pl, npcs, st):
    if st.xToGo == 0 and st.yToGo == 0:
        direction = directionToVector(pl.graphicTabIterator)
        for npc in npcs:
            if mapa.x / st.chunkSize + pl.x + direction[0] == npc.x and mapa.y / st.chunkSize + pl.y + direction[1] == npc.y:
                npc.interact()

def directionToVector(d):
    if d == Direction.up:
        return (0,-1)
    elif d == Direction.down:
        return (0,1)
    elif d == Direction.right:
        return (1,0)
    elif d == Direction.left:
        return (-1,0)

def goLeft(pl, st, mapa):
    st.xMovement -= st.chunkSize

def goRight(pl, st, mapa):
    st.xMovement += st.chunkSize

def goUp(pl, st, mapa):
    st.yMovement -= st.chunkSize

def goDown(pl, st, mapa):
    st.yMovement += st.chunkSize

def standLeft(pl, st, mapa):
    st.xMovement += st.chunkSize

def standRight(pl, st, mapa):
    st.xMovement -= st.chunkSize

def standUp(pl, st, mapa):
    st.yMovement += st.chunkSize

def standDown(pl, st, mapa):
    st.yMovement -= st.chunkSize