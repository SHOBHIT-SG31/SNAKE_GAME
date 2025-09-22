import pygame
import time
import random

pygame.init()
red = (255,0,0)
blue = (51,153,255)
grey = (192,192,192)
green = (51,102,0)

win_width=600
win_height=400
window = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Snake Game")
time.sleep(1)

snake = 10
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("calibri",26)
score_font = pygame.font.SysFont("comicsansms",30)
# fonts = pygame.font.get_fonts()
# print(fonts)
def user_score(score):
    number = score_font.render("Score: "+ str(score),True,red)
    window.blit(number,[0,0])

def game_snake(snake,snake_length_list):
    for x in snake_length_list:
        pygame.draw.rect(window,green,[x[0],x[1],snake,snake])

def message(msg):
    mesg = font_style.render(msg,True,red)
    window.blit(mesg,[win_width/6,win_height/3])
def game_loop():
    gameOver = False
    gameClose = False

    x1 = win_width/2
    y1 = win_height/2
     
    x1_change=0
    y1_change=0
    
    
    snake_length_list=[]
    snake_length=1

    foodx = round(random.randrange(0, win_width - snake)/10.0)*10.0
    foody = round(random.randrange(0, win_height - snake)/10.0)*10.0

    while not gameOver:
        while gameClose == True:
            window.fill(grey)
            message("You lost!! press P to play again and press Q to quit the game")
            user_score(snake_length-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False

                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake
        
        if x1>=win_width or x1<0 or y1>=win_height or y1<0 :
            gameClose = True
        
        x1 += x1_change
        y1 += y1_change
        window.fill(grey)
        pygame.draw.rect(window,red,[foodx,foody,snake,snake])
        snake_head = [x1, y1]
        snake_length_list.append(snake_head)
        if len(snake_length_list)>snake_length:
            del snake_length_list[0]

        for segment in snake_length_list[:-1]:
            if segment == snake_head:
                gameClose = True

        game_snake(snake,snake_length_list)
        user_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx or y1 == foody :
            foodx = round(random.randrange(0, win_width - snake)/10.0)*10.0
            foody = round(random.randrange(0, win_height - snake)/10.0)*10.0
            snake_length += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()

game_loop()

# import pygame
# import time
# import random

# # Initialize Pygame
# pygame.init()

# # Colors
# red = (255, 0, 0)
# blue = (51, 153, 255)
# grey = (192, 192, 192)
# green = (51, 102, 0)

# # Window setup
# win_width = 600
# win_height = 400
# window = pygame.display.set_mode((win_width, win_height))
# pygame.display.set_caption("Snake Game")
# time.sleep(1)

# # Snake settings
# snake_block = 10
# snake_speed = 15

# clock = pygame.time.Clock()

# # Fonts
# font_style = pygame.font.SysFont("calibri", 26)
# score_font = pygame.font.SysFont("comicsansms", 30)

# # Score display
# def user_score(score):
#     value = score_font.render("Score: " + str(score), True, red)
#     window.blit(value, [0, 0])

# # Draw snake
# def game_snake(snake_block, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])

# # Message display
# def message(msg):
#     mesg = font_style.render(msg, True, red)
#     window.blit(mesg, [win_width / 6, win_height / 3])

# # Main game loop
# def game_loop():
#     game_over = False
#     game_close = False

#     x1 = win_width / 2
#     y1 = win_height / 2

#     x1_change = 0
#     y1_change = 0

#     snake_list = []
#     snake_length = 1

#     foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0

#     while not game_over:

#         while game_close:
#             window.fill(grey)
#             message("You lost! Press P to play again or Q to quit.")
#             user_score(snake_length - 1)
#             pygame.display.update()

#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_p:
#                         game_loop()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     x1_change = 0
#                     y1_change = -snake_block
#                 elif event.key == pygame.K_DOWN:
#                     x1_change = 0
#                     y1_change = snake_block

#         # Boundary check
#         if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
#             game_close = True

#         x1 += x1_change
#         y1 += y1_change
#         window.fill(grey)
#         pygame.draw.rect(window, red, [foodx, foody, snake_block, snake_block])

#         snake_head = [x1, y1]
#         snake_list.append(snake_head)

#         if len(snake_list) > snake_length:
#             del snake_list[0]

#         # Self collision
#         for segment in snake_list[:-1]:
#             if segment == snake_head:
#                 game_close = True

#         game_snake(snake_block, snake_list)
#         user_score(snake_length - 1)

#         pygame.display.update()

#         # Food collision
#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
#             foody = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0
#             snake_length += 1

#         clock.tick(snake_speed)

#     pygame.quit()
#     quit()

# # Start the game
# game_loop()