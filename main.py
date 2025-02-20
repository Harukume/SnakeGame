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
        self.position = [new_head[0], new_head[1]]

#todo: collisions
class Fruit:
    def __init__(self):
        self.color = "white"
        self.width = None
        self.height = None
        self.exist = False

    def createFruit(self, width, height):
        self.width = random.randint(1, (width // 10) - 1) * 10
        self.height = random.randint(1, (height // 10) - 1) * 10
        self.exist = True


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.width, self.height), 10)

#todo: Score score change, save score

#todo: game over screen

class Score:
    def __init__(self):
        pygame.font.init()
        self.score_rect = None
        self.score_surface = None
        self.score_font = None
        self.score = 0
        self.color = "white"
        self.font = pygame.font.Font('SixtyfourConvergence.ttf', 24)
        self.size = 24
        self.position = [0, 0]
        self.score_text = ""

    def draw(self, screen):
        self.score_text = f"Score: {self.score}"

        self.score_surface = self.font.render(str(self.score_text), True, pygame.Color(self.color))
        self.score_rect = self.score_surface.get_rect(topleft=self.position)

        screen.blit(self.score_surface, self.position)

    def add_point(self):
        self.score += 1

    def ending_screen(self, width, height, screen):
        self.score_text = f"Game Over Score: {self.score}"
        self.score_surface = self.font.render(self.score_text, True, pygame.Color("white"))
        self.score_rect = self.score_surface.get_rect(midtop=[width/2, height/2])
        screen.blit(self.score_surface, self.score_rect)
def game_over(): #todo: save best score
    global running
    print("Game Over")

    window.screen.fill("black")
    score.ending_screen(window.width, window.height, window.screen)
    pygame.display.flip()

    time.sleep(2)
    pygame.quit()
    running = False

    quit()

#setting up game
window = Window(720, 480)
snake = Snake()
fruit = Fruit()
score = Score()
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

    if not fruit.exist:
        fruit.createFruit(window.width, window.height)

    fruit.draw(window.screen) #drawing fruit on every layer
    score.draw(window.screen) #drawing score

    #collisions with border #todo: add collision with tail
    if snake.position[0] > window.width or snake.position[0] < 0 or snake.position[1] > window.height or snake.position[1] < 0:
        game_over()

    if snake.position[0] <= fruit.width &  snake.position[1] <= fruit.height:
        score.add_point()
        fruit.createFruit(window.width, window.height)

    if running:
        pygame.display.flip() #refresh of layer

    window.clock.tick(60) #limit FPS to 60

#exit game
pygame.quit()