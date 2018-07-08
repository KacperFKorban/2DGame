import pygame
import animations

class Player:
    def __init__(self, st):
        self.x = st.xChunks / 2 * st.chunkSize
        self.y = st.yChunks / 2 * st.chunkSize
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
        self.graphicIterator = 0
        self.graphicTab = self.down

    def animateHorizontally(self, st, tab, screen):
        pass

    def animateVertically(self, st, tab, screen):
        pass

    def update(self, st, screen):
        screen.blit(self.down[0], (self.x, self.y))