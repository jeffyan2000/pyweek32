from config import *
from maps import *
from player import *

class Game:
    def __init__(self):
        self.dead = False
        self.fps_cap = 40
        self.player = Player(map1)


    def load_map(self, map_json):
        pass

    def update(self):
        self.player.update()

    def draw(self):
        screen.fill((146, 252, 249))
        map1.draw()
        self.player.draw()

    def handle_event(self, event):
        self.player.handle_event(event)

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
