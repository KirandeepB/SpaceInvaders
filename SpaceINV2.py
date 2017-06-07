#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kirandeep
#
# Created:     05/06/2017
# Copyright:   (c) Kirandeep 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import pygame
from pygame.locals import *
import sys
import random

class Player:

    def __init__(self):
        self.player = pygame.image.load("assets/shooter.png").convert()