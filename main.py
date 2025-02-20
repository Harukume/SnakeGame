import pygame
import random # for random respawn of fruit
import time

#todo: make window
class Window:
    def __init__(self, width, height):  #pygame setup
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Snake Game")

#todo: make snake, movement, length increase,
class Snake:
    def __init__(self):
        #first four blocks of snake
        self.body = [[100,50], [90,50], [80,50], [70,50]] #list of segments [x,y]

        #default position
        self.position = [100,50]

        self.speed = 15 #snake speed

        #default direction of snake, he goes to right
        self.direction = "RIGHT"
        self.change_to = self.direction

#todo: make fruit, score change, save score
class Fruit:
    pass
#todo: collisions
#setting up window
window = Window(720, 480)
snake = Snake()
fruit = Fruit()
running = True
#gameloop

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #quit game with X
            running = False

    window.screen.fill("purple") #fill screen with color

    #setup here

    pygame.display.flip() #display work on screen


    window.clock.tick(60) #limit FPS to 60

#exit game
pygame.quit()