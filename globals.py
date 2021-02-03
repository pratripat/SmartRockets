import pygame

width = height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Smart Rockets')

lifespan = 260
target = pygame.math.Vector2(width/2, 50)

black = (0,0,0)
white = (255,255,255)
