import pygame
import time
import random
import math
import numpy as np
from typing import List

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0, 255, 0)
blue = (0, 0, 255)

WIDTH = 1000
HEIGHT = 1000

CIRCLE_WIDTH = 2

SPEED = 15

TICK_TIME = 1

class Ball:
    x: int
    y: int
    vx: int
    vy: int
    bx: List[int]
    by: List[int]
    r: int

    def __init__(self) -> None:
        self.x = random.randint(0,WIDTH)
        self.y = random.randint(0,HEIGHT)
        self.vx = random.randint(-SPEED,SPEED)
        self.vy = random.randint(-SPEED,SPEED)
        self.bx = [0] * WIDTH
        self.by = [0] * HEIGHT
        self.r = 50

    def update(self) -> None:
        self.x += self.vx
        self.y += self.vy

        if self.x < 0 or self.x > WIDTH:
            self.vx *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.vy *= -1

        for i in range(WIDTH):
            self.bx[i] = int((self.x - i)**2)
        for i in range(HEIGHT):
            self.by[i] = int((self.y - i)**2)

class Pyballs:
    balls: List[Ball]

    def __init__(self, balls: List[Ball]):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('pyballs')
        self.time = time.time()
        self.clock = pygame.time.Clock()
        self.time = time.time()

        self.balls = balls

    def move(self):
        pass

    def draw(self, skip=True):

        if not skip:
            actual_time = time.time()
            if actual_time - self.time < TICK_TIME:
                return
            self.time = actual_time

        self.gameDisplay.fill(white)

        arr = np.zeros((WIDTH, HEIGHT))

        for ball in self.balls:
            ball.update()

        for y in range(HEIGHT):
            for x in range(WIDTH):
                m = 1
                for ball in self.balls:
                    m += 20000/(ball.bx[x] + ball.by[y] + 1)
                arr[y,x] = m % 255

        surf = pygame.surfarray.make_surface(arr)

        self.gameDisplay.blit(surf, (0, 0))

        for ball in self.balls:
            pygame.draw.circle(self.gameDisplay, red, (ball.y, ball.x), ball.r, CIRCLE_WIDTH)
    
    def start(self):
        self.end = False
        self.draw(True)
        while not self.end:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.balls[0].vx = 0
                        self.balls[0].vy = -SPEED
                    if event.key == pygame.K_w:
                        self.balls[0].vy = 0
                        self.balls[0].vx = -SPEED
                    if event.key == pygame.K_d:
                        self.balls[0].vx = 0
                        self.balls[0].vy = SPEED
                    if event.key == pygame.K_s:
                        self.balls[0].vy = 0
                        self.balls[0].vx = SPEED
                    if event.key == pygame.K_r:
                        self.__init__([])
                    if event.key == pygame.K_q:
                        print('q closed')
                        self.end = True
                if event.type == pygame.QUIT:
                    self.end = True
            self.move()
            self.draw()
            pygame.display.update()
            self.clock.tick(60)
def euclidean_distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

if __name__ == '__main__':
    ball = Ball()
    ball2 = Ball()
    a = Pyballs([
        ball,
        ball2
        ])
    a.start()
