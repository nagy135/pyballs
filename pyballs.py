import pygame
import time
import random
import numpy as np
from typing import List

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0, 255, 0)
blue = (0, 0, 255)

WIDTH = 400
HEIGHT = 400

CIRCLE_WIDTH = 2

SPEED = 5

TICK_TIME = 1

class Ball:
    x: int
    y: int
    vx: int
    vy: int
    r: int

    def __init__(self) -> None:
        self.x = random.randint(0,WIDTH)
        self.y = random.randint(0,HEIGHT)
        self.vx = random.randint(-SPEED,SPEED)
        self.vy = random.randint(-SPEED,SPEED)
        self.r = 50


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

        bxby = [];
        for ball in self.balls:
            ball.x += ball.vx
            ball.y += ball.vy

            if ball.x < 0 or ball.x > WIDTH:
                ball.vx *= -1
            if ball.y < 0 or ball.y > HEIGHT:
                ball.vy *= -1

            bx = [0] * WIDTH
            for i in range(WIDTH):
                bx[i] = int((ball.x - i)**2)
            by = [0] * HEIGHT
            for i in range(HEIGHT):
                by[i] = int((ball.y - i)**2)
            bxby.append((bx, by))

        arr = np.ones((WIDTH, HEIGHT))

        for i in range(len(self.balls)):
            X, Y = np.meshgrid(np.array(bxby[i][0]), np.array(bxby[i][1]))
            # arr +=  20000/X + 20000/Y
            arr *= 20000
            arr /= (X+Y)

        norm = np.linalg.norm(arr.clip(0,500))
        arr /= norm

        arr *= 20000
        arr %= 255

        self.gameDisplay.fill(white)
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

if __name__ == '__main__':
    ball = Ball()
    ball2 = Ball()
    ball3 = Ball()
    a = Pyballs([
        ball,
        ball2,
        ball3
        ])
    a.start()
