from config import *
from math import sqrt

import math


class Player:
    def __init__(self, game):
        self.pos = [350, 400]
        self.xDirection = 0  # tendency
        self.yDirection = 0
        self.facing_right = True
        self.game = game
        self.h = 191
        self.w = 100

        self.walk_cycle = Cycle(11, 0)


    def draw(self):
        pos = (self.pos[0] - (ENV["mouse_x"] - SCREEN_WIDTH / 2) * (100 / self.pos[1]) ** 2,
               self.pos[1] - self.h - (ENV["mouse_y"] - SCREEN_HEIGHT / 2) * (100 / self.pos[1]) ** 2)
        pygame.draw.ellipse(screen, (150, 150, 150), (pos[0], pos[1] + self.h - 20, self.w, 20))
        texture = "me"
        if not self.facing_right:
            texture = "me_left"
        if self.yDirection or self.xDirection:
            screen.blit(texture_lib[texture], (pos[0], pos[1]-h_s[self.walk_cycle.get()]))
        else:
            screen.blit(texture_lib[texture], pos)
            if self.walk_cycle.tick != 0 or self.walk_cycle.current != 0:
                self.walk_cycle.reset()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.xDirection -= 1
            elif event.key == pygame.K_d:
                self.xDirection += 1
            elif event.key == pygame.K_w:
                self.yDirection -= 1
            elif event.key == pygame.K_s:
                self.yDirection += 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.xDirection += 1
            elif event.key == pygame.K_d:
                self.xDirection -= 1
            elif event.key == pygame.K_w:
                self.yDirection += 1
            elif event.key == pygame.K_s:
                self.yDirection -= 1
            elif event.key == pygame.K_k:
                if ENV["item_interact"]:
                    item = ENV["item_interact"]
                    if item.item_id == 1:
                        self.game.start_chat_scene("vase")

    def move(self, dx, dy):
        self.pos[0] += dx
        if dx > 0:
            self.facing_right = True
        elif dx < 0:
            self.facing_right = False
        self.pos[1] += dy
        if self.pos[0] < 0:
            self.pos[0] = 0
        if self.pos[0] > 720:
            self.pos[0] = 720
        if self.pos[1] < 270:
            self.pos[1] = 270
        if self.pos[1] > 500:
            self.pos[1] = 500

    def update(self):

        if self.xDirection != 0 or self.yDirection != 0:
            speed = 6
            if self.xDirection != 0 and self.yDirection != 0:
                speed = 6/sqrt(2)
            self.move(speed * self.xDirection, speed * self.yDirection)
