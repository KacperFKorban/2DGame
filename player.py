import pygame

class Player:
    def __init__(self, st):
        self.x = st.xChunks / 2 * st.chunkSize
        self.y = st.yChunks / 2 * st.chunkSize
        self.walkingX = 0
        self.walkingY = 0
        self.down = [
                        pygame.image.load('./Images/Sprite_scaled/front1.png'),
                        pygame.image.load('./Images/Sprite_scaled/front2.png'),
                        pygame.image.load('./Images/Sprite_scaled/front1.png'),
                        pygame.image.load('./Images/Sprite_scaled/front3.png')
                    ]
        self.up =   [
                        pygame.image.load('./Images/Sprite_scaled/back1.png'),
                        pygame.image.load('./Images/Sprite_scaled/back2.png'),
                        pygame.image.load('./Images/Sprite_scaled/back1.png'),
                        pygame.image.load('./Images/Sprite_scaled/back3.png')
                    ]
        self.left = [
                        pygame.image.load('./Images/Sprite_scaled/left1.png'),
                        pygame.image.load('./Images/Sprite_scaled/left2.png')
                    ]
        self.right =    [
                            pygame.image.load('./Images/Sprite_scaled/right1.png'),
                            pygame.image.load('./Images/Sprite_scaled/right2.png')
                        ]
        self.graphicIterator = -1
        self.graphicTab = self.down

    def animateHorizontally(self):
        if self.walkingX > 0:
            self.graphicTab = self.right
        else:
            self.graphicTab = self.left
        if self.graphicIterator == -1:
            self.graphicIterator = 0
        else:
            self.graphicIterator += 1
            self.graphicIterator %= len(self.graphicTab)
        self.walkingX = 0

    def animateVertically(self):
        if self.walkingY > 0:
            self.graphicTab = self.down
        else:
            self.graphicTab = self.up
        if self.graphicIterator == -1:
            self.graphicIterator = 0
        else:
            self.graphicIterator += 1
            self.graphicIterator %= len(self.graphicTab)
        self.walkingY = 0

    def update(self, st, screen):
        if self.walkingY != 0:
            self.animateVertically()
        elif self.walkingX != 0:
            self.animateHorizontally()
        elif st.xMovement != 0 or st.yMovement != 0:
            if st.yMovement > 0:
                self.graphicTab = self.down
            elif st.yMovement < 0:
                self.graphicTab = self.up
            elif st.xMovement > 0:
                self.graphicTab = self.right
            else:
                self.graphicTab = self.left
            self.graphicIterator = 0
        else:
            self.graphicIterator = -1
        if self.graphicIterator == -1:
            screen.blit(self.graphicTab[0], (self.x, self.y))
        else:
            screen.blit(self.graphicTab[self.graphicIterator], (self.x, self.y))