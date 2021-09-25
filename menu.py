from config import *

class StartMenu:
    def __init__(self):
        self.dead = False
        self.dying = False

        self.progress = 0

    def draw(self):

        screen.fill((41, 41, 41))

        screen.blit(texture_lib["title"], (200, 25))

        # screen.blit(texture_lib["title_top"], (150, 40 + self.title_cycle1.get() / 2))
        # screen.blit(texture_lib["title_text"], (150, 40 + self.title_cycle2.get() / 2))
        # screen.blit(texture_lib["title_bottom"], (150, 40 + self.title_cycle3.get() / 2))

        screen.blit(texture_lib["start_button"], (300, 250))
        if 300 < pygame.mouse.get_pos()[0] < 500:
            if 250 < pygame.mouse.get_pos()[1] < 340:
                screen.blit(texture_lib["start_button_hover"], (300, 250))
                if pygame.mouse.get_pressed(3)[0]:
                    screen.blit(texture_lib["start_button_pressed"], (300, 250))
                    self.dying = True

        screen.blit(texture_lib["hand"], (ENV["mouse_x"], ENV["mouse_y"]))
        pygame.display.flip()

    def draw_exit(self):
        self.progress += 8
        pygame.draw.rect(screen, (41, 41, 41),
                         pygame.Rect(400 - self.progress * 8 / 2, 250 - self.progress * 5 / 2,
                                     self.progress * 8, self.progress * 5))
        #pygame.display.flip()
        if self.progress > 100:
            self.dead = True

    def start(self):
        while not self.dead:
            for event in pygame.event.get():
                handle_common_event(event)
            if self.dying:
                self.draw_exit()
            else:
                self.draw()
            clock.tick(30)
