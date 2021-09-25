from config import *
from maps import *
from player import *
from inventory import *
from mission import *
from chat import *

class Game:
    def __init__(self):
        self.dead = False
        self.fps_cap = 40
        self.player = Player(self)
        map1.set_player(self.player)
        self.inventory = Inventory()
        self.inventory.add_item("shovel")
        self.inventory.add_item("poop")
        self.inventory.add_item("injector")
        self.current_mission = None
        self.current_map = map1
        self.current_chat_scene = None
        self.trans_scene = NextScene("Day 1 Start")

    def load_map(self, map_json):
        pass

    def start_chat_scene(self, chat_name):
        self.current_chat_scene = ChatScene(chat_name)

    def update(self):
        if self.trans_scene:
            if self.trans_scene.dead:
                self.trans_scene = None
        else:
            if self.current_chat_scene:
                if self.current_chat_scene.dead:
                    self.current_chat_scene = None
            else:
                self.player.update()
        if not (pygame.key.get_pressed()[pygame.K_w]
            or pygame.key.get_pressed()[pygame.K_a]
            or pygame.key.get_pressed()[pygame.K_s]
            or pygame.key.get_pressed()[pygame.K_d]):
            self.player.xDirection = 0
            self.player.yDirection = 0

    def draw(self):
        screen.fill((146, 252, 249))
        map1.draw_back(self.player.pos)
        self.player.draw()
        map1.draw_fore(self.player.pos)
        self.inventory.draw()
        if self.current_mission:
            self.current_mission.draw()
        if self.current_chat_scene:
            self.current_chat_scene.draw()
        if self.trans_scene:
            self.trans_scene.draw()

    def handle_event(self, event):
        if self.current_chat_scene:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_k:
                    self.current_chat_scene.next_dialog()
        else:
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
