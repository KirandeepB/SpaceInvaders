#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kirandeep
#
# Created:     06/06/2017
# Copyright:   (c) Kirandeep 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import pygame
import random
from os import path
s=0
img_dir = path.join(path.dirname(__file__),'img')

WIDTH = 800
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
n=0
b=0
k=0
p=0
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders!")
clock = pygame.time.Clock()
FONT = "fonts/space_invaders.ttf"
def draw_text(surf,text, size, x, y):
    font = pygame.font.Font(FONT,size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop= (x,y)
    surf.blit(text_surface, text_rect)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img,(65,62))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx= -5
        if keystate[pygame.K_RIGHT]:
            self.speedx= +5
        self.rect.x +=self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left  < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img,(5,15))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y +=self.speedy
        if self.rect.bottom <0:
            self.kill()


class enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(enemy_img,(39,38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 70 + n +k+b+p
        self.rect.y = 100 +s
        self.speedy = 1
    def update(self):
        self.rect.x +=self.speedy
        if self.rect.top > HEIGHT +10:
            self.rect.x = 50 + n +k+b+p
            self.rect.y = 100+s
            self.speedy = 1
        self.rect.x +=self.speedy
        if self.rect.right > 800:
            self.rect.right = 0
        if self.rect.left  < 0:
            self.rect.left = 0
class meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(meteor_img,(55,55))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(1,8)

    def update(self):

        self.rect.y += self.speedy
        if self.rect.top > HEIGHT +10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)



background = pygame.image.load(path.join(img_dir, "star.png")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "ship.png")).convert()
enemy_img = pygame.image.load(path.join(img_dir, "enemy1.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laser.png")).convert()
meteor_img = pygame.image.load(path.join(img_dir, "red.png")).convert()

all_sprites = pygame.sprite.Group()

enemies = pygame.sprite.Group()
meteors = pygame.sprite.Group()
bullets=pygame.sprite.Group()
player=Player()

all_sprites.add(player)

for i in range(7):
    j = meteor()
    all_sprites.add(j)
    meteors.add(j)

for i in range(10):
    m=enemy()
    all_sprites.add(m)
    enemies.add(m)
    n=n+63
    o= n+30
    p=0
    k=0
    b=0
for l in range(10):
    f=enemy()
    all_sprites.add(f)
    enemies.add(f)
    k=k+63
    n=0
    b=0
    p=0
    o= n+30
    s = 50
for t in range(10):
    q=enemy()
    all_sprites.add(q)
    enemies.add(q)
    b=b+63
    o= b+30
    s = 100
    p=0
    n=0
    k=0
for r in range(10):
    h=enemy()
    all_sprites.add(h)
    enemies.add(h)
    p=p+63
    o= p+30
    s = 150
    n=0
    k=0
    b=0
score =0
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type== pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()


    # Update
    all_sprites.update()

    hits = pygame.sprite.groupcollide(enemies, bullets, True,True)
    for hit in hits:
        score+= 50

    hits2 = pygame.sprite.spritecollide(player,meteors,False)
    if hits2:
        running = False


    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH/2, 10)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()