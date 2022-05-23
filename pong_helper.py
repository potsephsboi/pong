import pygame
import time
import random

clock = pygame.time.Clock()
WIDTH = 500
HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
VEL_X = 0
VEL_Y = 2
VEL = 3
SCORE1 = 0
SCORE2 = 0
BALL_X = 210

def handle_ball(ball, char1, char2):
    global VEL_X
    global VEL_Y
    global SCORE1
    global SCORE2
    ball.y += VEL_Y
    ball.x += VEL_X
    if ball.colliderect(char1):
        VEL_Y = -abs(VEL_Y)
        d = ball.x - ((char1.x + char1.x + 50) / 2)
        VEL_X = int(d / random.randint(6, 10))

    if ball.colliderect(char2):
        VEL_Y = abs(VEL_Y)
        d = ball.x - ((char2.x + char2.x + 50) / 2)
        VEL_X = int(d / random.randint(6, 10))

    if ball.y == 0:
        VEL_Y = abs(VEL_Y)
        SCORE1 += 1
        ball.x = 250
        ball.y = 200
        VEL_X = 0
        char1.x = 210
        char2.x = 210
        print(SCORE1, SCORE2)
        time.sleep(0.5)
    if ball.y == 396:
        VEL_Y = -abs(VEL_Y)
        SCORE2 += 1
        ball.x = 250
        ball.y = 200
        VEL_X = 0
        char1.x = 210
        char2.x = 210
        print(SCORE1, SCORE2)
        time.sleep(0.5)

    if 10 >= ball.x >= 0:
        VEL_X = abs(VEL_X)
    if 500 >= ball.x >= 490:
        VEL_X = -abs(VEL_X)


def movement(char1, char2):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] and char1.x - VEL > 0:
        char1.x -= VEL
    if keys_pressed[pygame.K_d] and char1.x + VEL < 500:
        char1.x += VEL
    if keys_pressed[pygame.K_LEFT] and char2.x - VEL > 0:
        char2.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and char2.x + VEL < 500:
        char2.x += VEL


def run_ai1(char1, ball):
    global BALL_X
    global VEL
    VEL = random.randint(2, 5)
    dx = ball.x - BALL_X
    BALL_X = ball.x
    if char1.x < ball.x and dx > 0:
        char1.x += VEL
    if char1.x > ball.x and dx < 0:
        char1.x -= VEL
    if char1.x < ball.x and dx == 0:
        char1.x += VEL
    if char1.x > ball.x and dx == 0:
        char1.x -= VEL
