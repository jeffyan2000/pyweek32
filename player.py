from config import *


import math


class Player:
    def __init__(self, world):
        self.pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
        self.xDirection = 0  # tendency
        self.yDirection = 0
        self.last_x = 0
        self.world = world
        self.inventory = ...

        self.walk_cycle = TimedCycle(5, (3, 3, 3, 3, 3), [200,200,200,200,200])


    def draw(self):

        if self.xDirection == -1:
            self.last_x = -1
            draw_at_frame(self.pos, "temp_left", self.walk_cycle.get_frame(), (64, 64))
        elif self.xDirection == 1:
            self.last_x = 1
            draw_at_frame(self.pos, "temp_right", self.walk_cycle.get_frame(), (64, 64))
        elif self.yDirection != 0:
            if self.last_x == -1:

                draw_at_frame(self.pos, "temp_left", self.walk_cycle.get_frame(), (64, 64))  # for not movement.
            else:
                draw_at_frame(self.pos, "temp_right", self.walk_cycle.get_frame(), (64, 64))  # for not movement.
        else:
            if self.last_x == -1:
                draw_at_frame(self.pos, "temp_left", 0, (64, 64)) # for not movement.
            elif self.last_x == 1:
                draw_at_frame(self.pos, "temp_right", 0, (64, 64))  # for not movement.
            else:
                draw_at_frame(self.pos, "temp_right", 0, (64, 64))  # for not movement.


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

    def move(self, dx, dy):

        if -10 <= self.pos[0] <= 750:
            self.pos[0] += dx
        else:
            if -10 > self.pos[0]: # change the sign for continuation
                self.pos[0] = -10
            else:
                self.pos[0] = 750
        if 0 <= self.pos[1] <= 450:
            self.pos[1] += dy
        else:
            if 0 > self.pos[1]: # change the sign for continuation
                self.pos[1] = 0
            else:
                self.pos[1] = 450

    def update(self):

        if self.xDirection != 0 or self.yDirection != 0:
            self.move(ENV["delta_time"] * self.walk_cycle.get_movement() * self.xDirection,
                      ENV["delta_time"] * self.walk_cycle.get_movement() * self.yDirection)
            self.walk_cycle.tick()
            # if self.walk_cycle.changed() and self.walk_cycle.get_frame() == 2:
            #     self.world.animations.append(animation.WalkDust(self.pos, self.xDirection != -1)) # Walk dust



        #ENV["global_offset"] = (self.pos[0] - self.offset[0], self.pos[1] - self.offset[1])
