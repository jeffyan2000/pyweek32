from config import *

class Quest:
    def __init__(self, title, objective, completion):
        self.completed = False
        self.title = font_mission_title.render("Task: " + title, False, (0, 0, 0))
        self.objective = font_mission_desc.render("Objective: " + objective, False, (0, 0, 0))
        self.title2 = font_mission_title.render("Task: " + title, False, (255, 255, 255))
        self.objective2 = font_mission_desc.render("Objective: " + objective, False, (255, 255, 255))
        self.completion = completion
        self.finished = False
        self.dead = False
        self.y = -100
        self.s = 0

    def draw(self):
        if self.y < 0:
            self.y += 10
        if self.finished:
            self.s += 1
            self.y += self.s
            if self.y > SCREEN_HEIGHT:
                self.dead = True
        screen.blit(texture_lib["mission"], (10, 5 + self.y))
        screen.blit(self.title2, (72, 17 + self.y))
        screen.blit(self.objective2, (72, 44 + self.y))
        screen.blit(self.title, (70, 15 + self.y))
        screen.blit(self.objective, (70, 43 + self.y))

    def completed(self, *args):
        return self.completion(*args)


def q1_c(player):
    return player.current_map.id != 0


missions = (
    Quest("How to Play", "Walk to the door and interact with it", q1_c),
    Quest("How to Play", "Walk to the door and interact with it", q1_c),
)