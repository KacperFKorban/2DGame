import pygame

class Menu:
    def __init__(self):
        self.backColor = (255, 255, 255)
        self.optionHighlighted = 0
        self.font = pygame.font.Font("./fonts/SFPixelate-BoldOblique.ttf", 72)
        self.text = self.font.render("Hello, World", True, (0, 0, 0))

    def update(self, screen):
        screen.fill(self.backColor)
        screen.blit(self.text, (0, 0))

    def actionListener(self, st):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                st.runningFlag = False
            elif event.type != pygame.NOEVENT:
                self.actionActivist(event, st)

    def actionActivist(self, event, st):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                if self.optionHighlighted == 0:
                    st.menuFlag = False
            elif event.key == pygame.K_DOWN:
                self.optionHighlighted += 1

            elif event.key == pygame.K_UP:
                self.optionHighlighted -= 1