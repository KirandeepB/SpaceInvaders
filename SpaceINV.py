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

enemy_x = 50
enemy_change_x = 0.75
a=0
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600)) #Screen Resolution

pygame.mouse.set_visible(0)  #Used to Hide Mouse Cursor

ship = pygame.image.load("images\ship.png") #Load Ship Sprite
ship_top = screen.get_height() -ship.get_height()
ship_left = screen.get_width()/2 - ship.get_width()/2 #Used to position Ship

screen.blit(ship, (ship_left,ship_top))

enemy1 = pygame.image.load("images\enemy1.png") #Load enemy sprite
enemy2 = pygame.image.load("images\enemy2.png") #Load enemy sprite
enemy3 = pygame.image.load("images\enemy3.png") #Load enemy sprite
shot = pygame.image.load("images\laser.png") #Load Shot sprite

shoot_y = 0
n=0




while True:
    clock.tick(60) #Makes sure game stays at 60fps and doesn't speed up on different computers.
    screen.fill((0,0,0)) #Makes the screen black
    x,y = pygame.mouse.get_pos()
    screen.blit(ship,(x-ship.get_width()/2, ship_top))
    screen.blit(enemy,(enemy_x+50, 100))
    screen.blit(enemy,(enemy_x+130, 100))
    screen.blit(enemy,(enemy_x+210, 100))
    screen.blit(enemy,(enemy_x+290, 100))
    screen.blit(enemy,(enemy_x+370, 100))
    screen.blit(enemy,(enemy_x+450, 100))
    screen.blit(enemy,(enemy_x+50, 160))
    screen.blit(enemy,(enemy_x+130, 160))
    screen.blit(enemy,(enemy_x+210, 160))
    screen.blit(enemy,(enemy_x+290, 160))
    screen.blit(enemy,(enemy_x+370, 160))
    screen.blit(enemy,(enemy_x+450, 160))
    screen.blit(enemy,(enemy_x+50, 210))
    screen.blit(enemy,(enemy_x+130, 210))
    screen.blit(enemy,(enemy_x+210, 210))
    screen.blit(enemy,(enemy_x+290, 210))
    screen.blit(enemy,(enemy_x+370, 210))
    screen.blit(enemy,(enemy_x+450, 210))
    enemy_change_x = enemy_change_x * -1
    enemy_x += enemy_change_x
    if enemy_x > 0:
        enemy_change_x = enemy_change_x * -1
    if enemy_x >= 280:
        enemy_change_x = enemy_change_x * -1



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  #Allows me to exit game
        elif event.type == MOUSEBUTTONDOWN:
            shoot_y = 500
            shoot_x = x
    if shoot_y > 0:
                screen.blit(shot, (shoot_x,shoot_y))
                shoot_y -= 10

    pygame
    pygame.display.update()