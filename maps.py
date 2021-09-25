from config import *


class Item:
    def __init__(self, item_id, pos, texture, size, interactable=False):
        self.pos = pos
        self.size = size
        self.item_id = item_id
        self.texture = texture_lib[texture]
        self.interact_cycle = ReCycle(7, 3)
        self.interactable = interactable

    def draw(self):
        pos = (self.pos[0] - (ENV["mouse_x"] - SCREEN_WIDTH/2) * (100/self.pos[1])**2,
                                   self.pos[1] - self.size[1] - (ENV["mouse_y"] - SCREEN_HEIGHT/2) * (100/self.pos[1])**2)
        pygame.draw.ellipse(screen, (150, 150, 150), (pos[0], pos[1] + self.size[1] - 20, self.size[0], 20))
        screen.blit(self.texture, pos)

    def draw_interact(self):
        pos = (self.pos[0] - (ENV["mouse_x"] - SCREEN_WIDTH / 2) * (100 / self.pos[1]) ** 2,
               self.pos[1] - self.size[1] - (ENV["mouse_y"] - SCREEN_HEIGHT / 2) * (100 / self.pos[1]) ** 2)
        screen.blit(texture_lib["interact"], (pos[0], pos[1] + self.interact_cycle.get() * 2))

    def __lt__(self, other):
        return self.pos[1] < other.pos[1]


class Map:
    def __init__(self, map_id, background, foreground):
        self.background = texture_lib[background]
        self.foreground = texture_lib[foreground]
        self.items = []
        self.id = map_id
        self.player = None

    def set_player(self, player):
        self.player = player

    def add_item(self, item):
        self.items.append(item)

    def sort_items(self):
        self.items.sort()

    def draw_back(self, player_pos):
        screen.blit(self.background, (-100 - (ENV["mouse_x"] - SCREEN_WIDTH/2) * (100/245)**2,  - (ENV["mouse_y"] - SCREEN_HEIGHT/2) * (100/245)**2))

        for item in self.items:
            if item.pos[1] > player_pos[1]:
                return
            item.draw()

    def draw_fore(self, player_pos):
        for item in self.items:
            if item.pos[1] > player_pos[1]:
                item.draw()

        screen.blit(self.foreground, (-100 - (ENV["mouse_x"] - SCREEN_WIDTH / 2) * (100 / SCREEN_HEIGHT) ** 2,
                                      - (ENV["mouse_y"] - SCREEN_HEIGHT / 2) * (100 / SCREEN_HEIGHT) ** 2))

        ENV["item_interact"] = None
        for item in self.items:
            if item.interactable:
                if distance((player_pos[0] + 50, player_pos[1]), (item.pos[0] + item.size[0]/2, item.pos[1])) < 80:
                    ENV["item_interact"] = item
                    item.draw_interact()
                    break


map1 = Map(0, "bg1", "front1")
map1.add_item(Item(0, (77, 310), "bench", (297, 99)))
map1.add_item(Item(0, (580, 310), "lamp", (200, 339)))
map1.add_item(Item(1, (450, 450), "vase", (184, 273), interactable=True))
map1.sort_items()
