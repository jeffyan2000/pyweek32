from config import *

class ChatScene:
    def __init__(self, chat_name):
        self.conversation = []
        for sentence in chats[chat_name]:
            self.conversation.append(sentence)
        self.current_lines = []
        self.current_name = ""
        self.current_texture = "me_chat"
        self.next_dialog()
        self.dead = False

    def next_dialog(self):
        if self.conversation:
            next_c = self.conversation.pop(0)
            self.current_lines = []
            self.current_texture = next_c[2]
            self.current_name = font_chat_name.render(next_c[0], True, (0, 0, 0))
            current_line = ""
            sentence = next_c[1].split()
            for word in sentence:
                current_line += " " + word
                if font_chat_content.size(current_line)[0] > 650:
                    self.current_lines.append(current_line[:(-len(word))].strip())
                    current_line = word
            if current_line:
                self.current_lines.append(current_line.strip())
            for i in range(len(self.current_lines)):
                self.current_lines[i] = font_chat_content.render(self.current_lines[i], True, (0, 0, 0))
        else:
            self.dead = True

    def draw(self):
        pos = (- (ENV["mouse_x"] - SCREEN_WIDTH / 2) * (100 / 700) ** 2,
               - (ENV["mouse_y"] - SCREEN_HEIGHT / 2) * (100 / 700) ** 2)
        screen.blit(texture_lib[self.current_texture], pos)
        screen.blit(texture_lib["chat_box"], (0, 0))
        screen.blit(self.current_name, (95, 265))
        for i in range(len(self.current_lines)):
            screen.blit(self.current_lines[i], (75 - pos[0], 310 + i*25 - pos[1]))

class NextScene:
    def __init__(self, line):
        self.line = line
        self.text1 = font_next_day.render(self.line, True, (255, 255, 255))
        self.text2 = font_next_day.render(self.line, True, (200, 200, 200))
        self.text3 = font_next_day.render(self.line, True, (150, 150, 150))
        self.text4 = font_next_day.render(self.line, True, (100, 100, 100))
        self.circle_radius = 0
        self.display_countdown = 90
        self.pos = 0
        self.dead = False

    def draw(self):
        if self.circle_radius < 500 and self.display_countdown > 0:
            self.circle_radius += 20
            pygame.draw.circle(screen, (0, 0, 0), (400, 250), self.circle_radius)
        elif self.circle_radius > 0 and self.display_countdown <= 0:
            self.circle_radius -= 20
            pygame.draw.circle(screen, (0, 0, 0), (400, 250), self.circle_radius)
        elif self.display_countdown >= 1:
            self.display_countdown -= 1
            screen.fill(0)
            if self.pos+6 < len(q_s):
                screen.blit(self.text4, (q_s[self.pos], 220))
                screen.blit(self.text3, (q_s[self.pos+2], 220))
                screen.blit(self.text2, (q_s[self.pos+4], 220))
                screen.blit(self.text1, (q_s[self.pos+6], 220))
                self.pos += 1
        else:
            self.dead = True

chats = {
    "vase": (("me", "Hello how are you i'm fine thank you and you what is your we e name adf df d   my name is li ming ming",
     "me_chat"),
    ("person1", "Hello how are you i'm fine thank you and you what is your name my name is wang mei mei",
     "person1_chat")),
}