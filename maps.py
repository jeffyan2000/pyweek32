from config import *


class Item:
    def __init__(self, item_id, pos, texture, interactable=False, floor=False):
        self.pos = pos
        self.item_id = item_id
        self.texture = texture_lib[texture]
        self.size = self.texture.get_size()
        self.interact_cycle = ReCycle(7, 3)
        self.interactable = interactable
        self.floor = floor

    def draw(self):
        pos = (self.pos[0] - (ENV["mouse_x"] - SCREEN_WIDTH/2) * (100/self.pos[1])**2,
                                   self.pos[1] - self.size[1] - (ENV["mouse_y"] - SCREEN_HEIGHT/2) * (100/self.pos[1])**2)
        if not self.floor:
            pygame.draw.ellipse(screen, (150, 150, 150), (pos[0], pos[1] + self.size[1] - 20, self.size[0], 20))
        screen.blit(self.texture, pos)

    def draw_interact(self):
        pos = (self.pos[0] - (ENV["mouse_x"] - SCREEN_WIDTH / 2) * (100 / self.pos[1]) ** 2 - 50,
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

    def remove_item(self, item_id):
        pos = -1
        for i in range(len(self.items)):
            if self.items[i].item_id == item_id:
                pos = i
                break
        if pos >= 0:
            del self.items[pos]

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

        screen.blit(self.foreground, (-50 - (ENV["mouse_x"] - SCREEN_WIDTH / 2) * (100 / SCREEN_HEIGHT) ** 2,
                                      -40 - (ENV["mouse_y"] - SCREEN_HEIGHT / 2) * (100 / SCREEN_HEIGHT) ** 2))

        ENV["item_interact"] = None
        for item in self.items:
            if item.interactable:
                if distance((player_pos[0] + 50, player_pos[1]), (item.pos[0] + item.size[0]/2, item.pos[1])) < 80:
                    ENV["item_interact"] = item
                    item.draw_interact()
                    break


map1 = Map(0, "bg1", "front1")
map1.add_item(Item(1, (650, 400), "door", interactable=True, floor=True))
map1.add_item(Item(0, (381, 270), "case"))
map1.add_item(Item(0, (-50, 400), "bed"))
map1.sort_items()

map2 = Map(0, "bg2", "front2")
map2.add_item(Item(0, (310, 338), "dad"))
map2.add_item(Item(0, (476, 300), "sofa"))
map2.add_item(Item(0, (50, 350), "fridge"))
map2.add_item(Item(2, (500, 338), "mom", interactable=True))
map2.sort_items()

map3 = Map(0, "bg3", "front3")
map3.add_item(Item(3, (600, 338), "mystery", interactable=True))
map3.sort_items()

map4 = Map(0, "bg1", "front1")
map4.add_item(Item(4, (600, 338), "box", interactable=True))
map4.add_item(Item(0, (381, 270), "case"))
map4.add_item(Item(0, (-50, 400), "bed"))
map4.sort_items()

map5 = Map(0, "bg4", "front4")
map5.add_item(Item(6, (250, 350), "table", interactable=True))
map5.add_item(Item(5, (650, 450), "medicine", interactable=True))
map5.sort_items()

map6 = Map(0, "bg4", "front4")
map6.add_item(Item(6, (250, 350), "table"))
map6.sort_items()

map7 = Map(0, "bg5", "front5")
map7.add_item(Item(8, (250, 350), "hole1", interactable=True, floor=True))
map7.add_item(Item(7, (650, 450), "shovel", interactable=True))
map7.add_item(Item(0, (300, 500), "dog"))
map7.sort_items()

map8 = Map(0, "bg5", "front5")
map8.add_item(Item(8, (250, 350), "hole1"))
map8.add_item(Item(0, (300, 500), "dog"))
map8.sort_items()

map9 = Map(0, "bg6", "front6")
map9.add_item(Item(0, (100, 300), "vase"))
map9.add_item(Item(10, (400, 350), "cream", interactable=True))
map9.add_item(Item(9, (700, 450), "injector", interactable=True))
map9.sort_items()

map11 = Map(0, "bg4", "front4")
map11.add_item(Item(11, (250, 350), "table", interactable=True))
map11.sort_items()

map13 = Map(0, "bg5", "front5")
map13.add_item(Item(0, (300, 500), "dog"))
map13.add_item(Item(12, (250, 350), "hole2", interactable=True, floor=True))
map13.sort_items()

map15 = Map(0, "bg6", "front6")
map15.add_item(Item(13, (400, 350), "cream", interactable=True))
map15.add_item(Item(0, (100, 300), "vase"))
map15.sort_items()

map17 = Map(0, "bg1", "front1")
map17.add_item(Item(0, (381, 270), "case"))
map17.add_item(Item(0, (-50, 400), "bed"))
map17.add_item(Item(1, (650, 400), "door", interactable=True, floor=True))
map17.sort_items()

map18 = Map(0, "bg2", "front2")
map18.add_item(Item(0, (310, 338), "dad"))
map18.add_item(Item(0, (476, 300), "sofa"))
map18.add_item(Item(0, (50, 350), "fridge"))
map18.add_item(Item(2, (500, 338), "mom", interactable=True))
map18.sort_items()

map19 = Map(0, "bg3", "front3")
map19.add_item(Item(3, (600, 338), "mystery", interactable=True))
map19.sort_items()

map20 = Map(0, "bg1", "front1")
map20.add_item(Item(0, (381, 270), "case"))
map20.add_item(Item(0, (-50, 400), "bed"))
map20.add_item(Item(4, (600, 338), "box", interactable=True))
map20.sort_items()


maps = (map1, map2, map3, map4, map5, map6, map7, map8, map9,
        map11, map13, map15, map17, map18, map19, map20)