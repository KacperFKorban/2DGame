import pygame
from enum import Enum
from inventory import Inventory

class Player:
    def __init__(self, st):
        self.x = st.xChunks / 2
        self.y = st.yChunks / 2
        self.walkingX = 0
        self.walkingY = 0
        self.direction = Direction.down
        self.graphics = [
                            [
                                pygame.image.load('./images/sprite_scaled/back1.png'),
                                pygame.image.load('./images/sprite_scaled/back2.png'),
                                pygame.image.load('./images/sprite_scaled/back1.png'),
                                pygame.image.load('./images/sprite_scaled/back3.png')
                            ],
                            [
                                pygame.image.load('./images/sprite_scaled/right1.png'),
                                pygame.image.load('./images/sprite_scaled/right2.png')
                            ],
                            [
                                pygame.image.load('./images/sprite_scaled/front1.png'),
                                pygame.image.load('./images/sprite_scaled/front2.png'),
                                pygame.image.load('./images/sprite_scaled/front1.png'),
                                pygame.image.load('./images/sprite_scaled/front3.png')
                            ],
                            [
                                pygame.image.load('./images/sprite_scaled/left1.png'),
                                pygame.image.load('./images/sprite_scaled/left2.png')
                            ]
                        ]    
        self.graphicIterator = -1
        self.graphicTabIterator = Direction.down
        self.inventory = Inventory()

    def animateHorizontally(self):
        if self.walkingX > 0:
            self.graphicTabIterator = Direction.right
        else:
            self.graphicTabIterator = Direction.left
        if self.graphicIterator == -1:
            self.graphicIterator = 0
        else:
            self.graphicIterator += 1
            self.graphicIterator %= len(self.graphics[self.graphicTabIterator.value])
        self.walkingX = 0

    def animateVertically(self):
        if self.walkingY > 0:
            self.graphicTabIterator = Direction.down
        else:
            self.graphicTabIterator = Direction.up
        if self.graphicIterator == -1:
            self.graphicIterator = 0
        else:
            self.graphicIterator += 1
            self.graphicIterator %= len(self.graphics[self.graphicTabIterator.value])
        self.walkingY = 0

    def update(self, st, screen):
        if self.walkingY != 0:
            self.animateVertically()
        elif self.walkingX != 0:
            self.animateHorizontally()
        elif st.xMovement != 0 or st.yMovement != 0:
            if st.yMovement > 0:
                self.graphicTabIterator = Direction.down
            elif st.yMovement < 0:
                self.graphicTabIterator = Direction.up
            elif st.xMovement > 0:
                self.graphicTabIterator = Direction.right
            else:
                self.graphicTabIterator = Direction.left
            self.graphicIterator = -1
        else:
            self.graphicIterator = -1
        if self.graphicIterator == -1:
            screen.blit(self.graphics[self.graphicTabIterator.value][0], (self.x * st.chunkSize, self.y * st.chunkSize))
        else:
            screen.blit(self.graphics[self.graphicTabIterator.value][self.graphicIterator], (self.x * st.chunkSize, self.y * st.chunkSize))

class Direction(Enum):
    up = 0
    right = 1
    down = 2
    left = 3