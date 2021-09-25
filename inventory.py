from config import *

class Item:
    def __init__(self, texture):
        self.texture = texture_lib["item_" + texture]
        self.name = texture


class Inventory:
    def __init__(self):
        self.items = []

    def clear(self):
        self.items = []

    def add_item(self, name):
        self.items.append(Item(name))

    def has_item(self, name):
        for item in self.items:
            if item.name == name:
                return True
        return False

    def consume_item(self, name):
        length = len(self.items)
        for i in range(length):
            if self.items[i].name == name:
                del self.items[i]
                break

    def draw(self):
        for i in range(9):
            if 40 + i * 80 < ENV["mouse_x"] < 110 + i * 80:
                if 400 < ENV["mouse_y"] < 470:
                    screen.blit(texture_lib["item_select"], (40 + i*80, 400))
            screen.blit(texture_lib["item_slot"], (40 + i*80, 400))
            if len(self.items) > i:
                screen.blit(self.items[i].texture, (35 + i * 80, 395))
            screen.blit(texture_lib["item_slot_f"], (40 + i * 80, 400))