from config import *


class Game:
    def __init__(self):
        self.dead = False
        self.fps_cap = 40

    def load_map(self, map_json):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def handle_event(self, event):
        pass

    def start(self):
        self.update()
        while not self.dead:
            ENV['delta_time'] = clock.tick(self.fps_cap)/1000
            for event in pygame.event.get():
                handle_common_event(event)
                self.handle_event(event)
            self.update()
            self.draw()
            pygame.display.flip()
