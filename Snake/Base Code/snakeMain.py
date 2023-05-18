import pygame
from snakeClass import Snake
from foodClass import Food

def main():

    pygame.display.init()
    pygame.font.init()
    
    windowWidth = 1920
    windowHeight = 1080
    window = pygame.display.set_mode((windowWidth, windowHeight))
    windowColor = [255, 255, 255, 255]   
    window.fill(windowColor)
    
    clock = pygame.time.Clock()
    
    score = 0
    snake = Snake()
    food = Food()
    moveBuffer = 2
    running = True


    pygame.display.update()

    food.spawnFood()
    pygame.draw.rect(window, snake.headColor, [snake.position, [10, 10]])

    while running:
        pygame.display.update()
        window.fill(windowColor)
        clock.tick(60)
        if moveBuffer == 0:
            if snake.Move() == True:
                endFont = pygame.font.SysFont("Impact", 50)
                endText = endFont.render("Game Over", True, (255,255, 0))
                endTextRect = endText.get_rect()
                endTextRect.center = (windowWidth/2, windowHeight/2)
                window.blit(endText, endTextRect)
                
                scoreFont = pygame.font.SysFont("Impact", 25)
                scoreText = scoreFont.render("Score: {0}".format(score), True, (255, 255, 0))
                scoreTextRect = scoreText.get_rect()
                scoreTextRect.center = (windowWidth/2, windowHeight/2 + 40)
                window.blit(scoreText, scoreTextRect)

                menuFont = pygame.font.SysFont("Impact", 20)
                menuText = menuFont.render("Press escape to Quit, Press R restart", True, (255, 255, 0))
                menuTextRect = menuText.get_rect()
                menuTextRect.center = (windowWidth/2, windowHeight/2 + 75)
                window.blit(menuText, menuTextRect)
                pygame.display.update()
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_ESCAPE]:
                                running = False
                            if keys[pygame.K_r]:
                                main()
                
            moveBuffer = 2
            foodNotEaten = food.eatFood(snake.position)
            if foodNotEaten:
                snake.tailQueue.pop(0)
            else:
                
                score += 1
                
        else:
            moveBuffer -= 1
        pygame.draw.rect(window, food.foodColor, [food.foodPosition, [10, 10]])
        pygame.draw.rect(window, snake.headColor, [snake.position, [10, 10]])
        for tailPart in snake.tailQueue:
            pygame.draw.rect(window, snake.tailColor, [tailPart, [10, 10]])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    running = False
                if keys[pygame.K_w]:
                    snake.direction = "North"
                if keys[pygame.K_a]:
                    snake.direction = "West"
                if keys[pygame.K_s]:
                    snake.direction = "South"
                if keys[pygame.K_d]:
                    snake.direction = "East"
                
    

    #pygame.quit()
         

    """
    Initialize pygame's display and font functions
    """
    

   

    """
                !!! DO THIS LATER !!!
                
                Delete pygame.quit()
                
                create variables for endFont, endText, and endTextRect
                
                Set endFont equal to a pygame Font, giving it a font type to use and a font size
                Set endText equal to the rendered endFont, giving it "Game Over" as input for the string
                Set endTextRect equal to the rectangle from endText
                Then, set the center of endTextRect to half the windowWidth and a quarter of the windowHeight
                
                Repeat this process for scoreFont and menuFont
                
                Update the display

              
            Otherwise:
                Increase score by 1
                Update the display caption to reflect the new score
                (Note: Use 'Your Caption Here {0}'.format(score) to do this easily)
                (Note: The {0} will be replaced by whatever is inside format())
    """


  

    """
    Inside the !!! DO THIS LATER !!! part:
        Create an endFont, scoreFont, and menuFont variables
        ...
    """
    
if __name__ == "__main__":
    main()
