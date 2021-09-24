from config import *


class Item:
    def __init__(self, pos, texture, size):
        self.pos = pos
        self.size = size
        self.texture = texture_lib[texture]

    def draw(self):
        pos = (self.pos[0] - (ENV["mouse_x"] - SCREEN_WIDTH/2) * (100/self.pos[1])**2,
                                   self.pos[1] - self.size[1] - (ENV["mouse_y"] - SCREEN_HEIGHT/2) * (100/self.pos[1])**2)
        pygame.draw.ellipse(screen, (150, 150, 150), (pos[0], pos[1] + self.size[1] - 20, self.size[0], 20))
        screen.blit(self.texture, pos)

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

    def draw_back(self, player_y):
        screen.blit(self.background, (-100 - (ENV["mouse_x"] - SCREEN_WIDTH/2) * (100/245)**2,  - (ENV["mouse_y"] - SCREEN_HEIGHT/2) * (100/245)**2))

        for item in self.items:
            if item.pos[1] > player_y:
                return
            item.draw()

    def draw_fore(self, player_y):
        for item in self.items:
            if item.pos[1] > player_y:
                item.draw()

        screen.blit(self.foreground, (-100 - (ENV["mouse_x"] - SCREEN_WIDTH / 2) * (100 / SCREEN_HEIGHT) ** 2,
                                      - (ENV["mouse_y"] - SCREEN_HEIGHT / 2) * (100 / SCREEN_HEIGHT) ** 2))


map1 = Map(0, "bg1", "front1")
map1.add_item(Item((77, 310), "bench", (297, 99)))
map1.add_item(Item((580, 310), "lamp", (200, 339)))
map1.add_item(Item((450, 450), "vase", (184, 273)))
map1.sort_items()
