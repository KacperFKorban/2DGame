import pygame

class Inventory:
    def __init__(self):
        self.backColor = (255,255,0)
        self.graphic = pygame.image.load("./images/maps/tiledbackground.png")
        self.eq = []
        self.sq = []

    def addItem(self, e):
        self.eq.append(e)

    def update(self, screen):
        screen.fill(self.backColor)

    def actionListener(self, pl, st):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                st.runningFlag = False
            else:
                self.actionActivist(event, pl, st)

    def actionActivist(self, event, pl, st):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                st.menuFlag = True
            elif event.key == pygame.K_i:
                st.inventoryFlag = False