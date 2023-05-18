import pygame
import random

class Food:
    def __init__(self):

        self.foodColor = [255, 0, 0, 255]
        self.foodPosition = (500, 500)
        self.windowWidth = 1920
        self.windowHeight = 1080



    def spawnFood(self):

        self.randX = random.randint(0, (self.windowWidth - 10)/10)  
        self.randY = random.randint(0, (self.windowHeight - 10)/10)

        self.randX *= 10
        self.randY *= 10

        self.foodPosition = [self.randX, self.randY]

       

    def eatFood(self, snakePos):

        if snakePos == self.foodPosition:
            self.spawnFood()
            return False
        else:
            return True
