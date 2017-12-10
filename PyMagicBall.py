import pygame, sys, random, time
from pygame.locals import *

answers = ['Yes','No','Maybe','Ask later']

pygame.init()
SCREEN = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Magic Ball')
ball = pygame.image.load("Magic crystal ball.png")

font = pygame.font.SysFont("verdana", 30)
SCREEN.blit(ball,(0,0))
text = font.render('CLICK', True, (255, 255, 255))
SCREEN.blit(text,(260,280))

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONUP:
            SCREEN.blit(ball,(0,0))
            word = answers[random.choice(range(len(answers)))]
            text = font.render(word, True, (random.choice((0,255)), random.choice((0,255)), random.choice((0,255))))
            SCREEN.blit(text,(300-len(word)*8,280))
            pygame.display.update()
            time.sleep(2)
            SCREEN.blit(ball,(0,0))
            text = font.render('CLICK', True, (255, 255, 255))
            SCREEN.blit(text,(260,280))
    pygame.display.update()
