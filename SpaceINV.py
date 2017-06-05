#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kirandeep
#
# Created:     19/05/2017
# Copyright:   (c) Kirandeep 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()
import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600)) #Screen Resolution

pygame.mouse.set_visible(0)  #Used to Hide Mouse Cursor

ship = pygame.image.load("images\ship.png") #Load Ship Sprite
ship_top = screen.get_height() -ship.get_height()
ship_left = screen.get_width()/2 - ship.get_width()/2 #Used to position Ship

screen.blit(ship, (ship_left,ship_top))

shot = pygame.image.load("images\laser.png") #Load Shot sprite

shoot_y = 0


while True:
    clock.tick(60) #Makes sure game stays at 60fps and doesn't speed up on different computers.
    screen.fill((0,0,0)) #Makes the screen black
    x,y = pygame.mouse.get_pos()
    screen.blit(ship,(x-ship.get_width()/2, ship_top))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  #Allows me to exit game
        elif event.type == MOUSEBUTTONDOWN:
            shoot_y = 500
            shoot_x = x
    if shoot_y > 0:
        screen.blit(shot, (shoot_x,shoot_y))
        shoot_y -= 10

    pygame.display.update()