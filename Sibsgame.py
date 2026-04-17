import pygame
import random
import os
pygame.mixer.init()

pygame.init()


#colours
white = (255,255,255)
red  = (255,10,0)
black = (0,0,0)
blue =(100,240,255)
col = (200,180,250)
green = (0,255,120)


#window
screen_width = 500
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))

# game title
pygame.display.set_caption("Sibs Snake")
pygame.display.update()



clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

def text_screen(text,color,x,y):
    screen_text = font.render(text , True , color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color,snk_list, snake_size):
    for x,y in snk_list:
       pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])



def welcome():
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play()
    exit_game = False
    while not exit_game:

        gameWindow.fill((black))
        text_screen("Welcome to sib's snake game", green, 60, 230)
        text_screen("Press Space Bar To Play", green, 90, 270)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    gameloop()
        pygame.display.update()
        clock.tick(60)

#game loop
def gameloop():
    # variables
    exit_game = False
    game_over = False
    snake_x = 250
    snake_y = 250
    snake_size = 20
    khana_size = 10
    fps = 30
    velocity_x = 0
    velocity_y = 0
    score = 0
    khana_x = random.randint(20,200)
    khana_y = random.randint(20, 200)

    snk_list = []
    snk_len = 1
    #check if file exists
    if(not os.path.exists("Highscore.txt")):
        with open("Highscore.txt","w") as f:
            f.write("0")

    with open("Highscore.txt", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open("Highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(black)
            text_screen("GAME OVER! Press Enter", red,80,250)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game =  True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                         velocity_x =  7
                         velocity_y = 0
                    pygame.mixer.music.load('move.mp3')
                    pygame.mixer.music.play()


                    if event.key == pygame.K_LEFT:
                         velocity_x = -7
                         velocity_y = 0
                    pygame.mixer.music.load('move.mp3')
                    pygame.mixer.music.play()

                    if event.key == pygame.K_DOWN:
                         velocity_y = 7
                         velocity_x = 0
                    pygame.mixer.music.load('move.mp3')
                    pygame.mixer.music.play()

                    if event.key == pygame.K_UP:
                         velocity_y = -7
                         velocity_x = 0
                    pygame.mixer.music.load('move.mp3')
                    pygame.mixer.music.play()

                    if event.key == pygame.K_q:
                        score+=10
                        snk_len+=1
            snake_x = snake_x  + velocity_x
            snake_y = snake_y + velocity_y

            if (abs(snake_x - khana_x)<15 and abs(snake_y - khana_y)<15):
                score += 10

                khana_x = random.randint(20, screen_width - 450)
                khana_y = random.randint(20, screen_height - 300)
                snk_len+=2
                pygame.mixer.music.load('food.mp3')
                pygame.mixer.music.play()

                if score>int(highscore):
                    highscore = score

            gameWindow.fill(black)

            text_screen("Score: " + str(score ) + "  High score: "+str(highscore), green, 5, 5)

            pygame.draw.rect(gameWindow,red,[khana_x,khana_y,khana_size,khana_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_len:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()


           # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow,green, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()

