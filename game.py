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
        for map_in in maps:
            map_in.set_player(self.player)
        self.inventory = Inventory()
        self.current_mission = None
        self.current_map = maps[0]
        self.current_map_num = 0
        self.current_chat_scene = ChatScene("start")
        self.trans_scene = NextScene("Day 1: bedroom")


    def next_map(self):
        if self.current_map_num == 15:
            self.trans_scene = EndScene()
            return
        self.current_map_num += 1
        self.current_map = maps[self.current_map_num]
        self.player.pos = [150, 400]
        if self.current_map_num == 1:
            self.trans_scene = NextScene("Day 1, living room")
            self.start_chat_scene("day1")
        elif self.current_map_num == 2:
            self.trans_scene = NextScene("Day 1, street")
            self.start_chat_scene("day1street")
            self.inventory.add_item("money")
        elif self.current_map_num == 3:
            self.trans_scene = NextScene("Day 1, night")
            self.start_chat_scene("day1night")
        elif self.current_map_num == 4:
            self.trans_scene = NextScene("2000, day 1")
            self.start_chat_scene("p1")
        elif self.current_map_num == 5:
            self.inventory.consume_item("medicine")
            self.trans_scene = NextScene("2000, dinner")
            self.start_chat_scene("p1r", next_map=True)
        elif self.current_map_num == 6:
            self.trans_scene = NextScene("2000, day 2")
            self.start_chat_scene("p2")
        elif self.current_map_num == 7:
            self.trans_scene = NextScene("2000, park")
            self.start_chat_scene("p2r", next_map=True)
        elif self.current_map_num == 8:
            self.trans_scene = NextScene("2000, hotel")
            self.start_chat_scene("p3")
        elif self.current_map_num == 9:
            self.trans_scene = NextScene("2000, day 1", reverse=True)
            self.start_chat_scene("q1")
        elif self.current_map_num == 10:
            self.trans_scene = NextScene("2000, day 2")
            self.start_chat_scene("q2")
        elif self.current_map_num == 11:
            self.inventory.consume_item("shovel")
            self.trans_scene = NextScene("2000, hotel")
            self.start_chat_scene("q3")
        elif self.current_map_num == 12:
            self.inventory.consume_item("injector")
            self.trans_scene = NextScene("Day 1, bed room", reverse=True)
            self.start_chat_scene("start")
        elif self.current_map_num == 13:
            self.trans_scene = NextScene("Day 1, living room")
            self.start_chat_scene("day1")
        elif self.current_map_num == 14:
            self.trans_scene = NextScene("Day 1, street")
            self.start_chat_scene("day1street")
            self.inventory.add_item("money")
        elif self.current_map_num == 15:
            self.trans_scene = NextScene("Day 1, night")
            self.start_chat_scene("day1night")



    def start_chat_scene(self, chat_name, next_map=False):
        self.current_chat_scene = ChatScene(chat_name, next_map=next_map)

    def update(self):
        if self.trans_scene:
            if self.trans_scene.dead:
                self.trans_scene = None
        elif self.current_chat_scene:
            if self.current_chat_scene.dead:
                if self.current_chat_scene.next_map:
                    self.next_map()
                else:
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
        screen.fill(-1)
        self.current_map.draw_back(self.player.pos)
        self.current_map.player.draw()
        self.current_map.draw_fore(self.player.pos)
        self.inventory.draw()
        if self.current_mission:
            self.current_mission.draw()
        if self.trans_scene:
            self.trans_scene.draw()
        elif self.current_chat_scene:
            self.current_chat_scene.draw()

    def handle_event(self, event):
        if not self.trans_scene and self.current_chat_scene:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_k:
                    self.current_chat_scene.next_dialog()
        elif not self.current_chat_scene and not self.trans_scene:
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
