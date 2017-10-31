import pygame
from datetime import time
from pygame.locals import *

pygame.init()

time = 6
pygame.time.set_timer(USEREVENT + 1, 1000)

font = pygame.font.SysFont(None, 30)
font2 = pygame.font.SysFont('Arial', 60, bold=True)

window = pygame.display.set_mode((600, 500))
pygame.display.set_caption("My piu-piu game")
screen = pygame.Surface((600, 500))

square_enemy = pygame.Surface((40, 40))
square_enemy.fill((14, 204, 23))
pos_x_enemy = 0
pos_x = 0
pos_y_enemy = 0

warior_rect = pygame.Surface((20, 50))
warior_rect.fill((234, 13, 9))

bullet = pygame.Surface((3, 10))
bullet.fill((247, 247, 4))
bullet_go_up = False
#
pos_x_bullet = 500
pos_y_bullet = 300
timer = 0

dead = True
score = 0
speed = 1
done = True
square_go_right = False
pos_y_warior = int(290)
pygame.key.set_repeat(1, 0)
while done:
    screen.fill((0, 50, 50))
    for ex in pygame.event.get():
        if ex.type == pygame.QUIT:
            done = False

        if ex.type == USEREVENT + 1:
            time -= 1
            # text2 = font.render("Timer: {}".format(str(time)), True, (0, 0, 0))
            # if time == 0:
            # text2 = font.render("Timer: {}".format(str(time)), True, (0, 0, 0))
            # t3 = font2.render("GAME OVER", True, (0, 0, 0))
            # screen.blit(text3, (200, 300))
        # key for warior and bullet
        if ex.type == pygame.KEYDOWN:
            if ex.key == pygame.K_ESCAPE:
                done = False
            if ex.key == pygame.K_LEFT:
                if pos_y_warior > 5:
                    pos_y_warior -= 2
            if ex.key == pygame.K_RIGHT:
                if pos_y_warior < 580:
                    pos_y_warior += 2
            if ex.key == pygame.K_a:
                if bullet_go_up == False:
                    pos_y_bullet = pos_y_warior + 8
                    bullet_go_up = True
            if ex.key == pygame.K_r:
                if dead == False:
                    speed += 0.5
                    square_enemy.fill((14, 204, 23))
                    dead = True

    # enemy move



    if square_go_right == True:
        pos_x_enemy += speed
        if pos_x_enemy > 560:
            square_go_right = False
    else:
        pos_x_enemy -= speed
        if pos_x_enemy < 0:
            square_go_right = True

            # bullet fly
    if bullet_go_up == True:
        pos_x_bullet -= 3
        if pos_x_bullet < -5:
            bullet_go_up = False
            pos_x_bullet = 500

            # hit the target
    if (pos_y_bullet < pos_x_enemy + 30) and (pos_x_bullet < pos_y_enemy + 30) and (
        pos_y_bullet > pos_x_enemy - 30) and (pos_x_bullet > pos_y_enemy - 30):
        if dead == True:
            square_enemy.fill((0, 0, 0))
            dead = False
            score += 1
            # print score

    text = font.render("Your score: {}".format(str(score)), True, (0, 0, 0))
    # text2 = font.render("Timer: {}".format(str(time)), True, (0, 0, 0))
    # text2 = font.render("Timer: {}".format(str(time)), True, (0, 0, 0))
    # text3 = font2.render("GAME OVER", True, (0, 0, 0))
    screen.blit(text, (10, 450))
    # screen.blit(text2, (10, 470))
    # text3 = t3
    # screen.blit(text3,(200,300))
    screen.blit(square_enemy, (pos_x_enemy, pos_y_enemy))
    screen.blit(warior_rect, (pos_y_warior, 450))
    screen.blit(bullet, (pos_y_bullet, pos_x_bullet))
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(3)
    # label = font.render("Some text!", 1, (255, 255, 0))
    # screen.blit(label, (100, 100))
