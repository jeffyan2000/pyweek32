from config import *
from config import *

import math


class Player:
    def __init__(self, world):
        self.pos = [0, 0]
        self.offset = [0, 0]
        self.direction = 0
        self.world = world

    def get_draw_pos(self):
        return SCREEN_WIDTH // 2 - PLAYER_SIZE[0] // 2 + self.offset[0], \
               SCREEN_HEIGHT // 2 - PLAYER_SIZE[1] // 2 + self.offset[1]

    def draw(self):
        pos = self.get_draw_pos()

        # leave blank for sprite animation:
        # TODO: Do we leave sprite resize to animation.py?
        if self.direction == -1:
            pass
        elif self.direction == 1:
            pass
        else:
            pass

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.direction -= 1
            elif event.key == pygame.K_d:
                self.direction += 1
            elif event.key == pygame.K_w:
                pass
            elif event.key == pygame.K_s:
                pass

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.direction += 1
            elif event.key == pygame.K_d:
                self.direction -= 1
            elif event.key == pygame.K_w:
                pass
            elif event.key == pygame.K_s:
                pass

    def move_camera(self, dx, dy):
        self.offset[0] += dx
        self.offset[1] += dy
        if self.offset[0] != 0:
            self.offset[0] /= 1.1
            if abs(self.offset[0]) < 1:
                self.offset[0] = 0
        if self.offset[1] != 0:
            self.offset[1] /= 1.1
            if abs(self.offset[1]) < 1:
                self.offset[1] = 0

    def move(self, dx, dy):
        pass

    def update(self):
        pass
