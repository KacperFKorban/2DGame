import pygame

class Player:
    def __init__(self, st):
        self.x = st.xChunks / 2
        self.y = st.yChunks / 2
        self.xIncrement = 0
        self.yIncrement = 0

        down = [pygame.image.load('./Images/Sprite_scaled/front1.png'),
        pygame.image.load('./Images/Sprite_scaled/front2.png'),
        pygame.image.load('./Images/Sprite_scaled/front3.png')]

        up = [pygame.image.load('./Images/Sprite_scaled/back1.png'),
        pygame.image.load('./Images/Sprite_scaled/back2.png'),
        pygame.image.load('./Images/Sprite_scaled/back3.png')]

        left = [pygame.image.load('./Images/Sprite_scaled/left1.png'),
        pygame.image.load('./Images/Sprite_scaled/left2.png')]

        right = [pygame.image.load('./Images/Sprite_scaled/right1.png'),
        pygame.image.load('./Images/Sprite_scaled/right2.png')]

    def update(self, st, screen):
        if self.xIncrement > 0 and self.x + self.xIncrement < st.screenWidth:
            animateHorizontally(self, st, right)
        elif self.xIncrement < 0 and self.x + self.xIncrement > 0:
            animateHorizontally(self, st, left)
        elif self.yIncrement > 0 and self.y + self.yIncrement < st.screenHeight:
            animateVertically(self, st, down)
        elif self.yIncrement < 0 and self.y + self.yIncrement > 0:
            animateVertically(self, st, up)
            
        screen.blit(front1, [self.x, self.y])