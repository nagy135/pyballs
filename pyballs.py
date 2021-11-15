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

TICK_TIME = 1

class Ball:
    x: int
    y: int
    r: int

    def __init__(self) -> None:
        self.x = random.randint(0,WIDTH)
        self.y = random.randint(0,HEIGHT)
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
        # void draw() {
        #   for (int i=0; i<numBlobs; ++i) {
        #     b[i].update();
        #   }
        #   
        #   // Output into a buffered image for reuse
        #   pg.beginDraw();
        #   pg.loadPixels();
        #   for (int y=0; y<h; y++) {
        #     for (int x=0; x<w; x++) {
        #       int m = 1;
        #       for (int i=0; i <numBlobs; i++) {
        #         // Increase this number to make your blobs bigger
        #         m += 20000/(b[i].bx[x] + b[i].by[y] + 1);
        #       }
        #       pg.pixels[x+y*w] = color(0, m+x, (x+m+y)/2); //in HSB mode: color((m+x+y),255,255);
        #     }
        #   }
        #   pg.updatePixels();
        #   pg.endDraw();
        #
        #   // Display the results
        #   image(pg, 0, 0, width, height); 
        # }

        if not skip:
            actual_time = time.time()
            if actual_time - self.time < TICK_TIME:
                return
            self.time = actual_time

        self.gameDisplay.fill(white)

        x = np.arange(0, 300)
        y = np.arange(0, 300)

        x[100] = 200
        x[200] = 200

        # for y in range(HEIGHT):
        #     for x in range(WIDTH):
        #         m = 1
        #         for ball in self.balls:
        #             distance = euclidean_distance(x, y, WIDTH//2, HEIGHT//2)
        #
        #             m += 2000 / (ball.x + ball.y + 1)

        X, Y = np.meshgrid(x, y)
        Z = X + Y
        Z = 255*Z/Z.max()
        surf = pygame.surfarray.make_surface(Z)

        self.gameDisplay.blit(surf, (0, 0))

        return




    
    def start(self):
        self.end = False
        self.draw(True)
        while not self.end:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # if event.key == pygame.K_w:
                    #     self.player_move('k')
                    # if event.key == pygame.K_a:
                    #     self.player_move('h')
                    # if event.key == pygame.K_s:
                    #     self.player_move('j')
                    # if event.key == pygame.K_d:
                    #     self.player_move('l')
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
