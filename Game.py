#import modules

import pygame

import random

import time


def generate_apple():
    apple_x = random.randint(0,49) * 10
    apple_y = random.randint(0,49) * 10
    return apple_x, apple_y
def draw_apple(apple_x, apple_y):
    pygame.draw.rect(display, apple_color, pygame.Rect(apple_x, apple_y,10,10))
    
    
def collision_with_apple(snake_head, apple_x, apple_y, grow):
    if snake_head[0] == apple_x and snake_head[1] == apple_y:
        apple_x, apple_y = generate_apple()
        grow = False
    return apple_x, apple_y, grow

    


def collision_with_bounderies(snake_head):
    if snake_head[0] >= display_width or snake_head[0] < 0 or snake_head[1] >= display_height or snake_head[1] < 0:
        return 1
    return 0

def collision_with_self(snake_head, snake_position):
    for position in snake_position[1:]:
        if position[0] == snake_head[0] and position[1] == snake_head[1]:
            return 1

def generate_snake(snake_head, snake_position, button_direction, grow):

    #uses button_direction to decide where snake head will go
    if button_direction == 0:
        snake_head[0] += 10
    elif button_direction == 1:
        snake_head[0] -= 10 
    elif button_direction == 2:
        snake_head[1] += 10 
    elif button_direction == 3:
        snake_head[1] -= 10
    snake_position.insert(0,list(snake_head))
    if grow == True:
        snake_position.pop()
    
    return snake_position

def display_snake(snake_position):

    #uses list of snake's positions to display snake
    for position in snake_position:
        pygame.draw.rect(display, player_color, pygame.Rect(position[0],position[1],10,10))
        
def play_game(snake_head, snake_position, button_direction):

    crashed = False
    apple_x, apple_y = generate_apple()
    grow = True
    
    while crashed is not True:

        for event in pygame.event.get():

            #ends game if you click on X
            if event.type == pygame.QUIT:
                crashed = True

            #sets variable used to move snake using arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    button_direction = 0
                elif event.key == pygame.K_LEFT:
                    button_direction = 1
                elif event.key == pygame.K_DOWN:
                    button_direction = 2
                elif event.key == pygame.K_UP:
                    button_direction = 3                
                
            
        #moves snake position
        snake_position = generate_snake(snake_head, snake_position, button_direction, grow)
        grow = True
        

        #display background and snake
        display.fill(window_color)
        display_snake(snake_position)
        draw_apple(apple_x, apple_y)
        pygame.display.update()
        

        #ends game loop if snake leaves the boundary
        if collision_with_bounderies(snake_head) == 1:
            crashed = True
        if collision_with_self(snake_head,snake_position) == 1:
            crashed = True 
        apple_x, appple_y, grow = collision_with_apple(snake_head,apple_x,apple_y, grow)
    


        clock.tick(20)



if __name__ == "__main__":

    # set variables

    display_width = 500

    display_height = 500

    player_color = (250,247,249)

    window_color = (132,194,173)
    
    apple_color = (130,53,53)

    clock=pygame.time.Clock()

    

    #create the snake

    snake_head = [250,250]

    snake_position = [[250,250],[240,250],[230,250]]



    #initialize pygame modules    

    pygame.init()

    

    #display game window

    display = pygame.display.set_mode((display_width,display_height))

    display.fill(window_color)

    pygame.display.set_caption("Snake Game")

    pygame.display.update()

    

    #start the game loop

    play_game(snake_head, snake_position, 0)



    pygame.quit()
