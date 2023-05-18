import pygame

class Snake:
    def __init__(self):

        self.position = [1000, 1000]
        self.tailQueue = []
        self.direction = "East"
        self.headColor = [0, 0, 255, 255]
        self.tailColor = [0, 255, 0, 255]
        self.windowWidth = 1980
        self.windowHeight = 1080

    def Move(self):

        match self.direction:
            
            case "North":
                self.tailQueue.append((self.position[0], self.position[1]))
                self.position[1] -= 10
                for tailPart in self.tailQueue:
                    if tailPart[0] == self.position[0] and tailPart[1] == self.position[1]:
                        return True
                    if self.position[1] < 0:
                        return True
            case "East":
                self.tailQueue.append((self.position[0], self.position[1]))
                self.position[0] += 10
                for tailPart in self.tailQueue:
                    if tailPart[0] == self.position[0] and tailPart[1] == self.position[1]:
                        return True
                    if self.position[0] > self.windowWidth - 10:
                        return True
            case "South":
                self.tailQueue.append((self.position[0], self.position[1]))
                self.position[1] += 10
                for tailPart in self.tailQueue:
                    if tailPart[0] == self.position[0] and tailPart[1] == self.position[1]:
                        return True
                    if self.position[1] > self.windowHeight - 10:
                        return True
            case "West":
                self.tailQueue.append((self.position[0], self.position[1]))
                self.position[0] -= 10
                for tailPart in self.tailQueue:
                    if tailPart[0] == self.position[0] and tailPart[1] == self.position[1]:
                        return True
                    if self.position[0] < 0:
                        return True
       

if __name__ == "__main__":
    print()
