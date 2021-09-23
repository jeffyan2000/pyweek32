from config import *


class Animation:
    def __init__(self, pos, length, speed, width, height, txt_name):
        self.draw_cycle = Cycle(length, speed)
        self.pos = pos
        self.name = txt_name
        self.height = height
        self.width = width

    def is_dead(self):
        return self.draw_cycle.one

    def draw(self, offset=(0, 0)):
        current = self.draw_cycle.get()
        screen.blit(texture_lib[self.name], (self.pos[0] - offset[0], self.pos[1] - offset[1]),
                    pygame.Rect(0, current*self.height, self.width, self.height))


class WalkDust(Animation):
    def __init__(self, pos, left):
        Animation.__init__(self, pos, 7, 1, 50, 50, "walk_dust")
        if left:
            self.name = "walk_dust_left"
            self.pos = (pos[0], pos[1] + 25)
        else:
            self.name = "walk_dust"
            self.pos = (pos[0] + 30, pos[1] + 25)

    def draw(self, offset=(0, 0)):
        current = self.draw_cycle.get()
        screen.blit(texture_lib[self.name], (self.pos[0] - offset[0] + DEFAULT_CENTER[0],
                                             self.pos[1] - offset[1] + DEFAULT_CENTER[1]),
                    pygame.Rect(0, current*self.height, self.width, self.height))