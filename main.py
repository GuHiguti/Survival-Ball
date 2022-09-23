import imp


import sys
import pygame
pygame.init()

size = width_canva, height_canva = 500, 500
black = 0,0,0
white = 255,255,255
red = 255,0,0
green = 0,255,0
blue = 0,0,255

screen = pygame.display.set_mode(size)

pos_ball = x_ball,y_ball = 0,0
speed_ball = [1,1]

while 1:
    x_ball+=1
    y_ball+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    retang = pygame.draw.rect(screen,blue,(x_ball,y_ball,100,100))
    pygame.display.update()
