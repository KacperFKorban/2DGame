import pygame

class Menu:
    def __init__(self):
        self.backColor = (255, 255, 255)
        self.optionHighlighted = 0
        self.font = pygame.font.Font("./fonts/SFPixelate-BoldOblique.ttf", 36)
        self.menuTexts =["New Game", "Load Game", "Settings", "Credits", "Quit"]
        

    def update(self, screen, st):
        screen.fill(self.backColor)
        self.menuBlit(screen, st)

    def actionListener(self, st):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                st.runningFlag = False
            else:
                self.actionActivist(event, st)

    def actionActivist(self, event, st):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and st.startedFlag:
                st.menuFlag = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                if self.optionHighlighted == 0:
                    st.menuFlag = False
                    st.startedFlag = True
            elif event.key == pygame.K_DOWN:
                self.optionHighlighted += 1
            elif event.key == pygame.K_UP:
                self.optionHighlighted -= 1

    def menuBlit(self, screen, st):
        height = 90
        for iterator in range( len( self.menuTexts )):
            if self.optionHighlighted == iterator:
                text = self.font.render(self.menuTexts[iterator], True, (255, 0, 0))
            else:
                text = self.font.render(self.menuTexts[iterator], True, (0, 255, 0))
            screen.blit(text, (st.screenX // 2 - text.get_width(), height))
            height = height + 40


#
#    def textOff(self, text):
#        return self.font.render(text, True, (0, 255, 0))
#
#    def textOn(self, text):
#        return self.font.render(text, True, (255, 0, 0))
#