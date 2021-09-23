from config import *


import math


class Player:
    def __init__(self, world):
        self.pos = [0, 0]
        self.offset = [0, 0]

        self.xDirection = 0  # tendency
        self.yDirection = 0
        self.world = world
        self.inventory = ...


        self.walk_cycle = TimedCycle(5, (3, 3, 3, 3, 3), [200,200,200,200,200])

    def get_draw_pos(self):
        return SCREEN_WIDTH // 2 + self.offset[0], SCREEN_HEIGHT // 2 + self.offset[1]

    def draw(self):
        pos = self.get_draw_pos()

        if self.xDirection == -1:
            draw_at_frame(pos, "temp_left", self.walk_cycle.get_frame(), (64, 64))
        elif self.xDirection == 1:
            draw_at_frame(pos, "temp_right", self.walk_cycle.get_frame(), (64, 64))
        else:
            draw_at_frame(pos, "temp_right", 0, (64,64))

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
        print(self.pos)
        self.pos[0] += dx
        self.pos[1] += dy

    def update(self):

        prev_pos = self.pos[0], self.pos[1]

        if self.xDirection != 0 or self.yDirection != 0:
            self.move(ENV["delta_time"] * self.walk_cycle.get_movement() * self.xDirection,
                      ENV["delta_time"] * self.walk_cycle.get_movement() * self.yDirection)
            self.walk_cycle.tick()
            # if self.walk_cycle.changed() and self.walk_cycle.get_frame() == 2:
            #     self.world.animations.append(animation.WalkDust(self.pos, self.xDirection != -1)) # Walk dust


        self.move_camera(self.pos[0] - prev_pos[0], self.pos[1] - prev_pos[1])
        ENV["global_offset"] = (self.pos[0] - self.offset[0], self.pos[1] - self.offset[1])
