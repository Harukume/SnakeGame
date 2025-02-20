import pygame
import random # for random respawn of fruit
import time


class Window:
    def __init__(self, width, height):  #pygame setup
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Snake Game")

#todo: length increase
class Snake:
    def __init__(self):
        #first four blocks of snake
        self.body = [[100,50], [90,50], [80,50], [70,50]] #list of segments [x,y]

        #default position
        self.position = [100,50]

        self.speed = 2 #snake speed

        #default direction of snake, he goes to right
        self.direction = "RIGHT"
        self.change_to = self.direction


    def move(self):
        #check if direction can be changed for i.e. you cant go down if you are going up

        if self.change_to == "RIGHT" and self.direction != "LEFT":
            self.direction =  "RIGHT"
        if self.change_to == "LEFT" and self.direction != "RIGHT":
            self.direction =  "LEFT"
        if self.change_to == "UP" and self.direction != "DOWN":
            self.direction =  "UP"
        if self.change_to == "DOWN" and self.direction != "UP":
            self.direction =  "DOWN"

        #snake movement
        if self.direction == "RIGHT":
            new_head = [self.body[0][0] + self.speed, self.body[0][1]]
        if self.direction == "LEFT":
            new_head = [self.body[0][0] - self.speed, self.body[0][1]]
        if self.direction == "UP":
            new_head = [self.body[0][0], self.body[0][1]  - self.speed]
        if self.direction == "DOWN":
            new_head = [self.body[0][0], self.body[0][1]  + self.speed]


        self.body.insert(0, new_head) #add on 0 index new direction
        self.body.pop() #cut last piece of tail to maintain length

#todo: make fruit, collisions
class Fruit:
    pass

#todo: Score score change, save score
#setting up game
window = Window(720, 480)
snake = Snake()
fruit = Fruit()
running = True

while running: #game loop

    #event listeners for arrows and exit button
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_to = "UP"
            if event.key == pygame.K_DOWN:
                snake.change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                snake.change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                snake.change_to = "RIGHT"
        if event.type == pygame.QUIT:  #quit game with X
            running = False

    window.screen.fill("purple") #fill screen with color


    snake.move()
    #setup here
    for pos in snake.body:
        pygame.draw.rect(window.screen, "green", pygame.Rect(pos[0], pos[1], 20, 20) ) # (x,y, width, height)

    pygame.display.flip() #display work on screen

    pygame.display.update()

    window.clock.tick(60) #limit FPS to 60

#exit game
pygame.quit()