
# Modification date: Fri Sep  2 22:35:46 2022

# Production date: Sun Sep  3 15:43:58 2023

import pygame, sys, time
from PIL import Image
from random import randint
from random import random
from pygame.locals import *
import os


pygame.init()

monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

win = pygame.display.set_mode((monitor_size[0], monitor_size[1]))

background = Image.open("background.jpg")
background = background.resize((monitor_size[0], monitor_size[1]))
background.save("background.png")
#print(background.size)
#print(5/0)

background = pygame.image.load("background.png")


#pygame.mixer.music.load('rain_long.wav')
pygame.mixer.Channel(0).play(pygame.mixer.Sound('rain.mp3'), -1)
#pygame.mixer.music.load('guts_theme.mp3')
pygame.mixer.Channel(1).play(pygame.mixer.Sound('music.mp3'), -1)
#pygame.mixer.Channel(1).stop()

class Raindrop:
    def __init__(self, colour, w, h):
        self.x = randint(0, width + height)
        self.y = randint(-height, -h)
        self.vel = randint(height//27, height//18)
        self.colour = colour
        self.w = w
        self.h = h
    
    def fall(self, dt, width, height):
        if self.y > height + self.h * 5:
            self.y = randint(-width, -self.h)
            self.x = randint(0, width + height)
            self.vel = randint(height//40, height//30)#(height//27, height//18)
            #if self.w == 1:
                #self.vel = randint(height//27, height//18)
            return
        self.y += self.vel * dt
        self.x -= (self.vel//4) * dt
    
    def draw(self, win):
        pygame.draw.line(win, self.colour, (self.x + self.w, self.y), (self.x, self.y + self.h))
        #for i in range(5):
            #pygame.draw.rect(win, (self.colour[0] - (i * 10), self.colour[1] - (i * 10), self.colour[2] - (i * 10)), pygame.Rect(self.x + (self.w) * i, self.y - (i * self.h), self.w, self.h))
        

raindrops = []
for i in range(width//5):#20
    #vel = randint(height//27, height//18)
    raindrops.append(Raindrop((120, 150, 170), 4, 16))
    #vel = randint(height//13, height/9)
    #daw = random()
    #dah = randint(2, 8)
    #raindrops.append(Raindrop(vel, (170, 200, 220), 1, dah))



font = pygame.font.Font('ABeeZee-Regular.otf', 10)


fullscreen = True
clock = pygame.time.Clock()
fps = 75
last_time = time.time()
daw, dah = width, height
running = True
while running:
    clock.tick(fps)
    #win.fill((0, 0, 0))
    dt = time.time() - last_time
    dt *= fps
    last_time = time.time()
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if event.type == VIDEORESIZE:
            if not fullscreen:
                win = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                daw, dah = event.w, event.h
                background = Image.open("background.jpg")
                background = background.resize((event.w, event.h))
                background.save("background.png")
                background = pygame.image.load("background.png").convert()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_f:
                width, height = monitor_size[0], monitor_size[1]
                fullscreen = not fullscreen
                if fullscreen:
                    win = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                    daw, dah = monitor_size[0], monitor_size[1]
                    background = Image.open("background.jpg")
                    background = background.resize((monitor_size[0], monitor_size[1]))
                    background.save("background.png")
                    background = pygame.image.load("background.png").convert()
                else:
                    win = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
                    daw, dah = 800, 600
                    background = Image.open("background.jpg")
                    background = background.resize((800, 600))
                    background.save("background.png")
                    background = pygame.image.load("background.png").convert()
    
    win.blit(background, (0, 0))
    
    da_fps = int(clock.get_fps())
    
    text = font.render(str(da_fps), 1, pygame.Color(200, 200, 200))
    win.blit(text, (10, 10))
    
    for rd in raindrops:
        rd.fall(dt, daw, dah)
        rd.draw(win)
    
    pygame.display.flip()
