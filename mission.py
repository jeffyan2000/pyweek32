from config import *

class Quest:
    def __init__(self, title, objective, completion):
        self.completed = False
        self.title = title
        self.objective = objective
        self.completion = completion

    def draw(self):
        pass

    def completed(self, *args):
        return self.completion(*args)
