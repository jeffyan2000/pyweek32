from config import *

class Quest:
    def __init__(self, title, objective, completion):
        self.completed = False
        self.title = font_mission_title.render("Task: " + title, False, (0, 0, 0))
        self.objective = font_mission_desc.render("Objective: " + objective, False, (0, 0, 0))
        self.title2 = font_mission_title.render("Task: " + title, False, (255, 255, 255))
        self.objective2 = font_mission_desc.render("Objective: " + objective, False, (255, 255, 255))
        self.completion = completion

    def draw(self):
        screen.blit(texture_lib["mission"], (10, 5))
        screen.blit(self.title2, (72, 17))
        screen.blit(self.objective2, (72, 44))
        screen.blit(self.title, (70, 15))
        screen.blit(self.objective, (70, 43))

    def completed(self, *args):
        return self.completion(*args)


def q1_c(player):
    return player.current_map.id != 0


missions = (
    Quest("How to Play", "Walk to the door and interact with it", q1_c),
    Quest("How to Play", "Walk to the door and interact with it", q1_c),
)