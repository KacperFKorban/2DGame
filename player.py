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
        self.graphic = self.down[0]

    def update(self, st, screen):
        if st.xIncrement > 0 and self.x + st.xIncrement < st.screenX:
            animations.animateHorizontally(self, st, self.right, screen)
        elif st.xIncrement < 0 and self.x + st.xIncrement > 0:
            animations.animateHorizontally(self, st, self.left, screen)
        elif st.yIncrement > 0 and self.y + st.yIncrement < st.screenY:
            animations.animateVertically(self, st, self.down, screen)
        elif st.yIncrement < 0 and self.y + st.yIncrement > 0:
            animations.animateVertically(self, st, self.up, screen)

        screen.blit(self.down[0], [self.x, self.y])