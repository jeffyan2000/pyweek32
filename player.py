from config import *
from math import sqrt

import math


class Player:
    def __init__(self, game):
        self.pos = [150, 400]
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
                        self.game.start_chat_scene("door", next_map=True)
                    elif item.item_id == 2:
                        self.game.start_chat_scene("mom", next_map=True)
                    elif item.item_id == 3:
                        self.game.start_chat_scene("mystery", next_map=True)
                    elif item.item_id == 4:
                        self.game.start_chat_scene("box", next_map=True)
                    elif item.item_id == 5:
                        self.game.start_chat_scene("medicine")
                        self.game.current_map.remove_item(5)
                        self.game.inventory.add_item("medicine")
                    elif item.item_id == 6:
                        if self.game.inventory.has_item("medicine"):
                            self.game.start_chat_scene("table2", next_map=True)
                        else:
                            self.game.start_chat_scene("table1")
                    elif item.item_id == 7:
                        self.game.start_chat_scene("shovel")
                        self.game.current_map.remove_item(7)
                        self.game.inventory.add_item("shovel")
                    elif item.item_id == 8:
                        if self.game.inventory.has_item("shovel"):
                            self.game.start_chat_scene("hole2", next_map=True)
                        else:
                            self.game.start_chat_scene("hole1")
                    elif item.item_id == 9:
                        self.game.start_chat_scene("injector")
                        self.game.current_map.remove_item(9)
                        self.game.inventory.add_item("injector")
                    elif item.item_id == 10:
                        if self.game.inventory.has_item("injector"):
                            self.game.start_chat_scene("cream2", next_map=True)
                        else:
                            self.game.start_chat_scene("cream1")
                    elif item.item_id == 11:
                        self.game.start_chat_scene("q12", next_map=True)
                    elif item.item_id == 12:
                        self.game.start_chat_scene("q22", next_map=True)
                    elif item.item_id == 13:
                        self.game.start_chat_scene("q32", next_map=True)

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
