import pygame
from pygame.locals import *
import random
import time

pygame.init()
pygame.display.set_caption("killer")
display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
ph = pygame.image.load("msq.png").convert()   # photo to click
font = pygame.font.Font(None, 50)  # size of text

list = []
timer = 0
score = 0
force = 500

start_time = time.time()

class Inilist:
    def __init__(self, ph):
        self.x = random.randint(0, 700)
        self.y = random.randint(60, 600)
        self.ph = ph
        self.rect = Rect(self.x, self.y, self.ph.get_width(), self.ph.get_height())

    def draw(self, display):
        x = self.x
        y = self.y
        display.blit(self.ph, (x, y))

done = True

while done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = False

        elif event.type == MOUSEBUTTONDOWN:   # mouse_coordinate

            for el in list:
                if el.rect.collidepoint(mouse):  # if click mouse_coordinate in rectangle
                    list.remove(el)  # delete the photo in display
                    score += 1  # add score if you click
                    end_time = time.time()  # after add score get the time

    display.fill((255, 255, 255))

    mouse = pygame.mouse.get_pos()

    if timer % 500 == 2:  # speed regulation need modification
        list.append(Inilist(ph))
    timer += force
    force += 2

    if score == 10:  # how much of score to finish
        display.blit(font.render("you time: " + str((" %s seconds" % (end_time - start_time))), True, (0, 0, 0)), (0, 5))
        display.blit(font.render("world is free of : " + str(" %s mosquitoes " % score), True, (0, 0, 0)), (0, 40))
        clock.tick(1)  # froze display bad idea, but working

# if score < 10: # another metod for the froze display
    for inilist in list:   # draw the photo
        inilist.draw(display)

    # display.blit(font.render("score: " + str(score), True, (0, 0, 0)), (10, 10))

    pygame.display.flip()
