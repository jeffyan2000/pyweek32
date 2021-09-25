import pygame, sys, math, os, random
from cycles import *

pygame.init()
pygame.display.set_caption("regret, once again")
pygame.mouse.set_visible(False)

h_s = (0, 9, 16, 21, 24, 25, 24, 21, 16, 9, 0)
q_s = [800, 800, 800, 800, 800, 800]
q_speed = 70
while q_speed > 0:
    q_s.append((q_s[-1] - q_speed))
    q_speed -= 5
for _ in range(50):
    q_s.append(275)
q_speed = 0
while q_speed < 70:
    q_s.append((q_s[-1] - q_speed))
    q_speed += 5
for _ in range(20):
    q_s.append(-800)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
DEFAULT_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

ENV = {
    "delta_time": 0,
    "global_offset": (0, 0),
    "mouse_x": 0, "mouse_y": 0,
    "item_interact": None,
}


def handle_common_event(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEMOTION:
        new_mouse_pos = pygame.mouse.get_pos()
        ENV["delta_x"] = new_mouse_pos[0] - ENV["mouse_x"]
        ENV["delta_y"] = new_mouse_pos[1] - ENV["mouse_y"]
        ENV["mouse_x"], ENV["mouse_y"] = new_mouse_pos


def draw_at_frame(pos, sheet, frame, size):
    screen.blit(texture_lib[sheet], pos, pygame.Rect((frame * size[0], 0), size))

# ----------------------------------- Load Textures -------------------------------------------
textures = os.listdir("textures")
texture_lib = {}


def load(n):
    return pygame.image.load(os.path.join("textures", n + ".png")).convert_alpha()


def add_left(names):
    for name in names:
        texture_lib[name+"_left"] = pygame.transform.flip(texture_lib[name], True, False)


texture_names = [name for name in textures]
for name in texture_names:
    if name.endswith(".png"):
        texture_lib[name[:-4]] = load(name[:-4])

add_left(("me",))

# ----------------------------------------- Audio ----------------------------------------------


class AudioPlayer:
    def __init__(self, id_in, type_in, volume=0.2):
        self.id = id_in
        self.music = pygame.mixer.Sound(id_in + ".ogg")
        self.music.set_volume(volume)
        if type_in == "bg":
            self.channel = pygame.mixer.Channel(1)
        if type_in == "se":
            self.channel = pygame.mixer.Channel(2)
        if type_in == "sn":
            self.channel = pygame.mixer.Channel(3)

    def play_non_stop(self):
        self.channel.play(self.music, -1)

    def play_once(self):
        self.channel.play(self.music, 0)

    def stop(self):
        self.channel.stop()


font_mission_title = pygame.font.Font(os.path.join("fonts", "Action_Man_Bold.ttf"), 25)
font_mission_desc = pygame.font.Font(os.path.join("fonts", "Action_Man_Bold.ttf"), 20)
font_chat_name = pygame.font.Font(os.path.join("fonts", "Action_Man_Bold.ttf"), 28)
font_chat_content = pygame.font.Font(os.path.join("fonts", "Action_Man_Bold.ttf"), 30)
font_next_day = pygame.font.Font(os.path.join("fonts", "Romelio.ttf"), 40)


from math import sqrt

def distance(pos1, pos2):
    return sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)