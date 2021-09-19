from config import *

class StartMenu:
    def __init__(self):
        self.dead = False
        self.dying = False

    def draw(self):
        pass

    def draw_exit(self):
        pass

    def start(self):
        while not self.dead:
            for event in pygame.event.get():
                handle_common_event(event)
            if self.dying:
                self.draw_exit()
            else:
                self.draw()
            clock.tick(30)
