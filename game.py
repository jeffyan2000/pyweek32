from config import *
from maps import *

class Game:
    def __init__(self):
        self.dead = False
        self.fps_cap = 40

    def load_map(self, map_json):
        pass

    def update(self):
        pass

    def draw(self):
        screen.fill((146, 252, 249))
        map1.draw()

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
            screen.blit(texture_lib["hand"], (ENV["mouse_x"], ENV["mouse_y"]))
            pygame.display.flip()
