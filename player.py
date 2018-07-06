import pygame
import animations

class Player:
    def __init__(self, st):
        self.x = st.xChunks / 2
        self.y = st.yChunks / 2
        self.xIncrement = 0
        self.yIncrement = 0

        self.down = [pygame.image.load('./Images/Sprite_scaled/front1.png'),
        pygame.image.load('./Images/Sprite_scaled/front2.png'),
        pygame.image.load('./Images/Sprite_scaled/front1.png'),
        pygame.image.load('./Images/Sprite_scaled/front3.png')]

        self.up = [pygame.image.load('./Images/Sprite_scaled/back1.png'),
        pygame.image.load('./Images/Sprite_scaled/back2.png'),
        pygame.image.load('./Images/Sprite_scaled/back1.png'),
        pygame.image.load('./Images/Sprite_scaled/back3.png')]

        self.left = [pygame.image.load('./Images/Sprite_scaled/left1.png'),
        pygame.image.load('./Images/Sprite_scaled/left2.png')]

        self.right = [pygame.image.load('./Images/Sprite_scaled/right1.png'),
        pygame.image.load('./Images/Sprite_scaled/right2.png')]

    def update(self, st, screen):
        if self.xIncrement > 0 and self.x + self.xIncrement < st.screenX:
            animations.animateHorizontally(self, st, self.right, screen)
        elif self.xIncrement < 0 and self.x + self.xIncrement > 0:
            animations.animateHorizontally(self, st, self.left, screen)
        elif self.yIncrement > 0 and self.y + self.yIncrement < st.screenY:
            animations.animateVertically(self, st, self.down, screen)
        elif self.yIncrement < 0 and self.y + self.yIncrement > 0:
            animations.animateVertically(self, st, self.up, screen)

        screen.blit(self.down[0], [self.x, self.y])