from config import *

class Item:
    def __init__(self, name, desc, texture):
        self.name = name
        self.desc = desc
        self.texture = texture_lib[texture]

    def draw(self):
        pass

items = {
    "example": ("example", "this is an example", "example_item")
}

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name):
        self.items[name] = Item(items[name][0], items[name][1], items[name][2])

    def has_item(self, name):
        return name in self.items

    def consume_item(self, name):
        del self.items[name]
