
class Cycle:
    def __init__(self, num, speed, start_tick=0):
        self.tick = 0
        self.current = start_tick
        self.speed = speed
        self.num = num
        self.one = False
        self.prev = self.current

    def get(self):
        self.tick += 1
        self.prev = self.current
        if self.tick > self.speed:
            self.tick = 0
            self.current += 1
            if self.current >= self.num:
                self.current = 0
        if self.tick+1 > self.speed and self.current+1 >= self.num:
            self.one = True
        return self.current

    def reset(self):
        self.tick = 0
        self.current = 0

    def changed(self):
        return self.prev != self.current


class ReCycle:
    def __init__(self, num, speed, start=0):
        self.tick = 0
        self.current = start
        self.speed = speed
        self.num = num
        self.one = False
        self.v = 1
        self.prev = self.current

    def get(self):
        self.tick += 1
        if self.tick > self.speed:
            self.tick = 0
            self.prev = self.current
            self.current += self.v
            if self.current >= self.num:
                self.current = self.num - 1
                self.v = -1
                self.one = True
            elif self.current < 0:
                self.current = 0
                self.v = 1
        return self.current

    def reset(self):
        self.tick = 0
        self.current = 0

    def changed(self):
        return self.prev != self.current


class TimedCycle:
    def __init__(self, max_frame, ticks, movements, start_frame=0):
        self.current_tick = 0
        self.max_frame = max_frame
        self.frame = start_frame
        self.movements = movements
        self.max_ticks = ticks
        self.config = (max_frame, start_frame, movements, ticks)
        self.prev = start_frame

        self.one = False

    def changed(self):
        return self.prev != self.frame

    def tick(self):
        self.prev = self.frame
        self.current_tick += 1
        if self.current_tick > self.max_ticks[self.frame]:
            self.frame += 1
            self.current_tick = 0
            if self.frame >= self.max_frame:
                self.frame = 0
                self.one = True

    def get_movement(self):
        return self.movements[self.frame]

    def get_frame(self):
        return self.frame

    def reset(self):
        self.current_tick = 0
        self.max_frame, self.frame, self.movements, self.max_ticks = self.config
        self.one = False
